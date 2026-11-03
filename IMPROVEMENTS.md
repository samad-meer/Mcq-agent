# Making the MCQ agent faster

Written 1 November 2026 and re-checked on 2 November 2026 against the code as it is now (83 tests, all passing). Links point at the current [mcq_agent.py](mcq_agent.py). Timings come from this laptop; the model time comes from an earlier test in this project, not from a new live call.

Short version: a question costs about **14 s** today: 7 s in two model calls, 4.4 s in mouse movement, 3 s in fixed sleeps. The plan takes it to about **8.5 s** with the hand-like mouse kept, or about **5 s** with a `--quick` mouse, and halves the bill either way. It also fixes the two problems from the ProProfs log that are still open (question 8 stopped the run, question 3 was skipped).

## Status

Done on 2 November 2026:

- The mouse rests away from the options after every click and before every read ([rest](mcq_agent.py#L274)). That is the hover fix from section 4.
- [run.bat](run.bat) does one countdown and clicks straight away; `run.bat --dry-run` points the mouse at the answer without clicking. The old two-run flow is gone, so change 6 is done.
- The mouse moves along a curved, eased path with a pause before and after each press ([glide](mcq_agent.py#L241), [click](mcq_agent.py#L304)). You asked for this because straight moves looked unreal. It costs about 2 s per click; see change 8.
- Per-question Submit buttons are clicked when they are safe ([submit_is_safe](mcq_agent.py#L450)); the Submit that ends the quiz never is.

Also done on 2 November 2026, as the first step of the order of work: the timing line on every model call, `--effort` (Gemini only) and the connection warm-up during the countdown (changes 2 and 7). Then the second step: `pyautogui.PAUSE = 0.02`, and the fixed sleeps cut to 0.3 s after an answer click and 1.0 s after Next, Submit or a scroll (the quick part of change 4). Section 1 below describes the loop before these two steps; take about 2 s per question off its figures.

Later on 2 November: scrolling measures how far the page really moved between two screenshots and corrects itself ([scroll_page](mcq_agent.py), [measure_shift](mcq_agent.py)), instead of assuming 100 px per notch. On this 150 % display a notch moves about 150 px, which is why the fit scroll overshot and the agent scrolled up and down. A cut-off question is scrolled once; if it still does not fit, the agent asks for a zoom-out. `FIT_STEP`, `MAX_FITS = 2` and `SCROLL_AMOUNT` are gone, and the settle wait after a scroll is now adaptive (two matching screenshots in a row), which is part of change 4.

Night of 2 November, after the W3Schools-style run (every scroll "measured 0 px", a skipped question, a run ended by "Clicks are not registering"):

- The local click check from change 1 is in: [run](mcq_agent.py) compares a 60×60 px patch around each click before and after it ([patch](mcq_agent.py), [differs](mcq_agent.py)); a click the pixels confirm is never repeated, whatever the next read says about `selected`. The second read per question is still made, so the time saving of change 1 is not taken yet.
- A question whose clicks never register is left for you after 2 tries ("Could not select the answer to: ..."); the run stops only after two such questions in a row (`MAX_FAILED`).
- Before acting on a read, the screen is captured again and compared with the one the model saw; a page that changed meanwhile is read again (`MAX_STALE = 2`), which is the "stale screen" risk from change 1 handled generally.
- After Next or Submit the agent waits for the page to really change, up to 3 s, then for it to hold still ([wait_for_change](mcq_agent.py)); this is the adaptive wait after Next from change 4. The wait after answer clicks is still the fixed 0.3 s plus the pixel check.
- A single-answer question the model reports as already selected on first sight is clicked anyway (hover highlight or misread look the same), which is the other half of the hover fix from section 4.
- Scrolling, after an adversarial review: never more than 2 notches per wheel event, stop short of the target instead of past it (`SCROLL_TOLERANCE = 1.0`), "did not move" only when the two screenshots are byte-identical, fixed headers and footers left out of the measurement, measurements scaled on downscaled captures, and a move that lines up equally well at two shifts counted as unclear.
- `--debug` saves every read as `reads\read-NNN.jpg` with the targets drawn, so a bad run can be examined afterwards.

3 November 2026: the one-read-per-question part of change 1 is in. Once every answer click on a page is confirmed on the pixels and nothing else on the page changed (`changed_elsewhere`, which ignores the clicked options' rows and the control's own box), the agent follows the Next, Submit or scroll from the same read (`reusable`): a Next needs a clear label and not the last page, a Submit the usual safety checks. `--careful` keeps the second read.

3 November, after the second real run. The good news: scrolling measured 148–150 px per notch, so the earlier "measured 0 px" was the agent looking before the page had moved (`settle` now keeps waiting while the screen still equals the one before the wheel). The run ended on a question read as cut off with its top already at the top, after a 600-px scroll on a page that was still blank after Next, and "The page changed while I was reading it" fired after most actions. Fixes: the stale check and the wait after Next compare only the area the read placed questions and controls in ([read_region](mcq_agent.py), [changed_in](mcq_agent.py)), so a scrollbar fading at the edge is not a page change; a page that has just changed must hold still for three screenshots (`STILL_AFTER_CHANGE`) before it counts as loaded; the first read with no question in view gets a `PAGE_SETTLE` pause instead of a scroll; a cut-off question whose first line is already at the top makes the agent scroll back by what it scrolled on this page (`page_scrolled`, once) before giving up; clicks are confirmed across the option's row by an absolute pixel count (`CLICK_PIXELS = 12`), so a radio beside the words the model pointed at counts; fits round to the nearest notch, with `FIT_TOP = 260` so half a notch too far still clears the browser's bars.

4 November: changes 3 and 5 are in, as a variant rather than the default: `--fast` (or `run_fast.bat`). It differs from the plan above in two places. Option texts are kept, cut to 8 words with a command left whole, because the documentation check below reads the flags in them. The region is found automatically instead of picked by hand: after a whole-width read, only the columns around what the read placed are sent (`quiz_view`), at full height, so scrolling and cut-off questions mean what they always did. Positions are moved back onto the whole screen straight after each read (`from_view`), and an empty read, or anything at a cut edge, sends the whole width again. Measured on the 14-screen fair set with gemini-3.5-flash-lite, one normal and one `--fast` read per screen: 14 of 14 answers right in both, median read 2.92 s → 2.46 s, upload 140 → 67 KB. Gemini counted the same input tokens for the cut picture (2,503 → 2,425, the difference being the shorter prompt) and nearly the same output tokens (345 → 331), so the gain comes from the upload and the shorter prompt, not from fewer image tokens. A one-line JSON reply halved the characters written but answered a three-answer question wrongly in 2 of 3 tries against 0 of 3 indented, so it was not kept.

Also on 4 November: `answers.md` (every question, the choice, the reason, the time and whether the click was confirmed), the documentation check ([doc_check.py](doc_check.py): Git's local manual, `gh`'s help when installed, GitHub Actions context properties; a finding against the chosen option asks the model once more, text only), and keyboard control (`Ctrl+Alt+P` pause and go on, `Ctrl+Alt+S` skip, `Ctrl+Alt+Q` stop, as Windows hot keys). The `gh` part is tested against recorded help text only: `gh` is not installed on this PC.

Still to do: change 8 and the adaptive wait after answer clicks (still the fixed 0.3 s plus the pixel check).

## 1. Where the time goes now

Per question on a one-question-per-page quiz, [run()](mcq_agent.py#L532) does:

| Step | Code | Time |
|---|---|---|
| 1. Screenshot + model call: answer the question | [line 550](mcq_agent.py#L550) | ~3.5 s (3 s model + ~0.5 s upload) |
| 2. Glide to the option, pause, click, pause, glide away | [click()](mcq_agent.py#L304) | 2.2–2.5 s |
| 3. `sleep(WAIT_SECONDS)` | [line 564](mcq_agent.py#L564) | 1.5 s |
| 4. Screenshot + model call: check the click, find Next | [line 550](mcq_agent.py#L550) | ~3.5 s |
| 5. Glide to Next, pause, click, pause, glide away | [line 609](mcq_agent.py#L609) | 2.0–2.2 s |
| 6. `sleep(WAIT_SECONDS)` | [line 612](mcq_agent.py#L612) | 1.5 s |

That is about **14 s per question**. Once per run there is also the countdown (10 s in run.bat) and [rest_and_settle](mcq_agent.py#L298) before the first read (~2 s). A quiz with a Submit button on every question takes a third read and a third click per question, about 20 s.

The model figure (about 3 s per read for `gemini-3.5-flash-lite`) is from an earlier test on 14 generated screens. Nothing in this plan has been timed live; change 7 adds a timing line so the next run shows the real split.

Mouse movement, measured with the mouse calls mocked so the real mouse stayed still (pyautogui's 0.1 s pause after every real move and click is added back in):

| Mouse step | Time |
|---|---|
| glide 200 / 500 / 1000 / 1600 px | 0.3 / 0.4 / 0.5 / 0.7 s |
| click() on an option, from the resting spot at the right edge and back | 2.2–2.5 s |
| click() on Next, from the resting spot and back | 2.0–2.2 s |
| rest_and_settle() before the first read | 2.0–2.2 s |
| scroll_page() | 1.4–1.6 s |
| one real cursor update | 0.08 ms |

When the model returns a `blank` spot near the question, the trips are shorter and a click is about 1.7 s. The right edge is the fallback.

Screenshot and JPEG work is negligible (1920×1080, best of 5):

| Step | Time | Size |
|---|---|---|
| Screenshot (`sct.grab`) | 26 ms | |
| Convert to a PIL image | 4 ms | |
| JPEG q90, no subsampling (current, [line 330](mcq_agent.py#L330)) | 10 ms | 382 KB file, **509 KB as base64** |
| JPEG q85, default subsampling | 6 ms | 271 KB file, 361 KB base64 |
| Resize to 1280×720, then JPEG | 39 ms | 207 KB file |
| Crop to the middle 60 % of the width, then JPEG | 6 ms | 232 KB file |
| Compare a 60×60 pixel patch (the local click check below) | 0.6 ms | |

What the model time is made of:

- **Upload**: 509 KB per read. At 5 Mbps up that is about 0.8 s; at 20 Mbps about 0.2 s.
- **Thinking**: the code sends no `reasoning_effort`, so Gemini picks its own amount. The research report found thinking tokens set the bill; they also set the wait.
- **Writing the reply**: models write maybe 100–300 tokens per second, and each reply repeats the question, every option's full text, a reason and now six navigation fields, about 250–350 tokens. That is 1–3 s per read on its own.

Formula: **time per question ≈ 2 × (upload + thinking + reply) + 2 clicks (~4.4 s) + 3 s of sleeps.**

## 2. Changes, biggest win first

### Change 1: one model call per question instead of two

The second read exists only to check that the click worked and to find Next. Both can be done without the model:

- **Check the click locally.** Grab a 60×60 pixel patch around the click point before the click and again after it. If the pixels changed, the radio button or checkbox reacted. Under 1 ms. `mss` never captures the cursor, and `click()` already moves the mouse away, so by the time the second patch is taken the hover highlight is gone and no extra wait is needed.
- **Reuse Next from the first read.** `navigation.position` is already in the first read. Click it right after the verified answer click.
- **Only read again when needed:** the patch did not change (click missed), the whole screen changed after the answer click (the quiz moved on by itself, so the stored Next position is stale), the first read had no Next position (Next appears only after answering, as in the demo quiz), or the control is a per-question Submit (feedback and Next have to be read after it).

```python
def click_and_verify(sct, monitor, point, blank=None):
    x, y = to_screen(point, monitor)
    before = patch(sct, x, y)          # sct.grab of a 60x60 box around x, y
    click(point, monitor, blank)       # glides there, clicks, and rests away, as today
    return patch(sct, x, y) != before
```

Rules that keep it as careful as today:

- Never click Next unless every answer click on that screen was verified.
- Compare a 96×54 downscale of the whole screen before and after the answer click. If more than about 20 % of it changed, the page moved on: do not use the stored Next, take a fresh read.
- `finish` and the Submit safety checks stay exactly as they are.

Result: one read (~3.5 s) and one 1.5 s sleep gone, about 5 s per question, and half the bill.

### Change 2: less thinking, with `--effort`

Add a flag and send it only to providers that accept it:

```python
# in PROVIDERS
"gemini": {..., "effort": True},

# in read_screen
extra = {"reasoning_effort": effort} if provider.get("effort") and effort else {}
response = client.chat.completions.create(..., **extra)
```

Values are `low`, `medium` and `high`. Gemini's docs also list `none` for models that can switch thinking off; try it on flash-lite, and the API returns a 400 if the model does not allow it. Start with `low`. If the timing line (change 7) shows thousands of thinking tokens per read today, this alone saves seconds per question. Hard questions may lose some accuracy at `low`, so compare right answers on one known quiz before settling.

### Change 3: a smaller reply

The model has to write back every option's full text (question 2 in your log had four options of 15–25 words each), and output tokens are the slow part. Only labels and positions are needed to click. Change the schema at [lines 70–83](mcq_agent.py#L70-L83):

- `Option`: keep `label` and `position`, drop `text`. The question key ([question_key](mcq_agent.py#L369)) uses option texts to tell same-worded questions apart, so replace that with the question text plus the option labels and positions, or keep a short `text` of the first three words.
- `Question`: add `number` (the "8." the quiz shows) and `answer_text` (the words of the chosen option, so the printout and the answers file still show what was picked). Ask for `text` as the first 12 words only.
- Keep `reason` as one sentence. Add `--quiet` to drop it when you do not need the explanation.

Expected: roughly half the output tokens, so about 0.5–1 s less per read, and cheaper.

### Change 4: wait for the screen to settle instead of sleeping 1.5 s

`WAIT_SECONDS` ([line 34](mcq_agent.py#L34)) runs after the answer clicks ([line 564](mcq_agent.py#L564)) and after Next ([line 612](mcq_agent.py#L612)). But `click()` already spends about 0.9 s gliding away after the press, so a radio button has long reacted, and a page swap usually settles within 0.3–1 s. Replace both sleeps with:

```python
def wait_until_still(sct, monitor, timeout=2.0, interval=0.15):
    last = thumbnail(capture(sct, monitor))   # 96x54 grayscale, compared as bytes
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        time.sleep(interval)
        now = thumbnail(capture(sct, monitor))
        if now == last:
            return True
        last = now
    return False
```

Quick interim version, one line each: 0.3 s after an answer click and 1.0 s after Next. A read taken on a half-loaded page wastes a whole model call, so do not go lower than that without the adaptive wait.

Also set `pyautogui.PAUSE = 0.02` at startup. The default 0.1 s now runs three times per click (two real moves and the click), 0.6 s per question of pure waiting.

Saves about 2.5–3 s per question.

### Change 5: send less picture

- **JPEG q85 with default subsampling** ([line 330](mcq_agent.py#L330)): 509 KB → 361 KB per upload, with no visible loss on screen text. One line.
- **`--region`**: send only the quiz part of the screen. Pick it once, by holding the mouse at the quiz's top-left and then bottom-right during the countdown, or pass `--region left,top,width,height`. `to_screen` then adds the region's offset to every click, and `rest` keeps its spot inside the region. This gives four things at once:
  - a smaller upload (the middle 60 % of your screen was 232 KB);
  - the model sees the radio buttons and text larger, which helps it read what is selected and where to click;
  - your other windows, the browser bar and the ads are never sent;
  - clicks can never land outside the region. In [last_read.jpg](last_read.jpg) from the ProProfs run a sticky "DOWNLOAD" ad sat over the bottom of the question, and a click on it would open the advertiser's site.
- **Do not downscale to 1280 just to save upload.** It makes the text smaller for the model and that is where misreads start. Measure right answers first if you want to try it.

### Change 6: one countdown, no throw-away call

Done. [run.bat](run.bat) runs the agent once, and `--dry-run` is a separate check that points at the answer. Nothing left here.

### Change 7: small things

- Print one timing line per read, for example `read 3: 4.8 s, tokens in 1900 / out 240 / thinking 1100`. Use `response.usage`; Gemini fills `completion_tokens_details.reasoning_tokens` when thinking is on. This line tells you which of the changes above matters on your connection.
- Warm up the HTTPS connection during the countdown with `client.models.retrieve(provider["model"])`, so the first read does not pay the handshake (about 0.3–1 s, once per run). It also catches a wrong key or model name before the countdown ends.
- `--delay 10` in [run.bat](run.bat#L15) can go back to the default 5 once you are used to switching windows.
- Nothing here can run in parallel. Each step needs the screen that the previous step produced, so the plan is to make every step cheaper, not to overlap them.

### Change 8: the hand-like mouse costs about 4.4 s per question

After change 1 the mouse is the largest cost after the model call: two clicks at 2.0–2.5 s each. That time is the look you asked for (curved path, pause before the press, a dwell after it, the glide to a resting spot), so the plan keeps it as the default and offers two ways to spend less on it:

- **Shorter trips.** Most of a click is travel: ~0.7 s out to the option and ~0.9 s back to the right edge. When the model returns a `blank` spot near the question the agent already rests there and a click drops to about 1.7 s. Ask for `blank` more firmly in the prompt ("always give one when any empty background is visible") and that becomes the normal case. Saves about 1 s per question with the same curves and pauses.
- **`--quick`.** Straight 0.15 s moves and no press or dwell pauses, still moving away before every read. A click drops to about 0.5 s. Saves about 3.5 s per question, but the movement looks like a machine again. Your choice per run.

### Risks in these changes, and the solutions

Checked on 2 November 2026 against the ProProfs page in [last_read.jpg](last_read.jpg) (video ad, sticky banner, clock in the taskbar) and the current code.

**Change 1, the local click check**

In plain words first: today the agent reads the screen twice per question, once to answer and once more to see that the click took and where Next is. Change 1 drops the second read. The agent checks the click by comparing pixels, and clicks Next where the first read saw it. The points below are the ways that can go wrong.

1. *Next can move after the answer click.* On most quizzes Next stays where it is when you pick an option. On some, picking an option makes a "Correct" or "Wrong" box or an explanation appear under the options, and Next is pushed lower. Clicking where Next *was* then hits text (nothing happens) or, worse, a different button. **Solution:** after the answer click the agent compares the screen before and after. If the only change is the option itself (the dot filled), and perhaps Next changing colour because it became enabled, it is safe to click Next where it was. If anything else changed (a box appeared, things moved), take a fresh read, as today. The 0.5 % in the rule is just the line between "one small thing changed" and "look again". Next is also reused only when its label clearly said Next, Continue or an arrow, and the page is not the last question, where a "Next" is often really a Submit; those cases get a fresh read.
2. *The check proves the click took, not that the right option is selected.* A position off by one row selects the wrong option and passes. Today's confirm read could catch that, although the log shows it is not reliable either. **Solution: `--careful`** keeps today's confirm read. Use it the first time on a new site, after `--dry-run` shows the circles on the right options; the default is fast. `--debug` keeps the pictures, so a wrong click can be found afterwards.
3. *Checkbox questions.* Two kinds of option exist. Radio buttons take one answer only; true/false questions are these too. Clicking another option moves the dot, and clicking the same option again changes nothing, so an extra click is harmless. Checkboxes ("select all that apply") toggle: every click turns the box on or off. The agent knows a question is this kind when the model lists more than one answer. The risk: the agent ticks a box, the pixel check wrongly says "nothing changed" (the tick appeared somewhere it did not look), the agent clicks again, and the box is unticked, a right answer removed. **Solution:** on a checkbox question a "nothing changed" result never leads to a second click; the agent takes a fresh read and lets the model say what is ticked, as today. True/false and every other single-answer question take the fast path.
4. *A radio's patch is not always where the change is.* A card that shows its selection by a border or a tick at its far end does not change within 60 px of the radio. **Solution:** compare a band the height of the option, 60 px tall and 800 px wide around the point. Same cost.
5. *The check fails for good reasons too:* a click on an overlay changes nothing where it matters. Then the second point and the fresh read take over. That is the design: the local check is an accelerator, not the judge; when in doubt it falls back to what the agent does today.
6. *Moving pictures.* Ads, a video or a blinking caret change pixels on their own and could trigger "look again" every time. Your real quiz site has no ads (only the test site did), so nothing is done about this now. If a site ever animates, the fix is a noise mask: two screenshots 200 ms apart before acting, and the pixels that differ between them are ignored afterwards.

**Change 2, `--effort`**

- *Thinking may already be off on flash-lite*, in which case the flag saves nothing and `none` returns a 400. **Solution:** add the flag only after the timing line shows reasoning tokens above zero, and turn a 400 into "this model does not accept effort X" instead of a stop with a raw error.
- *Other providers reject the field.* Grok 4.7 and DeepSeek do not document it for these models. **Solution:** the per-provider `effort` flag, off unless the provider's docs show it.

**Change 3, the smaller reply**

- *Cutting the question to 12 words makes keys unstable.* Two reads can cut at different places, so a question looks new on the second read and a submitted question loses the protection of `submitted` and might be clicked again. **Solution:** keep the full question text (it is short compared with the options) and shorten only the options, to their first four words. [question_key](mcq_agent.py#L369) and [same_question](mcq_agent.py#L382) then work unchanged.
- *`strict: True` needs every field.* `number` is a string, `""` when the quiz shows none; `answer_text` keeps the chosen option's words for the printout and the answers file.

**Change 4, the settle wait**

- *A page that animates never looks still.* Not an issue on your site. Keep a floor of 0.3 s and a cap equal to today's 1.5 s anyway, so the wait can never be slower than now.
- *A loading placeholder looks still for a moment*, and a read on a half-loaded page wastes a 3 s model call. **Solution:** after Next, first wait for the screen to differ from the pre-click thumbnail, then for it to be still ("changed, then still"), within the same cap.

**Change 5, less picture** (optional for you: `--region` is for privacy and larger text, not for ads)

- *`rest()` assumes the box is the whole screen.* [capture](mcq_agent.py#L218) and [to_screen](mcq_agent.py#L227) already take a box, so a region is just another `{left, top, width, height}`, but [rest](mcq_agent.py#L274) parks the mouse by the right edge of the box, which inside a quiz column may be an option. **Solution:** rest at `blank` when the model gives one, else just outside the region's right edge when there is room, else in the region's top strip. The abort corners stay the real screen's.
- *Picking the region by hand is fiddly.* **Solution: `--pick-region`.** It says "put the mouse on the top-left of the quiz", waits 3 s, reads `pyautogui.position()`, repeats for the bottom-right, and prints the `--region left,top,width,height` line to reuse. Do not try to find the browser window automatically: a maximised browser is the whole screen, and the ads are inside the page.
- *Chroma subsampling can smear small coloured text.* If red or blue text looks blurred in `last_read.jpg`, keep `subsampling=0` and only drop the quality to 85, still about 20 % smaller.

**Change 7, small things**

- `usage.completion_tokens_details` is missing on some providers: read it with `getattr(..., None)`.
- `client.models.retrieve` may be unsupported (404) on a provider: wrap the warm-up in try/except and ignore a failure, it is only a warm-up.

**Change 8, the mouse**

- `--quick` must still move the mouse away before every read, or the hover problem returns: keep `rest()`, with a straight move.
- The `blank` spot is the model's guess. A wrong one only parks the mouse on something, with no click, so it is safe to lean on.

**Section 4, never skipping an unclicked radio question**

- Costs about 2 s per already-answered question when a quiz is resumed. Accept it, or add `--trust-selected` to get today's behaviour back.

**New, from your note: options cut off below the screen**

On your site some questions are taller than the visible page: the last options sit below the bottom edge and need a small scroll. Before this fix the prompt told the model to leave out any cut-off question, so the agent saw no question, scrolled a fixed 400 px and read again; by then the question's text could be off the top, and the agent wandered down the page or stopped.

**Done on 2 November 2026, in code.** Each question now carries `cut_off` and the position of its first line. A cut-off question is never answered or decided. The agent scrolls so that the first line lands near the top of the page area (`fit_scroll`, computed from that position at 100 px per wheel notch), reads again and answers. If the question is still cut off, it scrolls two more notches; after that it stops and asks for a browser zoom-out, because a question taller than the whole screen cannot be shown whole any other way. Complete questions on the same screen are answered before the scroll. No zooming is needed in the normal case. Check it with `--dry-run` on one tall question: the printout says "More options are below the screen edge".

## 3. Expected result

| | Model calls | Mouse | Sleeps and waits | Time per question |
|---|---|---|---|---|
| Today | 2, ~7 s | ~4.4 s | 3 s | ~14 s |
| After changes 1 and 4, hand-like mouse kept | 1, ~3.5 s | ~4.4 s | ~0.5 s | ~8.5 s |
| Same, with `--quick` (change 8) | 1, ~3.5 s | ~1 s | ~0.5 s | ~5 s |
| Plus changes 2 and 3 (`low` effort, smaller reply) | 1, ~2.5 s (a guess) | ~1 s | ~0.5 s | ~4 s |

The model figures are from the earlier generated-screen test and a guess for the last row. The timing line gives the real numbers on your connection; the ratios should hold either way.

## 4. Fixes for what the log showed

**Question 8 stopped the run** with "Clicks are not registering". The model reported option C as not selected three reads in a row. Either the click missed (the ProProfs page had a sticky ad over its bottom, and the card's edge is not clickable), or the click worked and the model could not see the selected state. The second is likely: the research found no benchmark tests reading a selected state, and flash-lite is the weakest model in the list. Fix: change 1. The agent checks its own clicks by pixels and no longer trusts the model's `selected` for a question it clicked itself. On top of that:

- Before giving up on a question, try a second click point: the middle of the option's row, about 200 px right of the radio button.
- Do not stop the whole run on one bad question. Print "skipped question 8", move on, and stop only when two questions in a row fail. You fix the one by hand. This replaces the `AgentStop` at [line 428](mcq_agent.py#L428).

**Question 3 was skipped.** It never appeared between 2 and 4, so the model must have reported it as already `selected` and the agent believed it. The hover highlight that can cause this is handled now: the mouse rests away from the options before every read. The other cause, a plain misread, is not: for single-answer questions, never skip a question the agent has not clicked itself, because clicking a radio button twice is harmless. For checkbox questions keep the model's `selected` only on the first look, then rely on the agent's own verified clicks. That also removes the flaw the report found, where one misread could untick a right answer. Submitted questions stay untouched, as now.

**Ads.** Only the test site had them. If a site ever does, use an ad blocker or `--region`: an ad over the options hides them from the model, and a click near an ad can open it.

**Keep a record.** Append each question, the picked option, the reason and the time to `answers.md` as the run goes. You get study notes and a way to check the wrong ones later. It is a few lines next to [print_question](mcq_agent.py#L485).

**`--debug`.** Save every read as `reads/001.jpg` with the circles drawn plus `001.json`. Today `last_read.jpg` is only written by the dry run, so a failure in the real run cannot be looked at afterwards. It costs about 10 ms per read.

## 5. Tests and docs that change

[test_mcq_agent.py](test_mcq_agent.py) has 93 tests. `RunLoopTest.play` ([line 205](test_mcq_agent.py#L205)) fakes `capture` as `None` and patches `glide`, `sleep`, `click` and `scroll`. With changes 1 and 4 it must return images instead (for example 1001×1001 solid images whose patch changes after a click) and patch `wait_until_still`. The run-loop tests get new expectations because there are fewer reads, and the Submit tests need the extra read after a Submit kept.

New tests to add: a verified click leads straight to Next with no second read; an unverified click retries at the second point, then skips; a large screen change after a click leads to a fresh read, not the stale Next; `reasoning_effort` is sent only for providers that allow it; option `text` is gone from the schema and keys still tell same-worded questions apart; the region offset is applied in `to_screen` and `rest`; `--quick` makes straight moves with no pauses.

[README.md](README.md) says each question uses at least two model calls ([line 97](README.md#L97)) and that a new screenshot confirms the click ([line 80](README.md#L80)); both change with change 1.

## 6. Order of work

1. Done: the timing line, `--effort` and the warm-up (changes 7 and 2). The next real run shows where the time really goes.
2. Done: the interim sleeps and `pyautogui.PAUSE` (change 4's quick part).
3. Done: the `cut_off` flag and the computed scroll, so tall questions are read whole.
4. Done: change 1 with `--careful`, and the wait after Next and Submit is adaptive. Left from here: change 8's `--quick` and the firmer `blank` request.
5. Change 3 (shorter option texts only) and change 5's JPEG setting. `--region` only if you want privacy or larger text.
6. `answers.md` (`--debug` and skip instead of stop are done).

Then measure on `demo_quiz.html` and on one ProProfs quiz: seconds per question, model calls per question, right answers, and wrong or missed clicks. Keep `gemini-3.5-flash-lite` for speed. The research report's pick for accuracy is `gemini-3.8-flash`, but on the free tier an earlier test measured about 129 s per read and hit the daily limit after about 20 calls, so it needs a paid key before it is usable here. Everything above works with both.
