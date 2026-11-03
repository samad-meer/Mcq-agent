import os
import subprocess
import tempfile
import unittest
from unittest import mock

import doc_check
from mcq_agent import Option, Point, Question

PUSH = """<html><body><h2>OPTIONS</h2><dl>
<dt>--all</dt><dt>-u</dt><dt>--set-upstream</dt><dt>-f</dt><dt>--force</dt>
<dt>--force-with-lease[=&lt;refname&gt;]</dt><dt>--[no-]verify</dt><dt>-d</dt><dt>--delete</dt>
</dl></body></html>"""
COMMIT = "<dt>-a</dt><dt>--all</dt><dt>-m &lt;msg&gt;</dt><dt>--amend</dt><dt>--no-edit</dt><dt>-S[&lt;keyid&gt;]</dt>"
RERUN_HELP = """Rerun an entire run, only failed jobs, or a specific job from a run.

USAGE
  gh run rerun [<run-id>] [flags]

FLAGS
  -d, --debug        Rerun with debug logging
      --failed       Rerun only failed jobs, including dependencies
  -j, --job string   Rerun a specific job ID from a run, including dependencies

INHERITED FLAGS
      --help                     Show help for command
  -R, --repo [HOST/]OWNER/REPO   Select another repository using the [HOST/]OWNER/REPO format
"""


class FlagsTest(unittest.TestCase):
    def test_flags_are_read_the_way_git_takes_them(self):
        self.assertEqual(doc_check.flags_in(["-am", "msg"]), ["-a", "-m"])
        self.assertEqual(doc_check.flags_in(["--format=%H", "-5", "-U3"]), ["--format", "-U"])
        self.assertEqual(doc_check.flags_in(["-mfixed"]), ["-m"])  # a value written straight after its flag
        self.assertEqual(doc_check.flags_in(["origin", "--", "--not-a-flag"]), [])

    def test_a_negated_option_counts_in_every_way_manuals_write_it(self):
        self.assertTrue(doc_check.documented("--[no-]verify", "--no-verify"))
        self.assertTrue(doc_check.documented("--[no-]verify", "--verify"))
        self.assertTrue(doc_check.documented("--no-edit", "--no-edit"))
        self.assertTrue(doc_check.documented("--edit", "--no-edit"))
        self.assertFalse(doc_check.documented("--force-with-lease", "--force-with"))
        self.assertTrue(doc_check.documented("--force-with-lease[=<refname>]", "--force-with-lease"))
        self.assertFalse(doc_check.documented("--force", "--force-safe"))


class GitTest(unittest.TestCase):
    """Against a small manual made here, so the tests do not depend on the Git installed."""

    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        for name, text in (("git-push.html", PUSH), ("git-commit.html", COMMIT)):
            with open(os.path.join(folder.name, name), "w", encoding="utf-8") as f:
                f.write(text)
        doc_check.git_page.cache_clear()
        self.addCleanup(doc_check.git_page.cache_clear)
        patcher = mock.patch.object(doc_check, "git_manual", return_value=folder.name)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_real_commands_pass(self):
        for text in ("git push --force-with-lease origin main", "git push -u origin main", "git commit -am 'x -z'",
                     "git push origin --delete old", "Run `git commit --amend --no-edit` now", "git push && git commit -a"):
            self.assertEqual(doc_check.check_option(text), [], text)

    def test_an_invented_flag_or_command_is_found(self):
        self.assertEqual(doc_check.check_option("git push --force-safe origin main"),
                         ["`--force-safe` is not an option of `git push` in Git's manual"])
        self.assertEqual(doc_check.check_option("git undo HEAD"), ["Git's manual has no `git undo` command"])

    def test_tools_outside_git_and_global_options_are_left_alone(self):
        self.assertEqual(doc_check.check_option("git lfs track '*.psd'"), [])
        self.assertEqual(doc_check.check_option("git -C repo push --nonsense"), [])

    def test_without_git_nothing_is_checked(self):
        with mock.patch.object(doc_check, "git_manual", return_value=None):
            self.assertEqual(doc_check.check_option("git undo --everything"), [])

    def test_findings_are_given_by_option_label(self):
        q = Question(text="Which command amends the last commit?", position=Point(x=1, y=1), options=[
            Option(label="A", text="git commit --undo", position=Point(x=1, y=2)),
            Option(label="B", text="git commit --amend", position=Point(x=1, y=3)),
        ], answers=["A"], selected=[], reason="", cut_off=False)
        self.assertEqual(doc_check.check(q), {"A": ["`--undo` is not an option of `git commit` in Git's manual"]})


class GhTest(unittest.TestCase):
    """gh's help is played back here: the format of `gh run rerun --help` and of an unknown command."""

    def setUp(self):
        doc_check.gh_help.cache_clear()
        self.addCleanup(doc_check.gh_help.cache_clear)

    def fake_gh(self, args, **_):
        words = tuple(args[1:-1])
        if words in (("run", "rerun"),):
            return subprocess.CompletedProcess(args, 0, RERUN_HELP, "")
        if words in (("run",), ("workflow",), ("pr",)):
            return subprocess.CompletedProcess(args, 0, f"Work with GitHub {words[0]}s.\n\nUSAGE\n  gh {words[0]} <command> [flags]\n", "")
        if len(words) == 2 and words[0] == "run":
            return subprocess.CompletedProcess(args, 1, "", f'unknown command "{words[1]}" for "gh run"\n')
        return subprocess.CompletedProcess(args, 1, "", f'unknown command "{words[-1]}" for "gh"\n')

    def check(self, text, installed=True):
        with (
            mock.patch.object(doc_check.shutil, "which", side_effect=lambda name: "gh" if installed and name == "gh" else None),
            mock.patch.object(doc_check.subprocess, "run", side_effect=self.fake_gh),
        ):
            return doc_check.check_gh(text)

    def test_the_fair_test_question_on_rerunning_failed_jobs(self):
        self.assertEqual(self.check("gh run rerun 12345 --failed"), [])
        self.assertEqual(self.check("gh run rerun 12345 --only-failed"),
                         ["`--only-failed` is not an option of `gh run rerun` in gh's help"])
        self.assertEqual(self.check("gh run retry 12345 --failed"), ["gh has no `gh run retry` command"])
        self.assertEqual(self.check("gh rerun 12345"), ["gh has no `gh rerun` command"])

    def test_inherited_flags_count(self):
        self.assertEqual(self.check("gh run rerun 1 -R owner/repo --debug"), [])

    def test_without_gh_nothing_is_checked(self):
        self.assertEqual(self.check("gh run retry --only-failed", installed=False), [])


class ActionsTest(unittest.TestCase):
    QUESTION = "Which condition runs a step only on main in a GitHub Actions workflow?"

    def test_properties_the_reference_does_not_list_are_found(self):
        self.assertEqual(doc_check.check_option("if: github.branch == 'main'", self.QUESTION),
                         ["`github.branch` is not a property of the `github` context"])
        self.assertEqual(doc_check.check_option("${{ runner.platform }}"),
                         ["`runner.platform` is not a property of the `runner` context"])
        self.assertEqual(doc_check.check_option("${{ steps.build.status }}"),
                         ["`steps.build.status` does not exist: `steps.<id>` has only conclusion, outcome, outputs"])
        self.assertEqual(doc_check.check_option("${{ workflow.name }}"), ["`workflow` is not a GitHub Actions context"])

    def test_real_expressions_pass(self):
        for text in ("if: github.ref == 'refs/heads/main'", "if: github.ref_name == 'main'", "${{ needs.test.result }}",
                     "${{ contains(github.event.head_commit.message, 'skip') }}", "${{ secrets.MY_TOKEN }}",
                     "${{ matrix.node-version }}", "${{ strategy.job-index }}", "${{ steps.build.outputs.path }}"):
            self.assertEqual(doc_check.check_option(text, self.QUESTION), [], text)

    def test_ordinary_text_is_not_read_as_an_expression(self):
        self.assertEqual(doc_check.check_option("See github.com/org/repo for runner.platform", "Which is true?"), [])
        self.assertEqual(doc_check.check_option("Clone https://github.com/org/repo", self.QUESTION), [])


if __name__ == "__main__":
    unittest.main()
