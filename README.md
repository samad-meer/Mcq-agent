# MCQ Agent

Reads multiple-choice questions from your screen, works out the answers with an AI model, clicks them, and moves to the next question. It works on any quiz you can see, because it reads the screen instead of the page code.

## Choose a model

| `--provider` | Who runs it | Default model | Cost | You need |
|---|---|---|---|---|
| `grok` (default) | xAI | `grok-4.7` | Paid: $2 per million tokens in, $6 out | Key from https://console.x.ai |
| `groq` | Groq, hosting an open model | `qwen/qwen3.8-27b` | Has a free plan with tight limits | Key from https://console.groq.com/keys |
| `local` | Your own computer, through Ollama | `gemma3:4b` | Free | Ollama from https://ollama.com/download |
| `gemini` | Google | `gemini-3.8-flash` | Free tier with daily limits; `--model gemini-3.5-flash-lite` is much faster | Key from https://aistudio.google.com/apikey |
| `deepseek` | DeepSeek | `deepseek-flash` | Paid: about $0.30 per million tokens in, $1.20 out | Key from https://platform.deepseek.com/api_keys |

Grok and Groq are different companies, despite the similar names.

`local` is the only option that keeps your screen on your computer, but it is slow without a dedicated graphics card. On a laptop with integrated graphics, expect each screenshot to take a long time, and expect small models to be weaker at reading small text and finding click positions.

Use `--model` to pick any other vision model from the same provider:

```powershell
.venv\Scripts\python mcq_agent.py --provider local --model qwen2.5vl
```

## Set up on a new PC: setup.bat

Works on a Windows 10 or 11 PC with nothing installed, without admin rights. With the internet connected:

1. Get the folder onto the PC: on GitHub choose Code, then Download ZIP; right-click the ZIP, choose Extract All, and put the extracted folder somewhere short, such as the Desktop or `C:\mcq-agent` (very deep folders break the install). If you copy the folder from another PC instead, leave its `.venv` folder behind; `setup.bat` makes a new one.
2. Open the extracted folder (not the ZIP window) and double-click `setup.bat`. If Windows asks whether you want to run it, choose Run. If the PC has no Python 3.13, it downloads it from python.org and installs it for your user account. Then it installs the exact package versions in `requirements.txt`. Allow a few minutes.
3. When it asks, paste a Gemini API key. Each person needs their own free key from https://aistudio.google.com/apikey, because the free daily limit belongs to the key's project. Use the Copy button next to the key, so no spaces come along. The key is saved in the `.env` file in this folder.
4. Open your quiz and double-click `run.bat`, as described below. To change the key later, edit `.env` or run `setup.bat` again: it offers to replace the saved one.

The quiz has to be on your main monitor: that is the only screen the agent reads, and only that screen's corners stop it.

## Where the keys go: .env

The API keys live in a file named `.env` in this folder, one line per provider. `setup.bat` writes the Gemini key there; for anything else, copy `.env.example` to `.env` and fill in the lines you use:

```
GEMINI_API_KEY=your-key
DEEPSEEK_API_KEY=
XAI_API_KEY=
GROQ_API_KEY=
```

The file wins over a key set as a Windows environment variable (`setx`), which still works when the file has no line for that provider. Git ignores `.env`, but a copy of the folder carries it, so never share the folder with it inside.

## Setup by hand

```powershell
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

Then put your provider's key in `.env` as above. For `local`, install Ollama first, then download the model (3.4 GB):

```powershell
ollama pull gemma3:4b
```

## Quickest way: run.bat

`run.bat` uses Gemini with the fast `gemini-3.5-flash-lite` model. Open the quiz, double-click `run.bat` (in a PowerShell window type `.\run.bat`), switch to the quiz within 10 seconds and leave the mouse alone. The mouse moves to each correct option, clicks it and moves on. To stop it, move the mouse to a corner of the main monitor.

- `run.bat --dry-run` points the mouse at the answer without clicking and prints what it would click next, such as `Navigation: submit (Submit answer)`. Use it first on a site you haven't tried before.
- Other options pass through, for example `run.bat --model gemini-3.8-flash` for harder questions. That model is much slower on the free tier.
- `run.bat --effort low` makes Gemini think less, which is faster and cheaper (`none`, `low`, `medium` or `high`). Look at the thinking tokens it prints first: if they are already 0, this changes nothing. Check the right-answer count on a known quiz before relying on it.
- `run.bat --debug` saves every screenshot it read, with red circles on the click targets, as `reads\read-001.jpg`, `read-002.jpg` and so on. When a run goes wrong, these show what the agent saw at each step.
- `run.bat --careful` reads the screen again after every answer before moving on, as earlier versions did. Slower, but the safest choice the first time on a new site.
- `run_fast.bat` (or `run.bat --fast`) is the quicker variant. After its first read it sends only the columns of the screen that hold the quiz, and it asks for a shorter reply: no reason, and question and option texts cut to their first words (a command stays whole). On the 14-screen test set it got the same 14 answers right as the normal mode, with reads about 0.5 s quicker (median 2.5 s instead of 2.9 s) and half the upload. Use the normal mode when you want the reason for each answer in `answers.md`.

### While it runs: keys

These work from any window, and the quiz page never receives them:

| Key | What it does |
|---|---|
| `Ctrl+Alt+P` | Pause. The agent finishes the click it is making, then waits. Press it again to go on; it reads the screen afresh first, so you can answer or scroll yourself meanwhile. |
| `Ctrl+Alt+S` | Skip the question in view. It is left unanswered and the agent moves on. |
| `Ctrl+Alt+Q` | Stop. |

A key takes effect within a few seconds, at the agent's next look at the screen or before it clicks Next. Moving the mouse into a screen corner still stops it at once. If another program already uses one of the keys, the agent says so when it starts.

### answers.md

Every question is written to `answers.md` in this folder as the run goes: the options, the one chosen, the reason, how long it took, and whether the click was confirmed on the screen, was left for you or was skipped. A line at the end of each run counts them. Each run is added below the last one, so you can look back over a quiz afterwards and find the questions to check by hand. `--no-log` turns it off.

### The documentation check

Before clicking an answer to an exact-syntax question, the agent looks up the commands in the chosen option. Git flags and commands are checked against Git's own manual, installed with Git (198 pages). `gh` commands are checked against `gh`'s help when `gh` is installed (`winget install GitHub.cli`). GitHub Actions expressions are checked against the list of context properties in GitHub's reference, such as `github.ref`, `runner.os` and `steps.<id>.outcome`. If the chosen option uses something that does not exist, such as `git push --force-safe`, `gh run rerun --only-failed` or `github.branch`, the agent asks the model once more, as text only, and tells it what the documentation says. The model then answers again, which also handles questions that ask which option is invalid. Nothing is sent when the chosen option checks out, which is almost always the case. `--no-doc-check` turns it off.

### A stronger model for scenario and code questions

The screen reader (Gemini) still reads the screen, finds the options and clicks. With an answer model, the text of each scenario or code question is also sent to a stronger model, which chooses the answer:

```powershell
run.bat --answer-provider openrouter
```

| `--answer-provider` | Default model | Key in `.env` | Notes |
|---|---|---|---|
| `deepseek` | `deepseek-flash` (DeepSeek V4.1 Flash) | `DEEPSEEK_API_KEY` | The best value found on 4 Nov 2026: $0.15 in / $0.60 out per million tokens off-peak, about 1–2 US cents a quiz. Peak hours (06:00–09:00 and 11:00–15:00 Pakistan time, weekdays) cost double. |
| `openrouter` | `z-ai/glm-5.3`, thinking set to low | `OPENROUTER_API_KEY` | One account for GLM-5.3, Kimi K3.1 Pro (`--answer-model moonshotai/kimi-k3.1-pro`), DeepSeek and others. Card, AliPay or USDC; 5.5% fee on credit. |
| `deepinfra` | `zai-org/GLM-5.3` | `DEEPINFRA_API_KEY` | GLM-5.3 at its lowest list price. |
| `together` | `reflection/Beam-1.0-501B-A23B` | `TOGETHER_API_KEY` | Beam; first purchase at least $15. |
| `huggingface` | `zai-org/GLM-5.3:cheapest` | `HF_TOKEN` | Picks the cheapest host; card only. |
| `zai` | `glm-5.3` | `ZAI_API_KEY` | GLM-5.3 direct; its card payments do not support 3-D Secure. |

Prices and payment details are from the providers' own pages on 4 November 2026 and change often.

`--answer-effort LEVEL` sets how much the answer model thinks, in its host's words (often `low`, `medium` or `high`). GLM-5.3, Kimi and Beam always think, and thinking tokens are billed as output, so a lower level is cheaper and quicker. During the countdown the agent asks the answer model one small test question, so a wrong model name, a setting the host refuses or an empty balance stops the run before the quiz, with the host's own message.

- A question goes to the answer model when its text is 20 words or longer (a scenario), or when the question or an option holds code or a command: brackets, `=`, `;`, HTML tags, `${{ }}`, or words such as `git`, `npm`, `docker`, `SELECT`, `def`, `function`. Short factual questions stay with the screen reader. `--answer-all` sends every question.
- Only the question and its options go, as text, and the answer model is not told what the screen reader chose, so its judgement is its own. One call per question, about 300 tokens in and 50 out.
- If the call fails, the screen reader's answer is clicked, so a dropped connection never stops the quiz. A key the service turns down stops the run at the start, before the countdown ends.
- `answers.md` notes which model answered and what the screen reader would have chosen, so you can compare them afterwards.
- `--answer-model` alone uses a model of the screen reader's provider, for example `run.bat --answer-model gemini-3.8-flash`.
- It cannot be combined with `--fast`, which cuts question texts short.

Put the answer provider's key in `.env` (see `.env.example` for the names), or save it with `.venv\Scripts\python mcq_agent.py --provider openrouter --save-key YOUR-KEY`.

## Try it on the demo quiz

Open `demo_quiz.html` in your browser, then run this and switch to the browser within 5 seconds. Add `--provider groq`, `--provider gemini` or `--provider local` if you aren't using Grok.

```powershell
.venv\Scripts\python mcq_agent.py --dry-run
```

This reads the screen once, prints the answers, and clicks nothing. The mouse then rests on each answer for a second, so you can see where it would click. It also saves `last_read.jpg` with red circles on those spots.

Then run it for real:

```powershell
.venv\Scripts\python mcq_agent.py
```

The demo quiz shows your score after you press Submit.

## How it works

1. Take a screenshot.
2. The model reads it and returns each question, the correct option, what is already selected, and where to click. A question whose options run below the bottom of the screen is reported as cut off.
3. Before clicking anything, take another screenshot and compare the part of it the model read (around the questions, options and button it placed) with the first one. If that part changed in the meantime (some quizzes move on by themselves), read it again instead of clicking a page that is no longer there. Changes elsewhere, such as a scrollbar fading at the edge, are ignored.
4. If a question is cut off, scroll so that its first line is near the top of the page and read again. Otherwise click the correct option and compare the pixels across the option's row before and after: if they changed (a radio filling, a card changing colour), the click registered, whatever the next read says about which option looks selected. A question the model reports as already selected on first sight is clicked anyway when it has one answer, because a hover highlight or a misread looks the same and clicking a chosen option again changes nothing.
5. If every click on the page registered and nothing else on the page changed, it moves on at once with the Next, Submit or scroll the model already found, so most questions need one model call. It reads the page again first when a click could not be confirmed, when the page reacted to the click (feedback appeared), when Next has no clear label, on the last question, or always with `--careful`.
6. Submit the answer if the question has its own Submit button, then move on with Next. After Next or Submit it waits for the page to actually change (up to 3 seconds) and then hold still before reading it, so a slow page is not mistaken for a Next button that did nothing. If a read then shows no question at all, it waits a moment and reads again before it would scroll, because a page that reloads is blank for a moment.

## When it stops

- **Last question:** it stops before the button that ends the whole quiz. It only clicks a Submit that records one answer: the button's own text has to say so (Submit answer, Check, Submit & Next and the like) or the model has to report that it records only the question in view. A button whose text mentions the quiz, test, exam, finish, end, results, score or similar words, in English and a few other languages, is never clicked, and neither is Previous or Back. On quizzes with a Submit button for each question, it also leaves the last one to you. This depends on the model reading the page right, so run `run.bat --dry-run` on a new site first.
- **A click doesn't register:** after 2 tries on the same question it prints `Could not select the answer to: ...`, leaves that question for you and moves on. It stops only when this happens on two questions in a row, which means clicks are not reaching the page at all (the quiz window is not in front, or something covers it).
- **A question doesn't fit on the screen:** it scrolls the question's first line to the top of the page area, measuring how far the page really moves rather than assuming, never more than two wheel notches at a time, and landing within half a notch of the target. If the first line is already at the top but the page had been scrolled down on this question, it scrolls back up first, because it has probably scrolled past the question's start. If the options are still cut off after two scrolls, or the page does not scroll at all, it asks you to zoom the browser out (Ctrl and minus) and run again. Every scroll prints a line such as `Scroll: asked 450 px, measured 300 px in 2 wheel event(s), 150 px per notch measured`; `the page did not move` on that line means the wheel is not scrolling this page.
- **The screen stops changing:** this covers a Next button that does nothing, or no quiz on screen.
- **You abort:** move the mouse to any corner of the screen, or press `Ctrl+Alt+Q`.

## Good to know

- With every provider except `local`, each screenshot of your whole main screen is sent to that company, so close anything private first. `--fast` sends only the quiz's columns after its first read, but that first read is the whole screen.
- `answers.md` holds the quiz's questions and your answers. Git ignores it, but a copy of the folder carries it along.
- Keep the quiz visible and don't touch the mouse while it runs. Moving it during a click shifts where the click lands.
- It only reads your main monitor.
- Answers can be wrong, especially on image-heavy or very specialized questions.
- Most questions use one model call; a second one is made when a click cannot be confirmed or the page needs another look (see "How it works"). Every call prints its time and token counts, with the thinking tokens when the provider reports them.

## Tests

```powershell
.venv\Scripts\python -m unittest test_mcq_agent test_doc_check
```
