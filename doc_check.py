"""Check the options of an exact-syntax question against documentation, not the model's memory.

Models now and then pick a command whose flag does not exist. Git installs its whole manual
with it and gh prints its help as plain text, so a flag can be looked up on this PC for free.
GitHub Actions has no local manual, so the properties of its fixed contexts are listed below,
from GitHub's contexts reference
(https://docs.github.com/en/actions/reference/workflows-and-actions/contexts, read 4 November 2026).

A finding is evidence, not a verdict. The agent hands it back to the model, which also knows
when a question asks for the option that does not exist.
"""
import functools
import html
import os
import re
import shutil
import subprocess

GH_TIMEOUT = 10  # s for one `gh ... --help`

ACTIONS_CONTEXTS = {
    "github", "env", "vars", "job", "jobs", "steps", "runner", "secrets", "strategy", "matrix", "needs", "inputs",
}
# Contexts whose properties are fixed. The others (env, vars, secrets, matrix, inputs) hold names the workflow chooses.
FIXED_PROPERTIES = {
    "github": {
        "action", "action_path", "action_ref", "action_repository", "action_status", "actor", "actor_id", "api_url",
        "artifacts", "artifacts_list", "base_ref", "env", "event", "event_name", "event_path", "graphql_url",
        "head_ref", "job", "path", "ref", "ref_name", "ref_protected", "ref_type", "repository", "repository_id",
        "repository_owner", "repository_owner_id", "repositoryUrl", "retention_days", "run_id", "run_number",
        "run_attempt", "secret_source", "server_url", "sha", "token", "triggering_actor", "workflow", "workflow_ref",
        "workflow_sha", "workspace",
    },
    "runner": {"name", "os", "arch", "temp", "tool_cache", "debug", "environment"},
    "job": {
        "check_run_id", "container", "services", "status", "workflow_ref", "workflow_sha", "workflow_repository",
        "workflow_file_path",
    },
    "strategy": {"fail-fast", "job-index", "job-total", "max-parallel"},
}
# Contexts keyed by a name the workflow chooses, and what each named entry holds.
NAMED_PROPERTIES = {
    "steps": {"outputs", "conclusion", "outcome"},
    "needs": {"outputs", "result"},
    "jobs": {"outputs", "result"},
}
# Commands run through git that are separate programs, so Git's manual has no page for them.
GIT_EXTERNAL = {"lfs", "flow", "credential-manager", "secrets", "filter-repo", "absorb"}

QUOTED = re.compile(r"\"[^\"]*\"|'[^']*'")
GIT_COMMAND = re.compile(r"(?<![\w/.-])git\s+(.+?)(?=\s*(?:&&|\|\||[|;]|$))")
GH_COMMAND = re.compile(r"(?<![\w/.-])gh\s+(.+?)(?=\s*(?:&&|\|\||[|;]|$))")
WORD = re.compile(r"^[a-z][a-z0-9-]*$")
EXPRESSION = re.compile(r"\$\{\{(.*?)\}\}")
CONTEXT_PATH = re.compile(r"(?<![\w.$/@:-])([A-Za-z_][\w-]*)((?:\.[A-Za-z_*][\w-]*)+)(\s*\()?")
WEB_ENDINGS = {"com", "io", "dev", "net", "org", "blog"}


def flags_in(tokens):
    """The flags among a command's words, each short letter on its own: -am is -a and -m."""
    found = []
    for token in tokens:
        if token == "--":
            break  # paths and revisions follow
        if re.match(r"^--[A-Za-z0-9][\w-]*", token):
            found.append(token.split("=", 1)[0])
        elif re.match(r"^-[A-Za-z]", token):
            letters = re.match(r"^-([A-Za-z]+)", token).group(1)
            # A long run of letters is more likely a value written straight after its flag, as in -mfix.
            found.extend(f"-{letter}" for letter in (letters if len(letters) <= 3 else letters[0]))
    return list(dict.fromkeys(found))


def documented(text, flag):
    """Whether a manual mentions this flag, in any of the ways manuals write an option and its negation."""
    if flag.startswith("--"):
        name = flag[2:]
        names = {name, f"no-{name}"}
        if name.startswith("no-"):
            names.add(name[3:])
        pattern = r"(?<![\w-])--(?:\[no-\])?(?:%s)(?![\w-])" % "|".join(map(re.escape, sorted(names, key=len, reverse=True)))
    else:
        pattern = r"(?<![\w-])%s(?![\w-])" % re.escape(flag)
    return re.search(pattern, text) is not None


@functools.cache
def git_manual():
    """The folder of Git's HTML manual on this PC, or None when Git is not installed."""
    git = shutil.which("git")
    if not git:
        return None
    try:
        folder = subprocess.run([git, "--html-path"], capture_output=True, text=True, timeout=GH_TIMEOUT).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None
    return folder if folder and os.path.isdir(folder) else None


@functools.cache
def git_page(command):
    """The text of one command's manual page, or None when the manual has no such page."""
    folder = git_manual()
    path = os.path.join(folder, f"git-{command}.html") if folder else ""
    if not path or not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as f:
        return html.unescape(re.sub(r"<[^>]+>", " ", f.read()))


@functools.cache
def gh_help(words):
    """gh's help for a command as (found, text); found is None when gh is not installed."""
    gh = shutil.which("gh")
    if not gh:
        return None, ""
    try:
        done = subprocess.run([gh, *words, "--help"], capture_output=True, text=True, timeout=GH_TIMEOUT,
                              env={**os.environ, "GH_PROMPT_DISABLED": "1", "NO_COLOR": "1"})
    except (OSError, subprocess.SubprocessError):
        return None, ""
    text = done.stdout + done.stderr
    return done.returncode == 0 and "unknown command" not in text, text


def check_git(text):
    findings = []
    for match in GIT_COMMAND.finditer(text):
        tokens = match.group(1).split()
        if not tokens or not WORD.match(tokens[0]):
            continue  # a global option such as -C comes first; not checked
        command = tokens[0]
        if command in GIT_EXTERNAL or git_manual() is None:
            continue
        page = git_page(command)
        if page is None:
            findings.append(f"Git's manual has no `git {command}` command")
            continue
        for flag in flags_in(tokens[1:]):
            if not documented(page, flag):
                findings.append(f"`{flag}` is not an option of `git {command}` in Git's manual")
    return findings


def check_gh(text):
    findings = []
    for match in GH_COMMAND.finditer(text):
        tokens = match.group(1).split()
        words = []
        for token in tokens[:3]:
            if not WORD.match(token):
                break
            words.append(token)
        if not words:
            continue
        # The longest run of words gh knows as a command; a word after it is an argument.
        known, page = 0, ""
        for size in range(len(words), 0, -1):
            found, help_text = gh_help(tuple(words[:size]))
            if found is None:
                return findings  # gh is not installed: nothing to check against
            if found:
                known, page = size, help_text
                break
        if not known:
            findings.append(f"gh has no `gh {words[0]}` command")
            continue
        unknown = re.search(r'unknown command "([^"]+)" for "([^"]+)"', gh_help(tuple(words[:known + 1]))[1]) \
            if known < len(words) else None
        if unknown:
            findings.append(f"gh has no `{unknown.group(2)} {unknown.group(1)}` command")
            continue
        for flag in flags_in(tokens[known:]):
            if not documented(page, flag):
                findings.append(f"`{flag}` is not an option of `gh {' '.join(words[:known])}` in gh's help")
    return findings


def check_actions(text, question_text=""):
    """Properties of GitHub Actions contexts that the contexts reference does not list."""
    looks_like_actions = "${{" in text or re.match(r"^\s*if\s*:", text) or re.search(r"workflow|actions", question_text, re.I)
    if not looks_like_actions:
        return []
    findings = []
    spans = [(m.start(1), m.end(1)) for m in EXPRESSION.finditer(text)]
    for match in CONTEXT_PATH.finditer(text):
        root, path, call = match.group(1), match.group(2), match.group(3)
        parts = path.split(".")[1:]
        if call:
            continue  # a function call such as contains(...)
        if root in FIXED_PROPERTIES:
            if root == "github" and parts[0] in WEB_ENDINGS:
                continue  # github.com
            if parts[0] not in FIXED_PROPERTIES[root]:
                findings.append(f"`{root}.{parts[0]}` is not a property of the `{root}` context")
        elif root in NAMED_PROPERTIES:
            if len(parts) > 1 and parts[1] not in NAMED_PROPERTIES[root]:
                allowed = ", ".join(sorted(NAMED_PROPERTIES[root]))
                findings.append(f"`{root}.{parts[0]}.{parts[1]}` does not exist: `{root}.<id>` has only {allowed}")
        elif root not in ACTIONS_CONTEXTS and any(a <= match.start() < b for a, b in spans):
            findings.append(f"`{root}` is not a GitHub Actions context")
    return findings


def check_option(text, question_text=""):
    """What the documentation says against one option's text: a list of plain sentences, empty when nothing."""
    plain = QUOTED.sub("''", text.replace("`", ""))
    return list(dict.fromkeys(check_git(plain) + check_gh(plain) + check_actions(plain, question_text)))


def check(question):
    """Findings for each option of a question, by label; options with nothing found are left out."""
    found = {}
    for option in question.options:
        notes = check_option(option.text, question.text)
        if notes:
            found[option.label] = notes
    return found


def describe():
    """One line on what can be checked on this PC."""
    folder = git_manual()
    git = f"Git's manual ({len([n for n in os.listdir(folder) if n.startswith('git-') and n.endswith('.html')])} pages)" \
        if folder else "no Git manual (Git is not installed)"
    gh = "gh's help" if shutil.which("gh") else "no gh (install it with: winget install GitHub.cli)"
    return f"Doc check: {git}, {gh}, and the GitHub Actions contexts."
