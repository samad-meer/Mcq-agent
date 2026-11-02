import json
import math
import os
import random
import tempfile
import unittest
from collections import Counter
from unittest import mock

import httpx2
import openai
from PIL import Image

import mcq_agent
from mcq_agent import AgentStop, Navigation, Option, Point, Question, ScreenRead

# 1001 pixels wide, so a grid position is also its screen position.
MONITOR = {"left": 0, "top": 0, "width": 1001, "height": 1001}
SCREEN = {"left": 0, "top": 0, "width": 1920, "height": 1080}
SUBMIT, NEXT = Point(x=500, y=600), Point(x=700, y=600)


def question(text="What is 2 + 2?", answers=("B",), selected=(), options=("3", "4", "5"), y=200, cut_off=False):
    """A question whose first line sits 50 px above its first option, which is at y."""
    labelled = [
        Option(label=label, text=option, position=Point(x=100, y=y + 50 * index))
        for index, (label, option) in enumerate(zip("ABC", options))
    ]
    return Question(text=text, position=Point(x=300, y=y - 50), options=labelled, answers=list(answers),
                    selected=list(selected), reason="Sum.", cut_off=cut_off)


def screen(*questions, action="none", position=None, label="", records="unknown", remaining="unknown", blank=None):
    navigation = Navigation(action=action, position=position, label=label, records=records, remaining=remaining, blank=blank)
    return ScreenRead(questions=list(questions), navigation=navigation)


def submit_screen(*questions, position=SUBMIT, label="Submit answer", records="unknown", remaining="more"):
    return screen(*questions, action="submit", position=position, label=label, records=records, remaining=remaining)


def next_screen(*questions, position=NEXT, label="Next", remaining="more"):
    return screen(*questions, action="next", position=position, label=label, remaining=remaining)


# Every random pick lands in the middle of its range, so positions and timings are predictable.
STILL = mock.Mock(uniform=lambda low, high: (low + high) / 2, randint=lambda low, high: (low + high) // 2)
REST_X = MONITOR["width"] - 1 - mcq_agent.EDGE_INSET - mcq_agent.REST_SPREAD // 2
PRESS = sum(mcq_agent.PRESS_SECONDS) / 2
DWELL = sum(mcq_agent.DWELL_SECONDS) / 2


class KeyTest(unittest.TestCase):
    def test_question_numbers_are_dropped_but_other_numbers_are_kept(self):
        self.assertEqual(mcq_agent.normalize("Q3. What is 2 + 2?", numbered=True), "what is 2 2")
        self.assertEqual(mcq_agent.normalize("Question 12: Pick one", numbered=True), "pick one")
        self.assertEqual(mcq_agent.normalize("3.14 is which constant?", numbered=True), "3 14 is which constant")
        self.assertEqual(mcq_agent.normalize("10:30"), "10 30")
        self.assertEqual(mcq_agent.normalize("2.5 + 2.5"), "2 5 2 5")

    def test_feedback_around_a_submitted_question_still_matches(self):
        key = mcq_agent.question_key(question())
        for text in ("What is 2 + 2? Correct!", "Correct! What is 2 + 2?", "Incorrect - What is 2 + 2?"):
            self.assertEqual(mcq_agent.key_of(question(text), {}, {key}), key, text)

    def test_rewritten_or_added_options_after_a_submit_still_match(self):
        key = mcq_agent.question_key(question())
        rewritten = question(options=("3", "Correct answer: 4", "5"))
        extended = question(options=("3", "4", "5"))
        extended.options.append(Option(label="D", text="Explanation: two and two", position=Point(x=100, y=350)))
        self.assertEqual(mcq_agent.key_of(rewritten, {}, {key}), key)
        self.assertEqual(mcq_agent.key_of(extended, {}, {key}), key)

    def test_short_options_are_matched_as_whole_words(self):
        key = mcq_agent.question_key(question(options=("1", "4", "5")))
        other = question(options=("11", "4", "5"))
        self.assertNotEqual(mcq_agent.key_of(other, {}, {key}), key)

    def test_fresh_questions_only_match_exactly(self):
        key = mcq_agent.question_key(question("Is a cat a mammal?"))
        longer = question("Is a cat a mammal? Think about milk.")
        self.assertNotEqual(mcq_agent.key_of(longer, {key: ["B"]}), key)


class PendingClicksTest(unittest.TestCase):
    def test_unanswered_question_is_clicked(self):
        pending = mcq_agent.pending_clicks(screen(question()), {}, Counter())
        self.assertEqual([o.label for o in pending[0][1]], ["B"])

    def test_correctly_marked_question_is_skipped(self):
        self.assertEqual(mcq_agent.pending_clicks(screen(question(selected=["B"])), {}, Counter()), [])

    def test_multi_select_clicks_only_what_is_missing(self):
        read = screen(question(answers=["A", "C"], selected=["A"]))
        pending = mcq_agent.pending_clicks(read, {}, Counter())
        self.assertEqual([o.label for o in pending[0][1]], ["C"])

    def test_changed_answer_on_a_later_read_does_not_flip_selection(self):
        decided = {}
        mcq_agent.pending_clicks(screen(question(answers=["B"])), decided, Counter())
        read = screen(question(answers=["C"], selected=["B"]))
        self.assertEqual(mcq_agent.pending_clicks(read, decided, Counter()), [])

    def test_question_text_is_matched_ignoring_case_spacing_and_punctuation(self):
        decided = {}
        mcq_agent.pending_clicks(screen(question("Q3. What is  2 + 2?")), decided, Counter())
        read = screen(question("what is 2+2", answers=["C"], selected=["B"]))
        self.assertEqual(mcq_agent.pending_clicks(read, decided, Counter()), [])

    def test_same_wording_with_other_options_is_another_question(self):
        decided = {}
        mcq_agent.pending_clicks(screen(question("Which is true?")), decided, Counter())
        read = screen(question("Which is true?", answers=["C"], options=("x", "y", "z")))
        pending = mcq_agent.pending_clicks(read, decided, Counter())
        self.assertEqual([o.label for o in pending[0][1]], ["C"])

    def test_question_shown_twice_in_one_read_is_clicked_once(self):
        pending = mcq_agent.pending_clicks(screen(question(), question()), {}, Counter())
        self.assertEqual(len(pending), 1)

    def test_stops_when_clicks_keep_failing(self):
        attempts = Counter({mcq_agent.question_key(question()): mcq_agent.MAX_ATTEMPTS})
        with self.assertRaises(AgentStop):
            mcq_agent.pending_clicks(screen(question()), {}, attempts)

    def test_submitted_question_is_left_alone_even_with_feedback_added(self):
        submitted = {mcq_agent.question_key(question())}
        read = screen(question("What is 2 + 2? Correct, well done!"))
        self.assertEqual(mcq_agent.pending_clicks(read, {}, Counter(), submitted), [])

    def test_cut_off_question_is_neither_clicked_nor_decided(self):
        decided = {}
        read = screen(question(answers=["A"], options=("3", "4"), cut_off=True))
        self.assertEqual(mcq_agent.pending_clicks(read, decided, Counter()), [])
        self.assertEqual(decided, {})


class CoordinatesTest(unittest.TestCase):
    def test_grid_scales_to_a_1080p_screen(self):
        self.assertEqual(mcq_agent.to_screen(Point(x=500, y=500), SCREEN), (960, 540))

    def test_grid_scales_to_a_4k_screen(self):
        monitor = {"left": 0, "top": 0, "width": 3840, "height": 2160}
        self.assertEqual(mcq_agent.to_screen(Point(x=500, y=500), monitor), (1920, 1080))

    def test_corners_are_pulled_one_pixel_in_so_the_abort_never_fires_by_itself(self):
        self.assertEqual(mcq_agent.to_screen(Point(x=1000, y=1000), SCREEN), (1918, 1078))
        self.assertEqual(mcq_agent.to_screen(Point(x=0, y=0), SCREEN), (1, 1))

    def test_monitor_offset_is_applied(self):
        monitor = {"left": 1920, "top": 100, "width": 1001, "height": 1001}
        self.assertEqual(mcq_agent.to_screen(Point(x=10, y=20), monitor), (1930, 120))

    def test_off_grid_point_is_rejected(self):
        with self.assertRaises(AgentStop):
            mcq_agent.to_screen(Point(x=1500, y=20), MONITOR)

    def test_downscaled_capture_keeps_shape(self):
        shot = mock.Mock(size=(3840, 2160), rgb=bytes(3840 * 2160 * 3))
        sct = mock.Mock(grab=mock.Mock(return_value=shot))
        self.assertEqual(mcq_agent.capture(sct, MONITOR).size, (1920, 1080))


class FitScrollTest(unittest.TestCase):
    def test_brings_the_first_line_up_to_the_top_of_the_page_area(self):
        # 400 grid rows down is 400 px on the 1001-px monitor: four notches of 100 px.
        self.assertEqual(mcq_agent.fit_scroll(Point(x=300, y=600), MONITOR), -4 * mcq_agent.WHEEL_NOTCH)

    def test_scales_with_the_screen(self):
        # The same 400 rows are 432 px on a 1080-px screen, still four notches.
        self.assertEqual(mcq_agent.fit_scroll(Point(x=300, y=600), SCREEN), -4 * mcq_agent.WHEEL_NOTCH)

    def test_always_scrolls_at_least_one_notch(self):
        self.assertEqual(mcq_agent.fit_scroll(Point(x=300, y=150), MONITOR), -mcq_agent.WHEEL_NOTCH)


class ActionTest(unittest.TestCase):
    def action(self, model_says, label, remaining="more"):
        return mcq_agent.intended_action(screen(action=model_says, label=label, remaining=remaining).navigation)

    def test_the_label_decides_between_next_and_submit(self):
        self.assertEqual(self.action("submit", "Next"), "next")
        self.assertEqual(self.action("next", "Submit answer"), "submit")
        self.assertEqual(self.action("next", "Submit & Next"), "submit")
        self.assertEqual(self.action("submit", "→"), "next")
        self.assertEqual(self.action("submit", ""), "submit")

    def test_labels_that_end_or_reverse_the_quiz_are_never_clicked(self):
        for label in ("Finish", "Finished", "Submit quiz", "Submit exams", "Terminar examen", "Send", "Turn in", "Grade"):
            self.assertEqual(self.action("next", label), "finish", label)
        for label in ("Previous", "Back to quiz", "< Prev"):
            self.assertEqual(self.action("next", label), "none", label)

    def test_feedback_is_not_mistaken_for_back(self):
        self.assertEqual(self.action("next", "Feedback"), "next")

    def test_unlabelled_next_on_the_last_page_is_left_to_the_user(self):
        self.assertEqual(self.action("next", "", remaining="last"), "finish")
        self.assertEqual(self.action("next", "Next", remaining="last"), "next")


class RunLoopTest(unittest.TestCase):
    """Drives run() with scripted screens, recording clicks instead of performing them."""

    def play(self, reads, max_steps=20):
        """Returns the click positions and scroll count; self.calls keeps every screen and mouse call in order."""
        reads = iter(reads)
        self.calls = mock.Mock()
        with (
            mock.patch.object(mcq_agent, "capture", return_value=None) as capture,
            mock.patch.object(mcq_agent, "read_screen", side_effect=lambda *_: next(reads)),
            mock.patch.object(mcq_agent, "wobble", STILL),
            mock.patch.object(mcq_agent, "glide") as glide,
            mock.patch.object(mcq_agent.time, "sleep") as sleep,
            mock.patch.object(mcq_agent.pyautogui, "click") as click,
            mock.patch.object(mcq_agent.pyautogui, "scroll") as scroll,
            mock.patch("builtins.print") as printed,
        ):
            for name, child in [("capture", capture), ("sleep", sleep), ("glide", glide), ("click", click), ("scroll", scroll)]:
                self.calls.attach_mock(child, name)
            mcq_agent.run(None, None, None, MONITOR, max_steps)
        self.printed = " ".join(str(c.args[0]) for c in printed.call_args_list if c.args)
        return [c.args for c in click.call_args_list], scroll.call_count

    def test_first_read_waits_for_the_mouse_to_rest_away_from_the_options(self):
        self.play([screen(action="finish")])
        self.assertEqual(self.calls.mock_calls[:3], [
            mock.call.glide(REST_X, 500, MONITOR, pace=1.3),
            mock.call.sleep(mcq_agent.WAIT_SECONDS),
            mock.call.capture(None, MONITOR),
        ])

    def test_mouse_moves_to_the_option_pauses_clicks_lingers_and_then_rests_away_from_it(self):
        self.play([
            screen(question("Q1"), action="none"),
            screen(question("Q1", selected=["B"]), action="finish"),
        ])
        self.assertEqual(self.calls.mock_calls[3:8], [
            mock.call.glide(100, 250, MONITOR),
            mock.call.sleep(PRESS),
            mock.call.click(100, 250),
            mock.call.sleep(DWELL),
            mock.call.glide(REST_X, 250, MONITOR, pace=1.3),
        ])

    def test_mouse_rests_on_the_blank_spot_the_model_found_but_not_after_moving_on(self):
        self.play([
            screen(question("Q1"), action="none", blank=Point(x=800, y=700)),
            next_screen(question("Q1", selected=["B"]), blank=Point(x=800, y=700)) if False else
            screen(question("Q1", selected=["B"]), action="next", position=NEXT, label="Next", remaining="more", blank=Point(x=800, y=700)),
            screen(action="finish"),
        ])
        glides = [c for c in self.calls.mock_calls if c[0] == "glide"]
        self.assertEqual(glides[2], mock.call.glide(800, 700, MONITOR, pace=1.3))  # after the option click
        self.assertEqual(glides[4], mock.call.glide(REST_X, 600, MONITOR, pace=1.3))  # after Next: the page changes

    def test_scrolls_with_the_mouse_over_the_page(self):
        _, scrolls = self.play([
            screen(question("Q1", selected=["B"]), action="scroll"),
            screen(question("Q2", selected=["B"]), action="finish"),
        ])
        self.assertEqual(scrolls, 1)
        self.assertEqual(self.calls.mock_calls[3:6], [
            mock.call.glide(500, 500, MONITOR),
            mock.call.scroll(mcq_agent.SCROLL_AMOUNT),
            mock.call.glide(REST_X, 500, MONITOR, pace=1.3),
        ])

    def test_submits_the_answer_then_clicks_next(self):
        clicks, _ = self.play([
            submit_screen(question("Q1")),
            submit_screen(question("Q1", selected=["B"])),
            next_screen(question("Q1", selected=[])),
            screen(action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (500, 600), (700, 600)])

    def test_submits_again_when_the_first_click_did_not_register_then_gives_up(self):
        clicks, _ = self.play([submit_screen(question("Q1"))] + [submit_screen(question("Q1", selected=["B"]))] * 8)
        self.assertEqual(clicks, [(100, 250), (500, 600), (500, 600)])
        self.assertIn("stopped changing", self.printed)

    def test_jittery_positions_do_not_defeat_the_stuck_detector(self):
        reads = [submit_screen(question("Q1", selected=["B"]), position=Point(x=500 + i % 3, y=600 - i % 2)) for i in range(10)]
        clicks, _ = self.play(reads)
        self.assertEqual(len(clicks), mcq_agent.MAX_STUCK)

    def test_submits_each_question_on_a_page_and_reclicks_one_that_lost_its_selection(self):
        first, second = Point(x=500, y=350), Point(x=500, y=650)
        q1 = lambda selected: question("Q1", selected=selected)
        q2 = lambda selected: question("Q2", answers=["A"], selected=selected, y=500)
        clicks, _ = self.play([
            submit_screen(q1([]), q2([]), position=first),
            submit_screen(q1(["B"]), q2(["A"]), position=first),
            submit_screen(q1(["B"]), q2([]), position=second),
            submit_screen(q1(["B"]), q2(["A"]), position=second),
            next_screen(q1(["B"]), q2(["A"])),
            screen(action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (100, 500), (500, 350), (100, 500), (500, 650), (700, 600)])

    def test_stale_read_after_next_still_reaches_the_next_question(self):
        clicks, _ = self.play([
            submit_screen(question("Q1")),
            submit_screen(question("Q1", selected=["B"])),
            next_screen(question("Q1", selected=["B"])),
            next_screen(question("Q1", selected=["B"])),
            screen(question("Q2", answers=["A"]), action="finish"),
            screen(question("Q2", answers=["A"], selected=["A"]), action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (500, 600), (700, 600), (700, 600), (100, 200)])

    def test_question_with_feedback_added_after_submit_is_not_clicked_again(self):
        clicks, _ = self.play([
            submit_screen(question()),
            submit_screen(question(selected=["B"])),
            next_screen(question("Correct! What is 2 + 2?", selected=[], options=("3", "Correct answer: 4", "5"))),
            screen(action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (500, 600), (700, 600)])

    def test_answers_the_last_question_but_leaves_its_submit_to_the_user(self):
        clicks, _ = self.play([
            submit_screen(question("Q1"), remaining="last"),
            submit_screen(question("Q1", selected=["B"]), remaining="last"),
        ])
        self.assertEqual(clicks, [(100, 250)])
        self.assertIn("last question", self.printed)

    def test_refuses_a_submit_that_sounds_like_the_end_of_the_quiz(self):
        for label in ("Submit quiz", "Finish", "Submit all answers", "End test", "Done", "Submit assessment", "Enviar"):
            clicks, _ = self.play([submit_screen(question(selected=["B"]), label=label, records="this question")])
            self.assertEqual(clicks, [], label)

    def test_bare_submit_is_clicked_only_when_the_model_says_it_records_this_question(self):
        clicks, _ = self.play([submit_screen(question(selected=["B"]), label="Submit", records="unknown")])
        self.assertEqual(clicks, [])
        self.assertIn("records one answer or ends the quiz", self.printed)
        clicks, _ = self.play([submit_screen(question(selected=["B"]), label="Submit", records="whole quiz")])
        self.assertEqual(clicks, [])
        clicks, _ = self.play([
            submit_screen(question(selected=["B"]), label="Submit", records="this question", remaining="unknown"),
            screen(action="finish"),
        ])
        self.assertEqual(clicks, [(500, 600)])

    def test_labels_that_promise_one_answer_or_moving_on_are_clicked_without_a_counter(self):
        for label in ("Check", "Submit & Next", "Submit answer", "Save and continue"):
            clicks, _ = self.play([
                submit_screen(question("Q1"), label=label, remaining="unknown"),
                submit_screen(question("Q1", selected=["B"]), label=label, remaining="unknown"),
                screen(action="finish"),
            ])
            self.assertEqual(clicks, [(100, 250), (500, 600)], label)

    def test_refuses_a_submit_with_no_question_in_view(self):
        clicks, _ = self.play([submit_screen()])
        self.assertEqual(clicks, [])
        self.assertIn("No question is in view", self.printed)

    def test_submits_a_question_the_user_had_already_answered(self):
        clicks, _ = self.play([submit_screen(question(selected=["B"])), screen(action="finish")])
        self.assertEqual(clicks, [(500, 600)])

    def test_control_that_says_next_is_treated_as_next_even_if_called_submit(self):
        clicks, _ = self.play([
            submit_screen(question("Q1"), label="Next"),
            submit_screen(question("Q1", selected=["B"]), label="Next"),
            screen(question("Q2", answers=["A"]), action="finish"),
            screen(question("Q2", answers=["A"], selected=["A"]), action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (500, 600), (100, 200)])

    def test_control_that_says_submit_answer_is_treated_as_submit_even_if_called_next(self):
        clicks, _ = self.play([
            next_screen(question("Q1"), label="Submit answer"),
            next_screen(question("Q1", selected=["B"]), label="Submit answer"),
            next_screen(question("Q1", selected=[])),
            screen(action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (700, 600), (700, 600)])

    def test_icon_only_next_is_clicked_unless_it_is_the_last_page(self):
        clicks, _ = self.play([next_screen(question(selected=["B"]), label="→"), screen(action="finish")])
        self.assertEqual(clicks, [(700, 600)])
        clicks, _ = self.play([next_screen(question(selected=["B"]), label="", remaining="last")])
        self.assertEqual(clicks, [])

    def test_never_clicks_a_next_that_is_really_previous(self):
        clicks, _ = self.play([next_screen(question(selected=["B"]), label="Previous")] * 5)
        self.assertEqual(clicks, [])

    def test_next_that_would_end_the_quiz_is_left_to_the_user(self):
        clicks, _ = self.play([next_screen(question(selected=["B"]), label="Finish")])
        self.assertEqual(clicks, [])

    def test_next_is_still_clicked_on_the_last_question(self):
        clicks, _ = self.play([next_screen(question(selected=["B"]), remaining="last"), screen(action="finish")])
        self.assertEqual(clicks, [(700, 600)])

    def test_questions_with_the_same_wording_but_other_options_are_answered_separately(self):
        clicks, _ = self.play([
            next_screen(question("Which is true?")),
            next_screen(question("Which is true?", selected=["B"])),
            screen(question("Which is true?", answers=["C"], options=("x", "y", "z")), action="finish"),
            screen(question("Which is true?", answers=["C"], selected=["C"], options=("x", "y", "z")), action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (700, 600), (100, 300)])

    def test_going_back_to_an_earlier_question_stops_the_run(self):
        clicks, _ = self.play([
            next_screen(question("Q1")),
            next_screen(question("Q1", selected=["B"])),
            next_screen(question("Q2", answers=["A"])),
            next_screen(question("Q2", answers=["A"], selected=["A"])),
        ] + [next_screen(question("Q1", selected=["B"]))] * 6)
        self.assertEqual(clicks, [(100, 250), (700, 600), (100, 200), (700, 600), (700, 600)])

    def test_answers_then_clicks_next_then_stops_at_submit(self):
        clicks, _ = self.play([
            next_screen(question("Q1")),
            next_screen(question("Q1", selected=["B"])),
            screen(question("Q2", answers=["A"]), action="finish"),
            screen(question("Q2", answers=["A"], selected=["A"]), action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (700, 600), (100, 200)])

    def test_never_clicks_the_finish_button(self):
        clicks, _ = self.play([screen(question(selected=["B"]), action="finish", position=SUBMIT, label="Submit")])
        self.assertEqual(clicks, [])

    def test_page_that_advances_by_itself_gets_no_next_click(self):
        clicks, _ = self.play([
            next_screen(question("Q1")),
            screen(question("Q2", answers=["C"]), action="finish"),
            screen(question("Q2", answers=["C"], selected=["C"]), action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (100, 300)])

    def test_next_button_that_appears_after_answering_is_used(self):
        clicks, _ = self.play([
            screen(question("Q1"), action="none"),
            next_screen(question("Q1", selected=["B"])),
            screen(action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (700, 600)])

    def test_stops_when_next_does_not_change_the_page(self):
        clicks, _ = self.play([next_screen(question(selected=["B"]))] * 10)
        self.assertEqual(len(clicks), mcq_agent.MAX_STUCK)

    def test_stops_when_there_is_no_quiz(self):
        clicks, _ = self.play([screen()] * 10)
        self.assertEqual(clicks, [])

    def test_stops_when_a_click_never_registers(self):
        with self.assertRaises(AgentStop):
            self.play([screen(question())] * 10)

    def test_scrolls_a_cut_off_question_into_view_before_answering(self):
        tall = question("Q1", answers=[], options=("3", "4"), y=700, cut_off=True)
        clicks, scrolls = self.play([
            screen(tall, action="scroll"),
            next_screen(question("Q1", y=300)),
            next_screen(question("Q1", y=300, selected=["B"])),
            screen(action="finish"),
        ])
        self.assertEqual(scrolls, 1)
        self.calls.scroll.assert_called_once_with(mcq_agent.fit_scroll(tall.position, MONITOR))
        self.assertEqual(clicks, [(100, 350), (700, 600)])
        self.assertIn("Scrolling to see the rest of: Q1", self.printed)

    def test_second_scroll_for_the_same_question_is_a_small_step(self):
        tall = question("Q1", answers=[], options=("3", "4"), y=700, cut_off=True)
        nearer = question("Q1", answers=[], options=("3", "4"), y=400, cut_off=True)
        clicks, _ = self.play([
            screen(tall, action="scroll"),
            screen(nearer, action="scroll"),
            next_screen(question("Q1", y=300)),
            next_screen(question("Q1", y=300, selected=["B"])),
            screen(action="finish"),
        ])
        self.assertEqual(self.calls.scroll.call_args_list, [
            mock.call(mcq_agent.fit_scroll(tall.position, MONITOR)),
            mock.call(mcq_agent.FIT_STEP),
        ])
        self.assertEqual(clicks, [(100, 350), (700, 600)])

    def test_question_that_never_fits_asks_for_a_zoom_out(self):
        tall = question("Q1", answers=[], options=("3", "4"), y=700, cut_off=True)
        with self.assertRaisesRegex(AgentStop, "Zoom the browser out"):
            self.play([screen(tall, action="scroll")] * 10)

    def test_complete_questions_on_the_screen_are_answered_before_scrolling_for_a_cut_off_one(self):
        tall = question("Q2", answers=[], options=("3", "4"), y=800, cut_off=True)
        clicks, scrolls = self.play([
            screen(question("Q1"), tall, action="scroll"),
            screen(question("Q1", selected=["B"]), tall, action="scroll"),
            screen(question("Q2", answers=["A"], y=300), action="finish"),
            screen(question("Q2", answers=["A"], selected=["A"], y=300), action="finish"),
        ])
        self.assertEqual(clicks, [(100, 250), (100, 300)])
        self.assertEqual(scrolls, 1)


class PrintTest(unittest.TestCase):
    def test_cut_off_question_says_so_instead_of_giving_a_reason(self):
        with mock.patch("builtins.print") as printed:
            mcq_agent.print_question(question(answers=[], cut_off=True), [])
        text = " ".join(str(c.args[0]) for c in printed.call_args_list)
        self.assertIn("below the screen edge", text)
        self.assertNotIn("Why", text)


class RestTest(unittest.TestCase):
    def test_fallback_spot_stays_off_the_corners_below_the_browser_bar_and_above_the_taskbar(self):
        offset = {"left": 1920, "top": 100, "width": 1001, "height": 1001}
        with mock.patch.object(mcq_agent, "wobble", STILL), mock.patch.object(mcq_agent, "glide") as glide:
            mcq_agent.rest(MONITOR, 0)
            mcq_agent.rest(MONITOR, 1000)
            mcq_agent.rest(offset, 0)
            mcq_agent.rest(offset, 2000)
        highest, lowest = mcq_agent.TOP_MARGIN, MONITOR["height"] - 1 - mcq_agent.TASKBAR_MARGIN
        self.assertEqual(glide.call_args_list, [
            mock.call(REST_X, highest, MONITOR, pace=1.3),
            mock.call(REST_X, lowest, MONITOR, pace=1.3),
            mock.call(REST_X + 1920, highest + 100, offset, pace=1.3),
            mock.call(REST_X + 1920, lowest + 100, offset, pace=1.3),
        ])

    def test_rests_near_the_blank_spot_the_model_found(self):
        with mock.patch.object(mcq_agent, "wobble", STILL), mock.patch.object(mcq_agent, "glide") as glide:
            mcq_agent.rest(MONITOR, 250, Point(x=800, y=700))
        self.assertEqual(glide.call_args_list, [mock.call(800, 700, MONITOR, pace=1.3)])

    def test_blank_spot_off_the_grid_falls_back_to_the_edge(self):
        with mock.patch.object(mcq_agent, "wobble", STILL), mock.patch.object(mcq_agent, "glide") as glide:
            mcq_agent.rest(MONITOR, 250, Point(x=1200, y=700))
        self.assertEqual(glide.call_args_list, [mock.call(REST_X, 250, MONITOR, pace=1.3)])

    def test_resting_spot_varies_between_visits(self):
        with mock.patch.object(mcq_agent, "wobble", random.Random(3)), mock.patch.object(mcq_agent, "glide") as glide:
            mcq_agent.rest(MONITOR, 500)
            mcq_agent.rest(MONITOR, 500)
        first, second = [c.args[:2] for c in glide.call_args_list]
        self.assertNotEqual(first, second)

    def test_tiny_monitor_is_rejected(self):
        with self.assertRaises(AgentStop):
            mcq_agent.rest({"left": 0, "top": 0, "width": 2, "height": 2}, 1)


class GlideTest(unittest.TestCase):
    def trace(self, start, target, seed, pace=1.0):
        with (
            mock.patch.object(mcq_agent, "wobble", random.Random(seed)),
            mock.patch.object(mcq_agent.pyautogui, "position", return_value=start),
            mock.patch.object(mcq_agent.pyautogui, "moveTo") as move_to,
            mock.patch.object(mcq_agent.time, "sleep") as sleep,
        ):
            mcq_agent.glide(*target, SCREEN, pace=pace)
        return move_to.call_args_list, sum(c.args[0] for c in sleep.call_args_list)

    def test_path_stays_on_screen_off_the_corners_and_ends_exactly_on_the_target(self):
        corners = {(0, 0), (1919, 0), (0, 1079), (1919, 1079)}
        starts = [(1916, 540), (5, 5), (1914, 1000), (960, 1), (1, 1078), (1918, 1), (-800, 300), (2500, -200)]
        targets = [(100, 400), (1918, 1078), (1, 1), (1850, 60), (60, 1050), (960, 540)]
        for seed in range(25):
            for start in starts:
                for target in targets:
                    calls, _ = self.trace(start, target, seed)
                    self.assertEqual(calls[-1], mock.call(*target))
                    for c in calls[:-1]:
                        x, y = c.args
                        self.assertTrue(1 <= x <= 1918 and 1 <= y <= 1078, (start, target, seed, x, y))
                        self.assertNotIn((x, y), corners, (start, target, seed))
                        self.assertEqual(c.kwargs, {"_pause": False})

    def test_motion_is_smooth_eased_and_gently_curved(self):
        start, target = (1916, 540), (300, 400)
        bends = []
        for seed in range(20):
            calls, seconds = self.trace(start, target, seed)
            points = [start] + [c.args for c in calls]
            steps = len(calls) - 1
            self.assertTrue(abs(steps - seconds * 90) <= 1 or steps == 8, (steps, seconds))
            hops = [math.dist(a, b) for a, b in zip(points, points[1:-1])]
            self.assertLessEqual(max(hops), 1.6 * sum(hops) / len(hops))  # no jumps
            peak = hops.index(max(hops))
            self.assertTrue(steps // 4 <= peak <= 3 * steps // 4 and hops[0] < max(hops) > hops[-1])  # eased
            chord = math.dist(start, target)
            bends.append(max(abs((p[0] - start[0]) * (target[1] - start[1]) - (p[1] - start[1]) * (target[0] - start[0])) / chord
                             for p in points[1:-1]))
        self.assertGreater(max(bends), 3)
        self.assertLess(max(bends), 0.12 * chord)

    def test_short_moves_are_quicker_and_pace_scales_the_time(self):
        for seed in range(10):
            _, long = self.trace((1916, 540), (300, 400), seed)
            _, short = self.trace((1916, 540), (1856, 540), seed)
            _, lazy = self.trace((1916, 540), (300, 400), seed, pace=1.3)
            self.assertLess(short, long)
            self.assertTrue(0.15 <= short <= 0.4 and 0.4 <= long <= 1.0, (short, long))
            self.assertAlmostEqual(lazy, long * 1.3, places=6)

    def test_tiny_moves_jump_straight_there(self):
        calls, _ = self.trace((300, 400), (301, 400), 1)
        self.assertEqual(calls, [mock.call(301, 400)])


class DryRunTest(unittest.TestCase):
    def test_points_at_each_answer_without_clicking_and_saves_targets(self):
        read = next_screen(question(answers=["A", "C"]))
        image = Image.new("RGB", (640, 360))
        with tempfile.TemporaryDirectory() as folder:
            debug_image = os.path.join(folder, "read.jpg")
            with (
                mock.patch.object(mcq_agent, "DEBUG_IMAGE", debug_image),
                mock.patch.object(mcq_agent, "capture", return_value=image),
                mock.patch.object(mcq_agent, "read_screen", return_value=read),
                mock.patch.object(mcq_agent, "wobble", STILL),
                mock.patch.object(mcq_agent, "glide") as glide,
                mock.patch.object(mcq_agent.time, "sleep") as sleep,
                mock.patch.object(mcq_agent.pyautogui, "click") as click,
                mock.patch.object(mcq_agent.pyautogui, "scroll") as scroll,
                mock.patch("builtins.print"),
            ):
                mcq_agent.dry_run(None, None, None, MONITOR)
            self.assertTrue(os.path.exists(debug_image))
        self.assertEqual(glide.call_args_list, [
            mock.call(REST_X, 500, MONITOR, pace=1.3),
            mock.call(100, 200, MONITOR),
            mock.call(100, 300, MONITOR),
        ])
        self.assertEqual(sleep.call_args_list, [
            mock.call(mcq_agent.WAIT_SECONDS), mock.call(mcq_agent.POINT_SECONDS), mock.call(mcq_agent.POINT_SECONDS),
        ])
        click.assert_not_called()
        scroll.assert_not_called()


class MakeClientTest(unittest.TestCase):
    def test_missing_key_names_the_variable_to_set(self):
        with mock.patch.dict(os.environ, clear=True):
            with self.assertRaisesRegex(AgentStop, "XAI_API_KEY"):
                mcq_agent.make_client(mcq_agent.PROVIDERS["grok"])

    def test_local_needs_no_key(self):
        with mock.patch.dict(os.environ, clear=True):
            client = mcq_agent.make_client(mcq_agent.PROVIDERS["local"])
        self.assertEqual(str(client.base_url), "http://localhost:11434/v1/")


class ReadScreenTest(unittest.TestCase):
    """Runs read_screen through the real SDK against a fake HTTP server."""

    def call(self, provider="grok", replies=None, finish_reason="stop", refusal=None):
        expected = next_screen(question())
        replies = iter(replies or [expected.model_dump_json()])
        self.requests = []

        def handler(request):
            self.requests.append(request)
            return httpx2.Response(200, json={
                "id": "chatcmpl-1",
                "object": "chat.completion",
                "created": 0,
                "model": "test",
                "choices": [{
                    "index": 0,
                    "finish_reason": finish_reason,
                    "message": {"role": "assistant", "content": next(replies), "refusal": refusal},
                }],
            })

        http_client = openai.DefaultHttpxClient(transport=httpx2.MockTransport(handler))
        client = openai.OpenAI(api_key="test", base_url="https://test.invalid/v1", http_client=http_client)
        read = mcq_agent.read_screen(client, mcq_agent.PROVIDERS[provider], Image.new("RGB", (640, 360)))
        return read, expected

    def body(self):
        return json.loads(self.requests[0].content)

    def image_url(self):
        return self.body()["messages"][1]["content"][0]["image_url"]

    def test_response_is_parsed_into_the_schema(self):
        read, expected = self.call()
        self.assertEqual(read, expected)

    def test_image_is_sent_as_a_data_url(self):
        self.call()
        self.assertTrue(self.image_url()["url"].startswith("data:image/jpeg;base64,"))

    def test_grok_request_uses_its_model_schema_and_detail(self):
        self.call("grok")
        self.assertEqual(self.body()["model"], "grok-4.7")
        self.assertEqual(self.body()["response_format"]["type"], "json_schema")
        self.assertTrue(self.body()["response_format"]["json_schema"]["strict"])
        self.assertEqual(self.image_url()["detail"], "high")

    def test_groq_request_uses_json_mode_and_no_detail(self):
        self.call("groq")
        self.assertEqual(self.body()["model"], "qwen/qwen3.8-27b")
        self.assertEqual(self.body()["response_format"], {"type": "json_object"})
        self.assertNotIn("detail", self.image_url())

    def test_local_request_uses_schema_and_no_detail(self):
        self.call("local")
        self.assertEqual(self.body()["model"], "gemma3:4b")
        self.assertEqual(self.body()["response_format"]["type"], "json_schema")
        self.assertNotIn("detail", self.image_url())

    def test_prompt_carries_the_schema_for_providers_that_do_not_enforce_it(self):
        self.call("groq")
        self.assertIn('"navigation"', self.body()["messages"][0]["content"])

    def test_bad_json_is_retried_once(self):
        good = screen().model_dump_json()
        read, _ = self.call(replies=["not json", good])
        self.assertEqual(read, screen())
        self.assertEqual(len(self.requests), 2)

    def test_bad_json_on_every_try_stops_the_agent(self):
        with self.assertRaises(AgentStop):
            self.call(replies=["not json"] * mcq_agent.MAX_READ_TRIES)

    def test_json_of_the_wrong_shape_counts_as_bad(self):
        with self.assertRaises(AgentStop):
            self.call(replies=['{"answer": "B"}'] * mcq_agent.MAX_READ_TRIES)

    def reply_with_answers(self, answers):
        reply = json.loads(screen(question()).model_dump_json())
        reply["questions"][0]["answers"] = answers
        return json.dumps(reply)

    def test_empty_answers_are_read_again(self):
        good = screen(question()).model_dump_json()
        read, _ = self.call(replies=[self.reply_with_answers([]), good])
        self.assertEqual(read, screen(question()))
        self.assertEqual(len(self.requests), 2)

    def test_answer_that_is_not_an_option_is_read_again(self):
        good = screen(question()).model_dump_json()
        read, _ = self.call(replies=[self.reply_with_answers(["All of the above"]), good])
        self.assertEqual(read, screen(question()))

    def test_empty_answers_on_every_try_stop_the_agent(self):
        with self.assertRaises(AgentStop):
            self.call(replies=[self.reply_with_answers([])] * mcq_agent.MAX_READ_TRIES)

    def test_cut_off_question_may_have_no_answer_yet(self):
        read, _ = self.call(replies=[screen(question(answers=[], cut_off=True)).model_dump_json()])
        self.assertTrue(read.questions[0].cut_off)
        self.assertEqual(len(self.requests), 1)

    def test_stop_message_names_the_missing_field(self):
        reply = json.loads(screen().model_dump_json())
        del reply["navigation"]["remaining"]
        with self.assertRaisesRegex(AgentStop, "navigation.remaining"):
            self.call(replies=[json.dumps(reply)] * mcq_agent.MAX_READ_TRIES)

    def test_screen_with_no_questions_is_a_good_read(self):
        read, _ = self.call(replies=[screen().model_dump_json()])
        self.assertEqual(read, screen())

    def test_refusal_stops_the_agent(self):
        with self.assertRaises(AgentStop):
            self.call(refusal="no")

    def test_running_out_of_tokens_stops_the_agent(self):
        with self.assertRaises(AgentStop):
            self.call(finish_reason="length")


if __name__ == "__main__":
    unittest.main()
