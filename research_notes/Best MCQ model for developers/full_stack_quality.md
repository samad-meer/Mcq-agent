# How well current LLMs answer full stack web development questions (state as of 1 November 2026)

## Which benchmarks test all or most of these models on the same scale?

### Takeaway
Five sources put nearly all of these models on one scale: Artificial Analysis (AA) Intelligence Index v5.0 with Terminal-Bench 4.0 and FrontierCode 2.0, Vals Vibe Code Bench v1.1, Arena WebDev, AIM text-to-SQL, and Bug Hunt Bench. None of them is a multiple-choice test. Nearly all results come from first-party APIs at high or maximum effort, not from the Groq deployment or from low-latency settings.

### Cited Findings

#### Reading notes for every table in this file
- Scores in one table column share one benchmark version. Where a model was only tested on another version, the cell says so instead of showing the number in that column.
- Decimal AA values and all AA Coding Agent rows were parsed on 2026-11-01 from JSON embedded in the AA page HTML, because the visible page text rounds them or omits them. AA gives no per-model test dates; v5.0 runs from October 2026 — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).
- Build names used here: "0910" is the original DeepSeek V4.1 Flash, released 10 Sep 2026, which AA now marks deprecated with no v5.0 overall score — [AA](https://artificialanalysis.ai/models/deepseek-v4-1-flash). "1017" is the 17 Oct 2026 update — [Vals](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017).

#### What the requested model IDs actually map to
- `deepseek-flash` serves DeepSeek-V4.1-Flash-1017 with vision supported. `deepseek-v4-pro` serves DeepSeek-V4-Pro-0813 with vision not supported — [DeepSeek pricing docs](https://api-docs.deepseek.com/quick_start/pricing).
- Conflict on image input: Cursor says V4.1 Flash 1017 "does not take image inputs" — [Cursor](https://cursor.com/docs/models/deepseek-v4-1-flash-1017); contradicted by [DeepSeek's docs](https://api-docs.deepseek.com/quick_start/pricing), by the Image-Text-to-Text tag and vision benchmarks on the [model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017), and by AA's image-input flag — [AA](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-1017-vs-gemini-3-8-flash).
- Groq `qwen/qwen3.8-27b` is in Preview, takes up to 3 images per request, has a 131,072-token context and 16,384 max output tokens, and offers `reasoning_effort` low, medium, high or none — [Groq docs](https://console.groq.com/docs/model/qwen/qwen3.8-27b). The model's own default effort is xhigh — [Qwen model card](https://huggingface.co/Qwen/Qwen3.8-27B).
- AA's and Vals' Qwen3.8-27B results come from Alibaba's API, and Vals ran xhigh — [AA](https://artificialanalysis.ai/models/qwen3-8-27b); [Vals](https://www.vals.ai/models/alibaba_qwen3.8-27b).
- The latest general-purpose Flash-Lite is `gemini-3.5-flash-lite`; `gemini-3.1-flash-lite` is also stable. The only 3.8 Flash-Lite listed is a TTS model — [Google model list](https://ai.google.dev/gemini-api/docs/models).
- Release dates: Grok 4.7 on 21 Sep 2026 — [Vals](https://www.vals.ai/models/grok_grok-4.7); Gemini 3.8 Flash on 2 Sep 2026 — [Vals](https://www.vals.ai/models/google_gemini-3.8-flash); Qwen3.8-27B on 14 Aug 2026 — [Vals](https://www.vals.ai/models/alibaba_qwen3.8-27b); V4 Pro 0813 on 13 Aug 2026 — [Vals](https://www.vals.ai/models/deepseek_deepseek-v4-pro-0813); Gemini 3.5 Flash-Lite on 21 Jul 2026 — [Vals](https://www.vals.ai/models/google_gemini-3.5-flash-lite). Gemini 4 Argon is 30 Sep 2026 on [AA](https://artificialanalysis.ai/models/gemini-4-argon) but 13 Oct 2026 on [Vals](https://www.vals.ai/models/google_gemini-4-argon).

#### Coverage matrix
Y means a score exists for that model. N means none was found on that page. Sources for each row are in the sections below.

| Benchmark (version) | Grok 4.7 | Qwen3.8-27B | V4.1 Flash 1017 | V4.1 Flash 0910 | Gemini 3.8 Flash | Flash-Lite | Argon | V4 Pro |
|---|---|---|---|---|---|---|---|---|
| AA Intelligence Index v5.0 | Y | Y | Y | N | Y | 3.5 | Y | 0813 |
| AA Terminal-Bench 4.0 | Y | Y | Y | Y | Y | 3.5, 3.1 | Y | 0813 |
| AA FrontierCode 2.0 | Y | Y | Y | N | Y | 3.5 | Y | 0813 |
| AA SWE-Atlas-QnA-AA (Coding Agent Index v2.0) | Y | N | Y | Y | Y | N | Y | N |
| Scale SWE Atlas Codebase QnA | N | N | N | N | Y | N | N | build unstated |
| Vals Vibe Code Bench v1.1 | Y | Y | Y | Y | Y | 3.5 | Y | both builds |
| Vals Terminal-Bench 4.0 | Y | N | Y | Y | Y | N | Y | both builds |
| Vals SWE-bench Multimodal | Y | N | N | Y | Y | N | Y | N |
| Arena WebDev | Y | Y | Y | Y | Y | 3.5, 3.1 preview | Y | Y |
| Arena Text Coding | Y | Y | N | Y | Y | 3.5, 3.1 preview | Y | Y |
| AIM text-to-SQL | Y | Y | Y | Y | Y | 3.5, 3.1 | Y | both builds |
| Bug Hunt Bench | Y | Y | Y | Y | Y | N | Y | Y |
| Next.js Agent Evals | Y | N | N | N | Y | N | Y | N |
| DeepSWE v1.1 public board | N | N | N | N | Y | N | N | build unstated |

#### AA model-only results (Intelligence Index v5.0 components, independent)
- Terminal-Bench 4.0 uses 66 tasks, the mini-swe-agent harness, pass@1 averaged over 3 repeats, and a 500-step cap. FrontierCode 2.0 uses 132 tasks, 3 attempts, the Stirrup harness, and a 500-turn cap. The Coding category is 25% of the index (FrontierCode 2.0 at 15%, Terminal-Bench 4.0 at 10%) — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).
- Values below come from [AA Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [AA FrontierCode 2.0](https://artificialanalysis.ai/evaluations/frontiercode-2-0), [AA SciCode](https://artificialanalysis.ai/evaluations/scicode), and comparison pages for [Grok and Argon](https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-gemini-4-argon), [Qwen](https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-gemini-3-8-flash), [DeepSeek 1017](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-1017-vs-gemini-3-8-flash), [V4 Pro](https://artificialanalysis.ai/models/comparisons/deepseek-v4-pro-vs-gemini-3-8-flash), [Grok vs Flash Low](https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-gemini-3-8-flash-low) and [Flash-Lite](https://artificialanalysis.ai/models/comparisons/gemini-3-5-flash-lite-vs-gemini-3-8-flash).

| Model and effort | Index v5.0 | Terminal-Bench 4.0 % | FrontierCode 2.0 % | SciCode % (not in index) |
|---|---|---|---|---|
| Gemini 4 Argon (High) | 50.4 | 57.1 | 25.7 | 61.8 |
| Grok 4.7 (High) | 35.0 | 24.8 | 27.8 | 57.8 |
| Grok 4.7 (Xhigh) | 34.3 | 25.8 | 28.7 | 57.4 |
| Grok 4.7 (Low) | 30.9 | 16.2 | 21.8 | 54.9 |
| DeepSeek V4.1 Flash 1017 (Max) | 32.5 | 33.8 | 28.5 | 55.9 |
| DeepSeek V4.1 Flash 1017 (Non-reasoning) | 18.5 | 9.1 | 6.1 | 38.5 |
| DeepSeek V4.1 Flash 0910 (Max), deprecated | no score | 26.8 | no score | 51.9 |
| Gemini 3.8 Flash (High) | 30.5 | 19.7 | 18.7 | 56.6 |
| Gemini 3.8 Flash (Medium) | 30.0 | 19.7 | 16.5 | 55.1 |
| Gemini 3.8 Flash (Low) | 22.3 | 10.1 | 8.1 | 55.0 |
| DeepSeek V4 Pro 0813 (Max), reference only | 23.1 | 14.1 | 17.1 | 51.0 |
| Qwen3.8 27B (Xhigh) | 20.1 | 5.6 | 14.9 | 46.6 |
| Qwen3.8 27B (Medium) | 17.5 | 5.1 | 11.5 | 39.0 |
| Qwen3.8 27B (Low) | 15.7 | 2.5 | 12.4 | 40.1 |
| Qwen3.8 27B (Non-reasoning) | 10.0 | 0.0 | 3.7 | 36.2 |
| Gemini 3.5 Flash-Lite (effort unlabelled) | 11.7 | 1.0 | 6.0 | 41.3 |
| Gemini 3.1 Flash-Lite (effort unlabelled), deprecated at AA | no score | 0.5 | no score | 43.4 |

- For context, the top of Index v5.0 is Gemini 4 Carbon (High) at 59 and Claude Opus 5.5 (Max) at 58 — [AA models](https://artificialanalysis.ai/models).
- AA has no named "Coding Index" in v5.0. Coding is a category, not a separately published index — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking). OpenRouter shows a "Coding Index" of 76.3 for Gemini 3.8 Flash and "Not available" for Grok 4.7 with no source or version named — [OpenRouter](https://openrouter.ai/compare/google/gemini-3.8-flash/x-ai/grok-4.7).

#### AA Coding Agent Index v2.0 (model plus agent harness, independent)
- The index is the equal-weight average of FrontierCode v1.1, Terminal-Bench 4.0 and SWE-Atlas-QnA-AA, with three attempts per task. Each row is an agent variant, not a model — [AA coding agent methodology](https://artificialanalysis.ai/methodology/coding-agents-benchmarking).
- Page data was materialized on 2026-10-30. The target rows show zero refusals. Attempt counts are 372 for QnA, except Argon at 371 — [AA Coding Agents](https://artificialanalysis.ai/agents/coding).

| Agent, model, effort | Index v2.0 | FrontierCode v1.1 % | SWE-Atlas-QnA-AA % | Terminal-Bench 4.0 % |
|---|---|---|---|---|
| Antigravity CLI, Gemini 4 Argon (High) | 53.2 | 48.6 | 55.1 | 56.1 |
| Codex, DeepSeek V4.1 Flash 0910 (Max) | 47.3 | 52.6 | 61.0 | 28.3 |
| Grok Build, Grok 4.7 (Xhigh) | 46.6 | 43.6 | 62.9 | 33.3 |
| DeepSeek Harness, V4.1 Flash 1017 (Max) | 46.3 | 46.5 | 61.6 | 30.8 |
| Antigravity SDK, Gemini 3.8 Flash (High) | 33.3 | 40.8 | 44.4 | 14.7 |
| Context: Claude Code, Opus 5.5 (Max, default fallback) | 61.7 | 56.0 | 65.9 | 63.1 |
| Context: Muse Code, Muse Wonder Full (Max) | 58.9 | 48.7 | 68.8 | 59.1 |
| Context: Claude Code, Qwen3.8 Max (not the 27B) | 39.2 | 44.8 | 56.2 | 16.7 |

#### Vals (independent, run by Vals)
- Sources: [Vibe Code Bench, updated 29 Oct 2026](https://www.vals.ai/benchmarks/vibe-code), [SWE-bench Multimodal, updated 29 Oct 2026](https://www.vals.ai/benchmarks/swebench-multimodal), and model pages for [Argon](https://www.vals.ai/models/google_gemini-4-argon), [1017](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017), [Grok 4.7](https://www.vals.ai/models/grok_grok-4.7), [0910](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash), [V4 Pro 0813](https://www.vals.ai/models/deepseek_deepseek-v4-pro-0813), [V4 Pro April](https://www.vals.ai/models/deepseek_deepseek-v4-pro), [Gemini 3.8 Flash](https://www.vals.ai/models/google_gemini-3.8-flash), [Qwen3.8-27B](https://www.vals.ai/models/alibaba_qwen3.8-27b) and [3.5 Flash Lite](https://www.vals.ai/models/google_gemini-3.5-flash-lite).
- Efforts as listed by Vals: Argon high, 1017 max, Grok 4.7 xhigh, 0910 max, V4 Pro max, Gemini 3.8 Flash high, Qwen3.8-27B xhigh, 3.5 Flash Lite high.

| Model | Vibe Code Bench v1.1 % (rank/123) | Terminal-Bench 4.0 % (rank/59) | SWE-bench Multimodal % (rank/20) | Code Migration v1.1 % (rank/29) |
|---|---|---|---|---|
| Gemini 4 Argon | 91.91 ±1.90 (2) | 57.58 ±2.31 (8) | 56.04 ±2.27 (4) | 70.80 ±3.72 (6) |
| DeepSeek V4.1 Flash 1017 | 87.73 ±2.75 (12) | 31.82 ±2.62 (21) | not listed | 67.52 ±2.76 (7) |
| Grok 4.7 | 86.17 ±2.18 (13) | 28.79 ±2.31 (24) | 42.92 ±2.26 (13) | 53.22 ±2.56 (12) |
| DeepSeek V4.1 Flash 0910 | 84.74 ±2.89 (19) | 19.70 ±1.75 (33) | 46.46 ±2.28 (6) | 58.94 ±2.66 (9) |
| DeepSeek V4 Pro 0813 | 82.30 ±3.15 (25) | 14.14 ±2.02 (38) | not listed | 51.99 ±2.23 (14) |
| Gemini 3.8 Flash | 78.65 ±3.88 (32) | 19.70 ±2.31 (34) | 40.83 ±2.25 (16) | 38.65 ±3.65 (22) |
| Qwen3.8-27B | 64.85 ±4.83 (53) | not tested on 4.0 | not listed | not tested on v1.1 |
| DeepSeek V4 Pro, April build (OLDER) | 49.93 ±4.77 (65) | 11.11 ±1.34 (42) | not listed | not tested on v1.1 |
| Gemini 3.5 Flash Lite | 37.16 ±4.63 (77) | not tested on 4.0 | not listed | not tested on v1.1 |

- OLDER version, do not compare with the 4.0 column: Vals Terminal-Bench 2.1 gives Qwen3.8-27B 58.43 ±5.25 (42/75), Gemini 3.5 Flash Lite 50.19 ±0.99 (58/75) — [Vals Qwen](https://www.vals.ai/models/alibaba_qwen3.8-27b); [Vals Flash Lite](https://www.vals.ai/models/google_gemini-3.5-flash-lite).
- Vibe Code Bench tests building web apps from scratch, graded by an evaluator agent running point-and-click tests. The sample spec includes sign-up and log-in, and the tool list mentions Supabase state management and SQL execution. Most rows use OpenHands — [Vals Vibe Code](https://www.vals.ai/benchmarks/vibe-code).
- SWE-bench Multimodal asks a model to fix real GitHub issues in JavaScript repositories where the bug report depends on an image. It has 480 test tasks from eleven repositories, run with mini-swe-agent — [Vals Multimodal search result](https://www.vals.ai/benchmarks/swebench-multimodal).

#### Arena (independent, human votes, not an accuracy measure)
- Efforts are as labelled by Arena. WebDev has 153 models and 952,039 votes, dated 27 Oct 2026, and covers front-end web development including agentic workflows; "Prelim." marks limited data — [Arena WebDev](https://arena.ai/leaderboard/code/webdev). Text Coding has 414 models, dated 27 Oct 2026 — [Arena Text Coding](https://arena.ai/leaderboard/text/coding). Image-to-WebDev has 65 models, dated 19 Oct 2026 — [Arena Image-to-WebDev](https://arena.ai/leaderboard/code/image-to-webdev).

| Model | WebDev score (rank) | Text Coding score (rank) | Image-to-WebDev score (rank) |
|---|---|---|---|
| Gemini 4 Argon (High) | 1679 ±11 (11) | 1550 ±12 (5) | not listed |
| DeepSeek V4.1 Flash 1017 (Max) | 1665 ±8 (16) | not listed | not listed |
| Grok 4.7 (xHigh) | 1637 ±9 (21) | 1494 ±11 (91) | 1586 ±17 (20) |
| DeepSeek V4.1 Flash 0910 (Max) | 1619 ±11 (29) | 1523 ±10 (31) | 1606 ±22 (13) |
| Qwen3.8-27B (effort unlabelled) | 1590 ±6 (34) | 1498 ±8 (84) | 1577 ±8 (24) |
| Gemini 3.8 Flash (High), preliminary | 1583 ±7 (37) | 1530 ±7 (22) | 1593 ±13 (19) |
| DeepSeek V4 Pro (High, 0813) | 1582 ±9 (39) | 1505 ±11 (70) | not listed |
| Gemini 3.5 Flash-Lite | 1434 ±41 (91, 236 votes) | 1502 ±7 (77) | 1448 ±15 (50) |
| Gemini 3.1 Flash-Lite Preview (OLDER) | 1256 ±7 (138) | 1458 ±6 (148) | 1336 ±11 (64) |

#### Other sources on one scale
- Design Arena, Website (General Purpose) Elo, with no dates or vote counts shown: Argon 1,303 (14), DeepSeek V4.1 Flash 1,297 (16, build unstated), Gemini 3.8 Flash 1,295 (17), Grok 4.7 1,276 (33), V4 Pro 1,216 (78). Qwen3.8-27B was not found. Argon's Overall card shows "#170" with no score, which conflicts with its Website rank — [Design Arena](https://www.designarena.ai/leaderboard).
- AIM text-to-SQL, Bug Hunt Bench and Next.js Agent Evals are tabulated in the SQL, TypeScript and React section below.
- DeepSWE v1.1 public board (mini-swe-agent, 113 tasks, updated 22 Sep 2026): Gemini 3.8 Flash (high) 74% ±1, `deepseek-v4-pro` (max, build unstated) 63% ±6. Grok 4.7, Qwen3.8-27B, V4.1 Flash and Argon are absent from the page, which shows 21 of 28 models — [Datacurve](https://deepswe.datacurve.ai/). The mirror of Epoch's hub shows Gemini 3.8 Flash at 73.8% (high) and 71.0% (medium), and no other target model in its visible rows — [BenchLeader](https://www.benchleader.com/benchmarks/deepswe).
- ARCHIVED: SWE-bench Verified at Vals (last update 1 Sep 2026) is no longer run on new releases: V4 Pro 0813 96.40%, Qwen3.8-27B 86.00%, Gemini 3.8 Flash 80.00%, V4 Pro April 77.40%, Gemini 3.5 Flash Lite 75.00%. Grok 4.7, V4.1 Flash and Argon are absent — [Vals SWE-bench](https://www.vals.ai/benchmarks/swebench).
- Aider polyglot is stale: last updated 20 Nov 2025, with none of these models on it — [Aider](https://aider.chat/docs/leaderboards/).
- SWE-Bench Pro Public has none of these models in the rows I could read — [Scale](https://labs.scale.com/leaderboard/swe_bench_pro_public).

### Inferences
- AA v5.0 plus its Terminal-Bench 4.0 and FrontierCode 2.0 columns is the most complete strictly comparable set, because it covers every requested model in at least one variant, with effort variants for several.
- Arena WebDev, Vibe Code Bench and Bug Hunt Bench are the most web-relevant of the broad sources. They measure app building, preference and bug fixing, not answer accuracy.
- Any score for Qwen3.8-27B describes the Alibaba API at xhigh, a setting Groq does not list. Its results should be treated as an upper-bound proxy for the Groq deployment, not a measurement of it. This is my reading of the settings and is not tested anywhere.

### Gaps
- LiveBench could not be read: the fetch returned only the page title, and a direct download returned an 889-byte shell. I do not know whether these models are on it.
- The official Terminal-Bench leaderboard at tbench.ai loaded with an empty table, so TB 4.0 scores above come from AA and Vals.
- AA's page gives no per-model run dates for the v5.0 evaluations.
- I could not trace OpenRouter's "Coding Index" of 76.3 to any published source.
- Scale's SWE Atlas Refactoring board could not be reached at the URL I tried (404).

## Which of those are closest to answering knowledge questions, rather than running autonomous agents?

### Takeaway
SWE-Atlas-QnA is the closest coding benchmark, because agents must answer in writing and may not change code. It is still an agent test with tools, not a closed-book quiz. The truly one-shot multiple-choice evidence (MMLU Pro, MMMU-Pro) is not about software, and the one-shot coding evidence (LiveCodeBench) is older and missing three of the main models.

### Cited Findings

#### What SWE-Atlas-QnA measures
- "In Codebase QnA, an agent is placed inside a real repository and asked the kinds of questions engineers face in real work." It spans architecture, root-cause analysis, code onboarding, security, and API or library integration, and answers often require running the system, not only reading code — [Scale, 7 May 2026](https://scale.com/blog/swe-atlas-complete).
- It has 124 tasks. A task counts as resolved only when the answer is comprehensive against a rubric, and agents are told not to modify source files — [Scale leaderboard](https://labs.scale.com/leaderboard/sweatlas-qna).
- The AA variant keeps the same 124 tasks and 1,306 criteria but rewords 127 criteria and judges with GPT-6 Luna (xhigh) on five votes per criterion; Scale's judge is Claude Opus 4.5. Tasks that change tracked repository files fail. Attempts that error, time out or hit a safety refusal score zero — [AA methodology](https://artificialanalysis.ai/methodology/coding-agents-benchmarking).
- In the AA variant, agents answer in writing, and results inferred from reading code do not count where a criterion asks for observed results. Repositories are in Go, Python, C and TypeScript — [AA dataset card](https://huggingface.co/datasets/ArtificialAnalysis/SWE-Atlas-QnA-AA).

#### Scores on the two grading schemes (do not compare across them)
- Scale's official grading, mean Task Resolve Rate, with effort not listed for either target row: Gemini 3.8 Flash on Mini-SWE-Agent 47.04 ±5.08 (6 of 24); DeepSeek V4 Pro on Mini-SWE-Agent 27.15 ±4.74 (18 of 24, build unstated); top row Opus 5 on Claude Code at xHigh 63.17 ±5.01. The latest dated page update is 28 Jul 2026, though later models are present and marked NEW — [Scale](https://labs.scale.com/leaderboard/sweatlas-qna).
- AA grading, data of 30 Oct 2026, model plus agent: Grok Build with Grok 4.7 (Xhigh) 62.9% (234 of 372 attempts, 8th of 34 rows in the page data); DeepSeek Harness with 1017 (Max) 61.6%; Codex with 0910 (Max) 61.0%; Antigravity CLI with Argon (High) 55.1%; Antigravity SDK with Gemini 3.8 Flash (High) 44.4%. Top row: Muse Code with Muse Wonder Full (Max) 68.8% — [AA Coding Agents](https://artificialanalysis.ai/agents/coding).
- Qwen3.8-27B, V4 Pro 0813 and every Flash-Lite model have no SWE-Atlas-QnA-AA row, and Grok 4.7, Qwen3.8-27B, V4.1 Flash, Argon and Flash-Lite have no row on Scale's board — [AA Coding Agents](https://artificialanalysis.ai/agents/coding); [Scale](https://labs.scale.com/leaderboard/sweatlas-qna).

#### One-shot and multiple-choice evidence (mostly older)
- Vals LiveCodeBench is ARCHIVED ("we no longer run this benchmark on new model releases") with data as of 1 Sep 2026. It tests competitive programming problems in Python and its page does not say whether runs are one-shot — [Vals LiveCodeBench](https://www.vals.ai/benchmarks/lcb).
- Vals MMLU Pro and MMMU Pro appear on the model pages below. They have no entries on the Vals pages for Grok 4.7, either V4.1 Flash build, or Argon — [Grok](https://www.vals.ai/models/grok_grok-4.7); [0910](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash); [1017](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017); [Argon](https://www.vals.ai/models/google_gemini-4-argon).

| Model and Vals effort | LiveCodeBench % (rank/143) | MMLU Pro % (rank/138) | MMMU Pro, image MCQ % (rank/93) |
|---|---|---|---|
| [Gemini 3.8 Flash](https://www.vals.ai/models/google_gemini-3.8-flash) (high) | 89.48 ±0.90 (3) | 90.22 ±0.29 (5) | 89.08 ±0.75 (4) |
| [V4 Pro 0813](https://www.vals.ai/models/deepseek_deepseek-v4-pro-0813) (max) | 87.53 ±0.96 (13) | 86.97 ±0.34 (36) | not listed |
| [V4 Pro April](https://www.vals.ai/models/deepseek_deepseek-v4-pro) (max, OLDER) | 87.48 ±0.95 (14) | 87.25 ±0.34 (32) | not listed |
| [Qwen3.8-27B](https://www.vals.ai/models/alibaba_qwen3.8-27b) (xhigh) | 84.00 ±1.03 (43) | 84.34 ±0.36 (65) | 83.93 ±0.88 (28) |
| [Gemini 3.5 Flash Lite](https://www.vals.ai/models/google_gemini-3.5-flash-lite) (high) | 79.01 ±1.10 (75) | 85.84 ±0.34 (54) | 83.58 ±0.89 (30) |

- AA MMMU-Pro is a ten-option multiple-choice test combining image and text across 30 academic disciplines, run by AA itself — [AA MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro). AA values: Gemini 3.8 Flash High 85.6, Medium 84.2, Low 84.5; 1017 Max 80.6, Non-reasoning 69.2; 0910 Max 77.0; Gemini 3.5 Flash-Lite 79.0; Grok 4.7 Low 78.2, with no value found for High or Xhigh; Qwen3.8-27B Xhigh 76.3, Medium 74.2, Low 73.8, Non-reasoning 69.9; Gemini 3.1 Flash-Lite 75.6; none found for Argon — [AA page data](https://artificialanalysis.ai/evaluations/mmmu-pro).
- AA SciCode is a coding benchmark of 288 subproblems from 80 laboratory problems across 16 scientific disciplines. Its page does not state whether runs are one-shot — [AA SciCode](https://artificialanalysis.ai/evaluations/scicode). It is the only AA coding column not labelled as agentic that has a value for every requested model, shown in the first AA table.
- Developer-knowledge MCQ and QA benchmarks exist but have no runs on these models that I could find: CodeMMLU tests code understanding and reasoning, with a 2024 paper reporting GPT-4o on top — [CodeMMLU](https://arxiv.org/pdf/2410.01999); SimpleDevQA tests development knowledge QA on 21 unnamed LLMs, revised 29 Oct 2026 — [SimpleDevQA](https://arxiv.org/abs/2512.08867).

### Inferences
- The difference that matters: agent benchmarks such as Terminal-Bench, FrontierCode and DeepSWE allow hundreds of steps and can recover from a wrong idea by running tests, so they reward planning, tool use and persistence. A multiple-choice question gives one answer with no tools and no feedback.
- My ordering by closeness to MCQ answering, closest first: (1) SWE-Atlas-QnA, for written code understanding, with tools; (2) AIM text-to-SQL, because each item is one short question with one final answer, though it allows up to nine tool calls; (3) MMMU-Pro and MMLU Pro, for format only, since neither is about software; (4) LiveCodeBench and SciCode, for one-answer code writing; (5) Bug Hunt Bench, for code reading inside an agent run; (6) Text Arena Coding, for chat-style questions judged by preference; (7) Terminal-Bench, FrontierCode, DeepSWE and Vibe Code Bench, for outcomes of long runs.
- The SWE-Atlas-QnA-AA scores for Grok 4.7, 1017 and 0910 (61.0 to 62.9) are too close to separate. Scale reports about ±5 on these same tasks, so a gap of one or two points is within that band, though AA publishes no interval for these rows.
- QnA-AA can penalize pure reading where a criterion asks for observed results, so it is a test of investigation as much as of comprehension.

### Gaps
- No run of SWE-Atlas-QnA with tools turned off exists for these models, so closed-book code comprehension is unmeasured.
- Scale's QnA board lists no effort for Gemini 3.8 Flash or V4 Pro.
- Grok 4.7, V4.1 Flash and Argon have no LiveCodeBench or MMLU Pro score that I could find, so the older one-shot table cannot be extended to them.

## Who ran each test? Which scores are independent and which are vendor-reported?

### Takeaway
The current like-for-like tables are independent, run by AA, Vals, Scale, AIMultiple, Vercel, an individual benchmark author, or crowd voters. Almost all the headline launch numbers (Argon 77.9% DeepSWE, DeepSeek 77.0%, Grok 38.0% Terminal-Bench 4.0, Qwen 90.3% LiveCodeBench) are vendor-reported or vendor-selected.

### Cited Findings

| Evidence | Who ran it | Label |
|---|---|---|
| AA Index v5.0, Terminal-Bench 4.0, FrontierCode 2.0, MMMU-Pro | AA: "All evaluations are conducted independently by Artificial Analysis" — [AA](https://artificialanalysis.ai/evaluations/mmmu-pro) | Independent |
| AA Coding Agent Index v2.0 | AA, running agent products including vendor harnesses — [AA](https://artificialanalysis.ai/agents/coding) | Independent run of vendor tools |
| SWE Atlas QnA and Test Writing | Scale: "we ran a suite of frontier closed and open coding models" — [Scale](https://labs.scale.com/leaderboard/sweatlas-qna) | Independent, benchmark owner, LLM judge |
| Vals tables | Vals: "We evaluated..." — [Vals](https://www.vals.ai/models/grok_grok-4.7) | Independent |
| Arena WebDev and Text Coding | Rankings from user votes — [Arena](https://arena.ai/leaderboard/code) | Independent preference, not accuracy |
| Design Arena | Aggregates "real-world user preferences" — [Design Arena](https://www.designarena.ai/leaderboard) | Independent preference |
| AIM text-to-SQL | AIMultiple, collected and published by the firm — [AIM](https://aimultiple.com/text-to-sql) | Independent, one run per model |
| Bug Hunt Bench | Pawel Huryn, with a blind LLM judge — [benchmark data](https://bughunt.productcompass.pm/data/benchmark.json) | Independent, single operator |
| Next.js Agent Evals | Published by Next.js, the framework's owner, not a model vendor — [Next.js](https://nextjs.org/evals) | Independent of model vendors |
| DeepSWE v1.1 public board | Datacurve built it; the page does not say who executed the runs — [Datacurve](https://deepswe.datacurve.ai/) | Benchmark owner; rated Flawed by Epoch |
| Epoch hub DeepSWE data | Sourced from Datacurve's public leaderboard, not re-run — [Epoch](https://epoch.ai/benchmarks/deepswe) | Secondary |

#### Vendor-reported numbers
- Google: Argon's DeepSWE v1.1 and Terminal-Bench 4.0 results are "self computed", with a mini-swe agent harness for DeepSWE — [Google evaluation PDF](https://storage.googleapis.com/deepmind-media/gemini/gemini_4_argon_model_evaluation.pdf). Google's headline is "a new state of the art on DeepSWE v1.1 (77.9%)", dated 30 Sep 2026 — [Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/). Its model card lists Argon at DeepSWE v1.1 77.9%, Terminal-bench 4.0 57.4%, FrontierSWE v2 55.0% and Vibe Code Bench 91.9% — [Google model card](https://deepmind.google/models/model-cards/gemini-4-argon/).
- xAI: DeepSWE v1.1 71.0% at high (attributed to Datacurve); Terminal-Bench 4.0 38.0% at xhigh in Grok Build (attributed to Harbor); FrontierSWE V2 29.0% at xhigh (attributed to Proximal Labs); SWE-Marathon v1.1 46.0% at high (attributed to Abundant AI); CursorBench 4.0 46.3% at xhigh and 43.9% at high. These are vendor-published claims of third-party runs — [xAI model card, 21 Sep 2026](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf).
- DeepSeek: 1017 Terminal-Bench 4.0 42.3 and DeepSWE v1.1 77.0; 0910 Terminal-Bench 4.0 31.2 and DeepSWE v1.1 74.2. Harnesses are Claude Code and Mini-SWE-V2; the page does not state who ran them — [DeepSeek model card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017).
- Qwen: Terminal Bench 2.1 73.0, SWE-bench Pro 61.7, DeepSWE 1.1 42.2, LiveCodeBench v6 90.3, in the Claude Code harness, with QwenSWEBench and two others being in-house benchmarks — [Qwen model card](https://huggingface.co/Qwen/Qwen3.8-27B). Groq's page repeats these with no independent source — [Groq](https://console.groq.com/docs/model/qwen/qwen3.8-27b).

### Inferences
- xAI's attributions to Datacurve and Harbor could not be confirmed from the public boards I could read, because the Datacurve page does not show Grok 4.7 and the tbench.ai table was empty. I would label those "vendor-reported, third-party run claimed".
- Comparing a vendor's table with a rival's vendor table is the weakest use of these numbers, because harness and settings differ between them.

### Gaps
- Vals pages do not state a per-benchmark run date, and they warn that some benchmarks may use a different provider or parameters.
- Vals "Updates" text often disagrees with the same page's table, usually in ranks and denominators, which look like launch-time snapshots. I used the tables and could not confirm that reading.

## Are there independent head-to-head reviews or hands-on tests of these exact models on web development or debugging questions?

### Takeaway
I found no independent hands-on review that compares all of these models on web or debugging questions. The available reviews are small: one DeepSeek against Gemini 3.8 Flash build test, one Qwen review, one Grok 4.7 against 4.6 test, one Gemini 3.8 Flash against Opus 5 review, and user forum reports. Bug Hunt Bench is the nearest thing to a broad repeated head-to-head, and it is covered in the SQL, TypeScript and React section.

### Cited Findings
- DataCamp, 17 Sep 2026: DeepSeek V4.1 Flash against Gemini 3.8 Flash in OpenCode at `high`, one attempt each, building a single-file HTML and JavaScript rehearsal scheduler with a conflict indicator and localStorage. Both passed. DeepSeek scored 5/5/5 in 2 turns; Gemini scored 4/5/4 in 4 turns, with unrequested extras forcing the form column to scroll. The article states this is one run of one task at one effort setting. It predates the 1017 build — [DataCamp](https://www.datacamp.com/blog/deepseek-v4-1-flash-vs-gemini-3-8-flash).
- Simon Willison, 16 Aug 2026: Qwen 3.8 27B run locally as a 17GB GGUF. It gave a solid answer on how Datasette auth works and wrote a working converter script. With reasoning off, its HTML bounding-box tool drew boxes in the wrong places; at default xhigh the same tool was massively over-engineered. LM Studio's default 8,192-token context was used up by reasoning. "My strong recommendation: ignore that default." — [Simon Willison](https://simonwillison.net/2026/Aug/16/qwen-38-27b/).
- Puter blog, 25 Sep 2026: Grok 4.7 against Grok 4.6 at default settings, five runs per task. A buggy JavaScript `median` function was fixed 5/5 every run by both. The same five bugs in a rephrased Python function averaged 2.4/5 against 2.0/5. The author found no evidence of more self-checking. Puter sells access to these models and discloses no affiliation statement, and the test is not a web task — [Puter](https://developer.puter.com/blog/grok-4-7-review/).
- Promptslove, 3 Sep 2026: Gemini 3.8 Flash at high in OpenCode, compared with Opus 5 on three of five apps. A Node, Express, EJS, PostgreSQL and session-auth app scored 3/5: login and editing worked, navigation and the review queue did not. Gemini ignored a specified Three.js stack in one build. Long multi-part builds were unreliable while contained single-file tasks went well. Runs appear to be single builds, and the author sells prompt products — [Promptslove](https://promptslove.com/blog/gemini-3-8-flash-review/).
- Cursor forum, 26 to 29 Sep 2026, one page of a longer thread: about 12 of 17 users were negative on Grok 4.7 and one positive. Reports include breaking working code, thinking loops and weaker analysis than 4.6: "Grok 4.7 is really poor in analysis task as compared to Grok4.6". One user said it sticks better to what was asked. These are anecdotes — [Cursor forum](https://forum.cursor.com/t/share-your-thoughts-on-grok-4-7/172527?page=5).
- Google AI forum, 16 to 21 Oct 2026: users call Argon underwhelming for coding and "not on par with Anthropic's or Openai's models", and one says it "gets distracted by legacy specs, code, etc." No reproducible tests are given — [Google forum](https://discuss.ai.google.dev/t/how-bad-is-gemini-4-argon/190009).
- Seen in search snippets only, not opened, low weight: a Hacker News comment describing a "Wait, actually.." habit in Qwen 3.8 27B — [HN](https://news.ycombinator.com/item?id=49299605). Reviews on reseller or AI-tool blogs were not relied on.

### Inferences
- The recurring weakness across independent sources for Qwen3.8-27B is effort sensitivity: too little reasoning produces wrong output, and the default produces overthinking. That matters for a tool with short response times.
- User reports on Grok 4.7 and Argon are more negative than their benchmark positions suggest, but they come from self-selected forum posters doing long agent work, so they say little about single-question accuracy.

### Gaps
- No hands-on test covers Groq-hosted Qwen3.8-27B, either Flash-Lite model, or `deepseek-v4-pro` on web questions.
- No review tests any of these models on React, TypeScript or SQL multiple-choice questions.
- I found no Simon Willison review of Grok 4.7 or Gemini 3.8 Flash in the search results.

## Where do results disagree, and why?

### Takeaway
Most disagreement has five causes: index or benchmark version, harness, effort, model build, and grading rule. Several widely quoted numbers are out of date or misattributed, including the 59 and 46 Intelligence Index figures and a 57.9% Terminal-Bench score credited to Grok 4.7 that actually belongs to Fable 5.1.

### Cited Findings

#### Index version
- Gemini 3.8 Flash at launch was reported as scoring 59 on the AA Intelligence Index (search snippet only; the post itself returned 403) — [AA post](https://x.com/ArtificialAnlys/status/2095177419489739063). The current v5.0 value is 31 — [AA](https://artificialanalysis.ai/models/gemini-3-8-flash).
- A search summary gave Grok 4.7 (High) 46 and Gemini 3.8 Flash (Low) 33 for a comparison page; the same page now shows 35 and 22 on v5.0 — [AA](https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-gemini-3-8-flash-low).
- v5.0 began in October 2026, adding HLE-Diamond, Terminal-Bench-Science and FrontierCode 2.0 and rebalancing categories to 25% each. v4.3 in September had replaced Terminal-Bench 2.1 with 4.0 — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).
- The Coding Agent Index also changed: v2.0 replaced DeepSWE with FrontierCode v1.1 and renamed SWE-Atlas-QnA to SWE-Atlas-QnA-AA with adjusted grading — [AA](https://artificialanalysis.ai/methodology/coding-agents-benchmarking). A search summary gave Grok 4.7 (xhigh) 56 on this index, while the current v2.0 value is 46.6 — [AA](https://artificialanalysis.ai/agents/coding).

#### Harness: the same benchmark version, Terminal-Bench 4.0, across runners

| Model | Vendor | AA mini-swe-agent | Vals | AA vendor harness |
|---|---|---|---|---|
| Grok 4.7 | 38.0 xhigh, Grok Build | 25.8 Xhigh | 28.79 xhigh | 33.3 Xhigh, Grok Build |
| V4.1 Flash 1017 | 42.3, Claude Code | 33.8 Max | 31.82 max | 30.8 Max, DeepSeek Harness |
| V4.1 Flash 0910 | 31.2 | 26.8 Max | 19.70 max | 28.3 Max, Codex |
| Gemini 3.8 Flash | 19.1 | 19.7 High | 19.70 high | 14.7 High, Antigravity SDK |
| Gemini 4 Argon | 57.4, self computed | 57.1 High | 57.58 high | 56.1 High, Antigravity CLI |

- Sources: [xAI card](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf); [DeepSeek card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017); [DataCamp for the 19.1 figure](https://www.datacamp.com/blog/deepseek-v4-1-flash-vs-gemini-3-8-flash); [Google model card](https://deepmind.google/models/model-cards/gemini-4-argon/); [AA](https://artificialanalysis.ai/evaluations/terminalbench-4-0); [AA agents](https://artificialanalysis.ai/agents/coding); Vals model pages for [Grok](https://www.vals.ai/models/grok_grok-4.7), [1017](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017), [0910](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash), [Gemini](https://www.vals.ai/models/google_gemini-3.8-flash) and [Argon](https://www.vals.ai/models/google_gemini-4-argon).
- xAI itself says absolute Terminal-Bench scores "remain sensitive to the agent harness" — [xAI card](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf).
- Misattribution found: a search summary credited Grok 4.7 with 57.9% on Terminal-Bench 4.0. The xAI card's chart reads Fable 5.1 (max) 57.9% and Grok 4.7 (xhigh) 38.0% — [xAI card](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf).
- OLDER Terminal-Bench 2.1, shown only to illustrate the same effect: Qwen3.8-27B is 73.0 from its vendor — [Qwen](https://huggingface.co/Qwen/Qwen3.8-27B), 79.8 at AA (Xhigh) — [AA](https://artificialanalysis.ai/evaluations/terminalbench-2-1), and 58.43 at Vals — [Vals](https://www.vals.ai/models/alibaba_qwen3.8-27b). DeepSeek 0910 is 90.6 from its vendor but 74.53 at Vals across three trials — [Vals](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash).

#### Benchmark quality and grading
- Epoch rates DeepSWE v1.1 Flawed, in a partial review dated 7 Sep 2026, after finding grader false negatives in at least 23 of 113 tasks. 18 of those came from a verifier issue where editing existing tests can break grading — [Epoch review](https://epoch.ai/benchmarks/deepswe/review).
- DeepSWE boards also differ: Epoch's mirror lists GPT-6 Astra (xhigh) at 74.1% — [BenchLeader](https://www.benchleader.com/benchmarks/deepswe), while Mercor's page lists Muse Wonder 1.0 (Max) at 75.2% and GPT-6 Astra (Max) at 73.2% — [Mercor](https://www.mercor.com/apex/oss-benchmarks/oss-deep-swe-leaderboard/).
- SWE Atlas QnA scores are unstable across time and source. Scale's page text still says top models reach 30% while its table tops out at 63.17 — [Scale](https://labs.scale.com/leaderboard/sweatlas-qna). BenchLM lists Ling 3.1 Flash at 64.5% and Muse Spark 1.3 at 59.4%, rows that are not on Scale's table — [BenchLM](https://benchlm.ai/benchmarks/swe-atlas-codebase-qna).
- Gemini 3.8 Flash rates near the top of DeepSWE at about 74% — [Datacurve](https://deepswe.datacurve.ai/) yet lowest of the five target rows on SWE-Atlas-QnA-AA at 44.4% — [AA](https://artificialanalysis.ai/agents/coding).
- MMMU Pro differs between runners on the same model: Gemini 3.8 Flash 89.08 at Vals — [Vals](https://www.vals.ai/models/google_gemini-3.8-flash) against 85.6 at AA; Qwen3.8-27B 83.93 at Vals — [Vals](https://www.vals.ai/models/alibaba_qwen3.8-27b) against 76.3 at AA — [AA](https://artificialanalysis.ai/evaluations/mmmu-pro).
- SWE-bench Verified is saturated relative to newer tests: V4 Pro 0813 is 96.40% there (2nd) — [Vals SWE-bench](https://www.vals.ai/benchmarks/swebench) but 14.14% on Terminal-Bench 4.0 — [Vals](https://www.vals.ai/models/deepseek_deepseek-v4-pro-0813).

#### Model build
- V4.1 Flash results must be split by build, and they do not move in one direction. 1017 beats 0910 on Bug Hunt Bench (39.1 against 21.7, both at max in Claude Code) — [benchmark data](https://bughunt.productcompass.pm/data/benchmark.json), and on Arena WebDev (1665 against 1619) — [Arena](https://arena.ai/leaderboard/code/webdev), but falls on AIM SQL (22.8 against 33.5) — [AIM](https://aimultiple.com/text-to-sql).
- V4 Pro also shifts by build: Vibe Code Bench v1.1 is 82.30 for 0813 and 49.93 for the April build — [Vals](https://www.vals.ai/benchmarks/vibe-code).

#### Effort
- AA shows large drops without reasoning: 1017 goes from 32.5 (Max) to 18.5 (Non-reasoning) on Index v5.0, and Qwen3.8-27B from 20.1 (Xhigh) to 10.0 (Non-reasoning). Gemini 3.8 Flash barely changes between High (30.5) and Medium (30.0) but falls to 22.3 at Low — [AA](https://artificialanalysis.ai/evaluations/terminalbench-4-0).
- Effort is not always monotonic: Grok 4.7 on Bug Hunt Bench scored xhigh 29.0, medium 26.7, high 19.3, low 15.7 — [benchmark data](https://bughunt.productcompass.pm/data/benchmark.json).

#### Debugging-style boards disagree
- AA ITBench-AA (Kubernetes root-cause analysis, separate from the index): Gemini 3.8 Flash (High) 52.5, 0910 (Max) 46.9, Grok 4.7 (Xhigh) 42.1 — [AA page data](https://artificialanalysis.ai/evaluations/terminalbench-4-0); [definition](https://artificialanalysis.ai/methodology/intelligence-benchmarking).
- Vals SRE Bench: Argon 44.27 — [Vals](https://www.vals.ai/models/google_gemini-4-argon), Gemini 3.8 Flash 11.07 — [Vals](https://www.vals.ai/models/google_gemini-3.8-flash), Grok 4.7 3.82 — [Vals](https://www.vals.ai/models/grok_grok-4.7), V4 Pro 0813 1.91 — [Vals](https://www.vals.ai/models/deepseek_deepseek-v4-pro-0813), 0910 0.76 — [Vals](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash).

#### Arena snapshot drift
- Blog coverage placed Argon 8th on WebDev at 1,679 — [MindStudio search result](https://www.mindstudio.ai/blog/gemini-4-argon-benchmarks); the dated board shows the same 1679 at rank 11 on 27 Oct 2026 — [Arena](https://arena.ai/leaderboard/code/webdev).

### Inferences
- The stale 59 and 46 figures are most likely earlier v4.x values. AA's version history fits that, but I could not open the pages that originally showed them.
- Agreement is strongest where the harness is controlled: on Terminal-Bench 4.0, AA and Vals sit close for Argon and Gemini 3.8 Flash, while vendor runs with their own harness tend to be higher for Grok and DeepSeek. Argon's self-computed score matches AA and Vals closely, which raises confidence in that one vendor number.
- A model's rank depends on the skill tested. Grok 4.7 and DeepSeek are strong on QnA-AA and mid-table on Terminal-Bench 4.0, Argon shows the reverse pattern, and Gemini 3.8 Flash is strong on DeepSWE and SQL but weak on QnA-AA and Bug Hunt Bench.
- Because Epoch flags DeepSWE as Flawed and AA dropped it, DeepSWE scores deserve less weight than their prominence in launch tables suggests.

### Gaps
- I could not determine why Gemini 3.8 Flash's DeepSWE and SWE-Atlas-QnA-AA positions differ. The two tests have different harnesses and tasks, and no source explains the gap.
- I did not open the Vals SRE Bench methodology, so its scale and task type are unconfirmed.

## Is there anything specific on SQL, TypeScript, React, or debugging accuracy for these models?

### Takeaway
Yes, more than expected, but all of it is imperfect. AIM provides a wide SQL panel, Bug Hunt Bench gives TypeScript and React/Supabase bug-fixing scores, and Next.js Agent Evals covers one React framework. All three are agent or tool-assisted tests, not knowledge questions.

### Cited Findings

#### SQL: AIM text-to-SQL (updated 30 Oct 2026)
- Method: 759 BIRD-SQL questions across 11 databases. Models pick a database and write a query with up to nine tool calls. OpenRouter runs requested temperature 0, and no reasoning effort is named for them. BIRD's hints are withheld. It is one run per model. 236 of 759 references were flagged as broken, and an LLM jury reviews missed answers — [AIM](https://aimultiple.com/text-to-sql).
- AIM warns that each model reaches a different question set and that "A controlled SQL comparison would supply every model with the correct database for the same questions. That experiment has not been run." — [AIM](https://aimultiple.com/text-to-sql).
- 1017 was run on 30 Oct 2026 through OpenRouter. The two Flash-Lite rows used an older tool-call layer (`pre_v3`) — [AIM](https://aimultiple.com/text-to-sql); [AIM data download](https://cdn.aimultiple.com/benchmark_data/article5_text-to-sql_data.zip?v=1793466393).

| Model | SQL accuracy % (strict, broken refs removed) | Before reference review % | After answer review % | Scored n / correctly routed n |
|---|---|---|---|---|
| gemini-4-argon | 78.6 | 64.3 | 81.4 | 518 / 747 |
| gemini-3.8-flash | 77.2 | 63.5 | 82.2 | 443 / 613 |
| gemini-3.5-flash-lite | 57.4 | 46.4 | 68.7 | 444 / 645 |
| gemini-3.1-flash-lite | 57.0 | 45.8 | 68.1 | 386 / 570 |
| grok-4.7 | 53.8 | 43.3 | 74.9 | 470 / 682 |
| qwen3.8-27b | 49.4 | 41.6 | 72.8 | 460 / 668 |
| deepseek-v4-pro-0813 | 46.0 | 38.0 | 72.7 | 465 / 674 |
| deepseek-v4.1-flash (0910) | 33.5 | 28.8 | 69.3 | 481 / 694 |
| deepseek-v4.1-flash-1017 | 22.8 | 19.4 | 63.8 | 474 / 682 |
| Context: claude-opus-5.5 (Claude Code, medium) | 87.8 | 74.9 | 91.1 | 506 / 733 |
| Context: grok-4.6 (OLDER) | 64.2 | 50.4 | 74.5 | 475 / 694 |

- Older or non-target SQL items: UniQL reports DeepSeek V4 Flash at about 51.6% on SQLite under BIRD's difficulty stratification, seen in a search summary only — [UniQL](https://arxiv.org/pdf/2606.08018). Google's Gemini-SQL2 at 80.04% on BIRD is built on Gemini 3.1 Pro and is not one of these models — [AI Weekly](https://aiweekly.co/alerts/googles-gemini-sql2-tops-bird-text-to-sql-at-8004).

#### TypeScript, React and debugging: Bug Hunt Bench (updated 27 Oct 2026)
- It plants 105 real regressions, with test suites left green, across a roughly 28K-line TypeScript VS Code extension (45 bugs) and a roughly 60K-line React and Supabase learning platform (60 bugs). Each model uses its native CLI, and an independent judge grades the diff blind against a withheld key — [benchmark data](https://bughunt.productcompass.pm/data/benchmark.json).
- Noise is high: identical configurations run three times spanned 1 to 14 points of 105, and the author warns that a gap of a few points may be noise. Runs that read answers from outside their folder were voided, and some DeepSeek rows carry integrity warnings. The judge differs across rows (Grok on some, Codex on others) — [benchmark data](https://bughunt.productcompass.pm/data/benchmark.json).
- Board leader among current rows: Sonnet 5.5 (max), mean of 3 runs, 51.3 of 105 — [benchmark data](https://bughunt.productcompass.pm/data/benchmark.json). No Flash-Lite model is on the board.

| Model, harness, effort, runs, date | Total /105 | TypeScript extension /45 | React + Supabase /60 |
|---|---|---|---|
| V4.1 Flash 1017, DeepSeek Harness, max, 7 runs, 18 Oct | 42.7 | 19.0 | 23.7 |
| V4.1 Flash 1017, Pi, max, 5 runs, 18 Oct | 42.2 | 17.8 | 24.4 |
| Gemini 4 Argon, Antigravity CLI, high, 3 runs, 14 Oct | 40.7 | 13.0 | 27.7 |
| Gemini 4 Argon, Antigravity CLI, medium, 3 runs, 14 Oct | 39.3 | 13.7 | 25.7 |
| V4.1 Flash 1017, Pi, high, 5 runs, 18 Oct | 40.4 | 16.0 | 24.4 |
| V4.1 Flash 1017, Claude Code, max, 7 runs, 18 Oct | 39.1 | 18.1 | 21.0 |
| Gemini 4 Argon, Antigravity CLI, low, 3 runs, 14 Oct | 35.3 | 12.7 | 22.7 |
| V4.1 Flash 1017, Pi, low, 5 runs, 18 Oct | 33.8 | 14.0 | 19.8 |
| Grok 4.7, Grok Build, xhigh, 5 runs, 8 Oct | 29.0 | 13.0 | 16.0 |
| Grok 4.7, Grok Build, medium, 3 runs, 21 Sep | 26.7 | 12.0 | 14.7 |
| V4.1 Flash 0910, Claude Code, max, 3 runs, 15 Sep | 21.7 | 11.3 | 10.3 |
| Grok 4.7, Grok Build, high, 3 runs, 21 Sep | 19.3 | 8.7 | 10.7 |
| Gemini 3.8 Flash, Antigravity CLI, high, 3 runs, 15 Sep | 18.0 | 6.7 | 11.3 |
| V4 Pro, Claude Code on DeepSeek API, max, 1 run, 10 Sep | 16 | 8 | 8 |
| Grok 4.7, Grok Build, low, 3 runs, 21 Sep | 15.7 | 10.3 | 5.3 |
| Qwen3.8-27B, Claude Code on Alibaba API, xhigh, 3 runs, 15 Sep | 15.0 | 5.7 | 9.3 |
| Qwen3.8-27B 8-bit, OpenRouter via Parasail, default, 3 runs, 16 Sep | 10.7 | 3.7 | 7.0 |

#### React framework: Next.js Agent Evals (last run 30 Oct 2026)
- Success rate is pass@4, meaning any of four attempts passing. New evals a model has not run count as failures, and the table's second column uses bundled AGENTS.md documentation — [Next.js](https://nextjs.org/evals).
- Gemini 4 Argon in OpenCode: 97% without AGENTS.md, 97% with. Grok 4.7 in OpenCode: 94% and 94%. Gemini 3.8 Flash in OpenCode: 90% and 97%. Effort is not listed. Qwen3.8-27B, V4.1 Flash, V4 Pro and Flash-Lite are not on the board — [Next.js](https://nextjs.org/evals).

#### Testing and other JavaScript or TypeScript evidence
- SWE Atlas Test Writing has 90 tasks across 11 repositories in Go, Python, C and TypeScript, with its latest update on 28 Jul 2026. Gemini 3.8 Flash on Mini-SWE-Agent 53.70 ±5.86 (4 of 24); V4 Pro on Mini-SWE-Agent 27.05 ±5.59 (22 of 24). Effort is not stated. The other target models are absent — [Scale](https://labs.scale.com/leaderboard/sweatlas-tw).
- SWE-bench Multimodal is JavaScript bug fixing from image-dependent issue reports, tabulated in the first section. It is the only coding evidence found that combines image input and JavaScript — [Vals](https://www.vals.ai/benchmarks/swebench-multimodal).

#### Web-specific benchmarks with no results for these models
- Web-Bench is a 2025 ByteDance benchmark of 50 projects of 20 tasks each, and its best result then was 25.1% Pass@1 on Claude 3.7 Sonnet — [Web-Bench paper](https://arxiv.org/pdf/2505.07473). A "Web Bench" board lists only two self-reported Seed models — [LLM Stats](https://llm-stats.com/benchmarks/web-bench).
- BaxBench tests secure backend generation across 392 tasks, and I found only its 2025 results, in which the best model reached 62% correctness — [BaxBench](https://iclr.cc/virtual/2025/33345).

### Inferences
- The strict SQL column overstates differences. The spread shrinks a lot after answer review, from 22.8 to 78.6 strict down to 63.8 to 82.2 reviewed. 1017 looks unusually dependent on this: its answers often seem acceptable to a jury but not an exact result match. The reviewed column depends on an LLM jury, so neither column is a clean truth.
- The SQL panel still gives real signal for the Gemini family: Argon and Gemini 3.8 Flash stay near the top on strict scoring, and Gemini 3.8 Flash stays there after review. However, Gemini 3.8 Flash routed only 613 of 759 questions correctly, so it was scored on a different and smaller subset than Argon (747).
- Bug Hunt's React and Supabase repo is the nearest available proxy for full stack debugging skill. Bug fixing is still not the same as picking the right option in a question.
- The Qwen3.8-27B 8-bit row sits below the first-party row, but effort also differs (default against xhigh), so the gap cannot be assigned to quantization alone. It is a reason for care with hosted variants, and it says nothing direct about Groq.

### Gaps
- No Grok 4.7 or Qwen3.8-27B SQL result exists from any source other than AIM.
- AIM does not name reasoning effort for its OpenRouter runs, and a low or default setting could explain part of DeepSeek's strict score. DeepSeek's card recommends temperature 1.0, while AIM requested temperature 0.
- There is no Bug Hunt Bench, Next.js or QnA result for Flash-Lite models, and no Next.js result for DeepSeek or Qwen.

## What evidence is missing?

### Takeaway
No benchmark I could find tests full stack multiple-choice questions on these models. Everything here is indirect evidence, and any statement about MCQ accuracy on these topics would be an extrapolation.

### Cited Findings
- SWE-Atlas-QnA, the closest test, has no Qwen3.8-27B, V4 Pro 0813 or Flash-Lite row at AA, and no Grok 4.7, Qwen3.8-27B, V4.1 Flash, Argon or Flash-Lite row at Scale — [AA](https://artificialanalysis.ai/agents/coding); [Scale](https://labs.scale.com/leaderboard/sweatlas-qna).
- All SWE-Atlas-QnA-AA rows are model plus agent variants, so no pure model score exists on it. Each row reflects the model, its settings and its execution configuration — [AA Coding Agents](https://artificialanalysis.ai/agents/coding).
- Groq was not found in the one provider comparison I checked. The Vals Inference Provider Index (updated 20 Oct 2026) covers DeepSeek V4.1 Flash, Kimi K3 and MiniMax M3 only, and third-party providers of V4.1 Flash were within error of first-party accuracy — [Vals](https://www.vals.ai/benchmarks/inference_provider).
- Groq's page lists no independent benchmark of its own deployment and repeats vendor figures — [Groq](https://console.groq.com/docs/model/qwen/qwen3.8-27b).
- Two older one-shot sources stopped running on new models: Vals LiveCodeBench — [Vals](https://www.vals.ai/benchmarks/lcb) and SWE-bench Verified — [Vals](https://www.vals.ai/benchmarks/swebench). Aider's board stopped on 20 Nov 2025 — [Aider](https://aider.chat/docs/leaderboards/).

### Inferences
- The strongest honest statement is about patterns across indirect tests, not about MCQ accuracy. The evidence base can support statements like "stronger on written code investigation" or "stronger on strict SQL", not "better at React questions".
- A small custom test would fill the largest gap more cheaply than further desk research: the same set of full stack MCQs, with and without code screenshots, through the exact API IDs and effort settings the tool will use, repeated several times. Bug Hunt Bench shows why repeats matter, given its 1 to 14 point spreads on identical configurations.

### Gaps
- No benchmark found for MCQ accuracy on HTML, CSS, JavaScript, TypeScript, React, Node, Python or Java APIs, SQL, HTTP, authentication, caching, testing, deployment or debugging on these models.
- No topic-level results found for HTTP, caching, authentication, or deployment on any of these models. No Java API-specific result was found. A search summary mentioned a Java coding-agent study on the V4 Flash predecessor, which I did not open.
- No benchmark found for reading code from images and choosing an answer. SWE-bench Multimodal and Arena Image-to-WebDev are the nearest and neither is a knowledge test.
- No evaluation of Groq-hosted Qwen3.8-27B was found on any benchmark, including at its available effort levels, or of whether Groq's deployment is quantized.
- Low-effort behaviour is thinly covered. AA has Low and Non-reasoning rows for some models, but QnA, Vals, Bug Hunt and SQL evidence is mostly at high or maximum effort, or unnamed.
- Flash-Lite evidence is limited to AA, Vals, Arena and AIM. There is no code-comprehension result for it.
- Pages that could not be used: LiveBench (title only), tbench.ai (empty table), Scale Refactoring (404 at the URL tried), and the AA post on X (403). Android Bench coverage of Argon was seen only in secondary reports, was outside web scope, and was not checked.
