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

## Setup

```powershell
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

Then set up your provider. Open a new terminal afterwards so `setx` takes effect.

```powershell
# grok
setx XAI_API_KEY "your-key"

# groq
setx GROQ_API_KEY "your-key"

# gemini
setx GEMINI_API_KEY "your-key"

# deepseek
setx DEEPSEEK_API_KEY "your-key"

# local: install Ollama first, then download the model (3.4 GB)
ollama pull gemma3:4b
```

## Quickest way: run.bat

`run.bat` uses Gemini with the fast `gemini-3.5-flash-lite` model. Open the quiz, run `run.bat` (or double-click it), switch to the quiz within 10 seconds and leave the mouse alone. The mouse moves to each correct option, clicks it and moves on. To stop it, move the mouse to a screen corner.

- `run.bat --dry-run` points the mouse at the answer without clicking and prints what it would click next, such as `Navigation: submit (Submit answer)`. Use it first on a site you haven't tried before.
- Other options pass through, for example `run.bat --model gemini-3.8-flash` for harder questions. That model is much slower on the free tier.
- `run.bat --effort low` makes Gemini think less, which is faster and cheaper (`none`, `low`, `medium` or `high`). Look at the thinking tokens it prints first: if they are already 0, this changes nothing. Check the right-answer count on a known quiz before relying on it.

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
3. If a question is cut off, scroll so that its first line is near the top of the page and read again. Otherwise click the correct option, then take a new screenshot to confirm it registered.
4. Submit the answer if the question has its own Submit button, then move on with Next or by scrolling, and repeat.

## When it stops

- **Last question:** it stops before the button that ends the whole quiz. It only clicks a Submit that records one answer: the button's own text has to say so (Submit answer, Check, Submit & Next and the like) or the model has to report that it records only the question in view. A button whose text mentions the quiz, test, exam, finish, end, results, score or similar words, in English and a few other languages, is never clicked, and neither is Previous or Back. On quizzes with a Submit button for each question, it also leaves the last one to you. This depends on the model reading the page right, so run `run.bat --dry-run` on a new site first.
- **A click doesn't register:** it stops after 2 tries on the same question.
- **A question doesn't fit on the screen:** after two scrolls it asks you to zoom the browser out (Ctrl and minus) and run again.
- **The screen stops changing:** this covers a Next button that does nothing, or no quiz on screen.
- **You abort:** move the mouse to any corner of the screen.

## Good to know

- With every provider except `local`, each screenshot of your whole main screen is sent to that company, so close anything private first.
- Keep the quiz visible and don't touch the mouse while it runs. Moving it during a click shifts where the click lands.
- It only reads your main monitor.
- Answers can be wrong, especially on image-heavy or very specialized questions.
- Each question uses at least two model calls. Every call prints its time and token counts, with the thinking tokens when the provider reports them.

## Tests

```powershell
.venv\Scripts\python -m unittest test_mcq_agent
```
