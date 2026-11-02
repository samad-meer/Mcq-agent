# Git, GitHub and command-line accuracy, and multiple-choice reliability, of current LLMs (as of 1 November 2026)

## Question 1: Which benchmarks test command-line and tool knowledge on these models, and why do Terminal-Bench figures differ?

### Takeaway
No benchmark tests Git or GitHub knowledge on these models. Terminal-Bench is the only command-line benchmark with rows for them, but it scores long agent runs, and none of the 66 Terminal-Bench 4.0 task instructions mentions Git. Most of the differing figures for one model come from harness, effort, benchmark version and snapshot date: when the harness is the same, the official board, Artificial Analysis (AA) and Vals agree within about 3 points.

### Cited Findings

#### Which rows apply to the models in scope
- `deepseek-flash` "is now served by DeepSeek-V4.1-Flash-1017", and the older names `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` now route to the same model — [DeepSeek API docs](https://api-docs.deepseek.com/). AA marks the earlier V4.1 Flash of 10 September as deprecated — [AA model page](https://artificialanalysis.ai/models/deepseek-v4-1-flash). So the 1017 rows are the ones that apply. Earlier-snapshot rows appear below only for contrast.
- Groq lists `qwen/qwen3.8-27b` as Preview. It accepts up to 3 images per request, offers `reasoning_effort` values `default`, `none`, `low`, `medium` and `high`, and caps output at 16,384 tokens — [Groq model page](https://console.groq.com/docs/model/qwen/qwen3.8-27b). Alibaba's card says the model's default effort is `xhigh` — [Hugging Face card](https://huggingface.co/Qwen/Qwen3.8-27B). AA tested Xhigh, Medium, Low and Non-reasoning — [AA model page](https://artificialanalysis.ai/models/qwen3-8-27b). So AA has no row at Groq's top named setting (`high`).
- `gemini-3.8-flash`, `gemini-3.5-flash-lite`, `gemini-3.1-flash-lite` and `gemini-4-argon` are listed as stable, and `gemini-3.1-flash-lite-preview` is shut down. The only 3.8 Flash-Lite ID listed is the speech model `gemini-3.8-flash-lite-tts` — [Gemini API models](https://ai.google.dev/gemini-api/docs/models). AA's "Gemini 3.1 Flash-Lite" row is keyed to the preview ID and marked deprecated — [AA evaluations data](https://artificialanalysis.ai/evaluations/terminalbench-4-0).
- Gemini 4 Argon had restricted access at launch. On 9 October The Batch said it was limited to Google's Fairwind cybersecurity programme — [The Batch](https://www.deeplearning.ai/the-batch/argon-a-low-hallucination-model-build-for-knowledge-work). The Gemini API page now lists it as stable — [Gemini API models](https://ai.google.dev/gemini-api/docs/models). AA tested it at High only — [AA model page](https://artificialanalysis.ai/models/gemini-4-argon).
- AA shows image input as false for DeepSeek V4 Pro 0813 and true for V4.1 Flash 1017 — [AA model page](https://artificialanalysis.ai/models/deepseek-v4-pro). DeepSeek's docs page does not say which snapshot `deepseek-v4-pro` maps to — [DeepSeek API docs](https://api-docs.deepseek.com/).

#### How the numbers were read
- AA's text view shows only the top of each chart, so per-model AA values in these notes come from the data embedded in AA's public pages, downloaded on 2026-11-01. They matched every visible value checked, for example Kimi K3.1 Pro 67.2% on Terminal-Bench 4.0 and Gemini 3.8 Flash 95.3% on GPQA Diamond — [AA Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0); [AA GPQA Diamond](https://artificialanalysis.ai/evaluations/gpqa-diamond). AA gives no per-row run dates.
- Official Terminal-Bench rows were read the same way from the data embedded in the leaderboard page on 2026-11-01 — [tbench.ai leaderboard](https://www.tbench.ai/leaderboard).

#### Terminal-Bench versions (never comparable across rows)

| Version | Date | Tasks | What changed | Status |
|---|---|---|---|---|
| 1.0 | May 2025 | 80 | First release | Retired |
| 2.0 | Nov 2025 | 89 | Harder curated set, Harbor framework | Retired |
| 2.1 | May 2026 | 89 | 28 tasks revised | Retired |
| 3.0 | Jul 2026 | 74 | Harder rolling set, separate agent and verifier containers | Retired |
| 4.0 | 28 Aug 2026 | 66 | 8 removed, 19 revised, flat 8-hour timeout, recalibrated resources | Current |

Sources: [Snorkel version history](https://snorkel.ai/leaderboard/terminal-bench/), [Terminal-Bench 4.0 post](https://www.tbench.ai/news/terminal-bench-4-0), [Terminal-Bench 3.0 post](https://www.tbench.ai/news/terminal-bench-3-0), [Terminal-Bench news index](https://www.tbench.ai/news) for the 4.0 date, [LLM Learner status table](https://llmlearner.com/rankings/terminal-bench-4-0). Snorkel says 20 tasks were revised in 4.0; the official post says 19. The official post calls resource changes and task removals breaking changes that require re-running trials.

#### Terminal-Bench 4.0 scores (percent of tasks solved)

| Model and config | Official board (66 tasks × 5 trials, ±95% CI) | Vendor-reported | AA (mini-swe-agent, 3 repeats, E2B, 500-step cap) | Vals (mini-swe-agent, avg@3, Daytona, no step cap, as of 29 Oct) |
|---|---|---|---|---|
| Grok 4.7 | 37.58 ±3.54, xhigh, Grok Build | 37.6 xHigh | 25.8 xhigh; 24.7 high; 16.2 low | 28.79 xhigh |
| Qwen3.8-27B | No row | Not on its card | 5.6 xhigh; 5.1 medium; 2.5 low; 0.0 none | Not listed |
| DeepSeek V4.1 Flash 1017 | No row | 42.3, Claude Code harness | 33.8 max; 9.1 none | 31.82 max |
| DeepSeek V4.1 Flash (10 Sep, replaced) | No row | 31.2 | 26.8 max; 5.6 none | 19.70 high |
| Gemini 3.8 Flash | 19.09 ±3.36, high, mini-SWE-agent | 19.1 | 19.7 high; 19.7 medium; 10.1 low | 19.70 high |
| Gemini 3.5 Flash-Lite | No row | Not found | 1.0 | Not listed |
| Gemini 3.1 Flash-Lite (preview ID) | No row | Not found | 0.5 | Not listed |
| Gemini 4 Argon | No row | 57.4 Max, via a secondary table only | 57.1 high | 57.58 high |
| DeepSeek V4 Pro 0813 (reference) | No row | Not found | 14.1 max; 1.5 none | 14.14 max |

Sources: [tbench.ai leaderboard](https://www.tbench.ai/leaderboard); [xAI launch post](https://x.ai/news/grok-4-7); [DeepSeek 1017 card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017); [Google model card](https://deepmind.google/models/model-cards/gemini-3-8-flash/); [AA Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0); [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking); [Vals Terminal-Bench 4.0](https://www.vals.ai/benchmarks/terminal-bench-4); [LLM Learner](https://llmlearner.com/rankings/terminal-bench-4-0) for Argon's vendor figure. Effort labels on Vals rows come from [BenchLM's mirror of Vals data](https://benchlm.ai/benchmarks/vals-terminal-bench-4), dated 27 October. The official board had 35 rows on 2026-11-01. None is for Qwen3.8-27B, any DeepSeek model, Gemini 4 Argon or any Flash-Lite model.

#### Terminal-Bench 2.1 scores (retired version, not comparable with 4.0)

| Model and config | Vendor-reported | AA (Terminus 2, E2B, 3 repeats) | Vals (Terminus 2, Daytona, pass@1, archived) |
|---|---|---|---|
| Grok 4.7 | Not found | No row | 73.41 |
| Qwen3.8-27B | 73.0, Terminus | 79.8 xhigh; 67.4 low; 65.2 medium; 49.1 none | 58.43 |
| DeepSeek V4.1 Flash (10 Sep) | 90.6, DeepSeek Harness Minimal, max | No row | 74.53 |
| DeepSeek V4.1 Flash 1017 | Not found | No row | No row |
| Gemini 3.8 Flash | 89.4, harness not stated | 87.6 high; 83.9 medium; 83.1 low | 81.27 |
| Gemini 3.5 Flash-Lite | Not found | 53.6 | 50.19 |
| Gemini 3.1 Flash-Lite (preview ID) | Not found | 31.1 | 34.08 |
| Gemini 4 Argon | Not found | No row | 57.68 |
| DeepSeek V4 Pro 0813 (reference) | 87.9, snapshot not stated | 78.7 | 54.68 |

Sources: [Alibaba card](https://huggingface.co/Qwen/Qwen3.8-27B); [DeepSeek V4.1 Flash card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash); [Google model card](https://deepmind.google/models/model-cards/gemini-3-8-flash/); [AA Terminal-Bench 2.1](https://artificialanalysis.ai/evaluations/terminalbench-2-1); [Vals Terminal-Bench 2.1](https://www.vals.ai/benchmarks/terminal-bench-2-1).

#### Other Terminal-Bench versions
- **2.0:** Vals' archived page shows rankings as of 4 June 2026. Of the models in scope, only DeepSeek V4 (56.18%, listed under the `deepseek-v4-pro` link) and Gemini 3.1 Flash Lite Preview (24.72%) have rows, and both results are older — [Vals Terminal-Bench 2.0](https://www.vals.ai/benchmarks/terminal-bench-2).
- **3.0:** DeepSeek reports 30.0 for V4.1 Flash and 11.8 for V4 Pro on its own harness, at max effort — [DeepSeek V4.1 Flash card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash). The official launch post's top scores were 34.4 and 33.8 — [Terminal-Bench 3.0 post](https://www.tbench.ai/news/terminal-bench-3-0). I found no independent 3.0 row for any model in scope.
- **1.0:** I found no rows for the models in scope.
- **Terminal-Bench Hard:** This is a legacy AA evaluation that AA replaced with 2.1 in Index v4.1 — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking). The only rows near scope are older snapshots: Gemini 3.1 Flash-Lite (preview ID) at 24.2 and DeepSeek V4 Pro 0424 (Max) at 46.2 — [AA evaluations](https://artificialanalysis.ai/evaluations/terminalbench-hard).

#### Why the same model has different figures
- **Harness is the largest documented cause.** The official board accepts each lab's own agent: xAI used Grok Build and Google used mini-SWE-agent — [tbench.ai leaderboard](https://www.tbench.ai/leaderboard). DeepSeek says it used the Claude Code harness for its 42.3 — [DeepSeek 1017 card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017). AA and Vals both use mini-swe-agent with bash — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking); [Vals Terminal-Bench 4.0](https://www.vals.ai/benchmarks/terminal-bench-4).
- **A natural experiment supports this.** Google's official mini-SWE-agent run (19.09) matches AA and Vals (19.7 each). xAI's Grok Build run (37.58) is 9 to 12 points above AA and Vals at the same xhigh effort. DeepSeek's Claude Code figure (42.3) is 8 to 10 points above theirs — sources as in the 4.0 table above.
- **Vendor data shows harness spread directly.** On Terminal-Bench 2.1, V4.1 Flash scored 84.1 (Codex), 85.0 (OpenCode), 85.8 (two DeepSeek Harness modes), 86.1 (Pi), 88.0 (Claude Code), 90.3 (mini-SWE) and 90.6 (DeepSeek Harness Minimal), with N=3 and max_steps=500 — [DeepSeek V4.1 Flash card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash).
- **Effort changes scores on the same harness.** On AA, Gemini 3.8 Flash scores 10.1 at low and 19.7 at medium and high, and Grok 4.7 scores 16.2 at low and 25.8 at xhigh — [AA Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0). Vals' 19.70 for the 10 September V4.1 Flash is a high-effort run, while AA's 26.8 is max — [BenchLM's mirror of Vals data](https://benchlm.ai/benchmarks/vals-terminal-bench-4).
- **Trial counts and noise differ.** The official board runs 330 trials per row with half-widths near ±3.5 — [tbench.ai leaderboard](https://www.tbench.ai/leaderboard). AA and Vals use 3 repeats, and Vals shows ±2.31 standard errors for both Grok 4.7 and Gemini 3.8 Flash — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking); [Vals comparison](https://www.vals.ai/comparisons/google_gemini-3.8-flash-vs-grok_grok-4.7).
- **Infrastructure matters.** Anthropic measured a 6-point gap on Terminal-Bench 2.0 between most- and least-resourced setups (published 5 February 2026) — [Anthropic engineering](https://www.anthropic.com/engineering/infrastructure-noise). AA uses E2B and a 500-step cap, while Vals uses Daytona with no step limit — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking); [Vals Terminal-Bench 4.0](https://www.vals.ai/benchmarks/terminal-bench-4).
- **The same harness name does not guarantee the same result on 2.1.** AA and Vals both use Terminus 2, yet Qwen3.8-27B is 79.8 versus 58.43 and V4 Pro 0813 is 78.7 versus 54.68. Neither source explains this gap — [AA Terminal-Bench 2.1](https://artificialanalysis.ai/evaluations/terminalbench-2-1); [Vals Terminal-Bench 2.1](https://www.vals.ai/benchmarks/terminal-bench-2-1).
- **Rounding creates phantom differences.** xAI's post and the official board say 37.6 and 37.58 — [xAI launch post](https://x.ai/news/grok-4-7); [tbench.ai leaderboard](https://www.tbench.ai/leaderboard). BenchLM lists the same run as 38.00% — [BenchLM](https://benchlm.ai/md/models/grok-4-7.md).
- **Old snapshots circulate.** A 22 September digest reported Vals' Grok 4.7 result as 12.12 and noted that Vals' rows named no reasoning setting — [The Aggregate](https://buttondown.com/theaggregate/archive/grok-47-terminal-and-web-agent-coding-gains-lower/). Vals now shows 28.79 at xhigh — [Vals Terminal-Bench 4.0](https://www.vals.ai/benchmarks/terminal-bench-4).
- **Version mixing causes the largest gaps.** Gemini 3.8 Flash is 87.6 on AA's 2.1 and 19.7 on AA's 4.0, because they are different tests — [AA Terminal-Bench 2.1](https://artificialanalysis.ai/evaluations/terminalbench-2-1); [AA Terminal-Bench 4.0](https://artificialanalysis.ai/evaluations/terminalbench-4-0).
- **The official board has integrity rules.** It requires trajectories for passing trials, and an agent judge reviews them. Past removals involved changed timeouts, embedded solutions and uploaded tests — [Terminal-Bench integrity update](https://www.tbench.ai/news/leaderboard-integrity-update).

#### How well each benchmark maps to answering a Git question

| Benchmark | What it measures | Fit for a Git exact-detail question |
|---|---|---|
| Terminal-Bench 4.0 | Long agent tasks with an 8-hour limit; all verifier tests must pass | Poor. A case-insensitive word search of all 66 `instruction.md` files found "git" in none, and "commit" only once, as a CLI subcommand name in an unrelated task — [repository tasks](https://github.com/harbor-framework/terminal-bench/tree/main/tasks) |
| Terminal-Bench 2.1 | 89 tasks in a terminal | Partial. The repository's `legacy` folder has five Git-named tasks: `fix-git`, `git-leak-recovery`, `git-multibranch`, `sanitize-git-repo`, `configure-git-webserver` — [repository legacy folder](https://github.com/harbor-framework/terminal-bench/tree/main/legacy). Published scores are aggregates only |
| InterCode-ALFA and NL2SH-ALFA | Natural language to shell command, scored by execution | Closest for shell recall, but no model in scope has been tested |
| GitGoodBench | Agent work on three Git scenarios | Closest for Git workflow, tested on GPT-4o only |
| Git-Assistant | Natural language to Git command sequences in a real repository | Closest for Git commands, tested on GPT-4o and o4-mini only |

#### NL2Bash and command generation
- "Local LLMs for NL2Bash" (LAST-X workshop at NDSS 2026, KU Leuven) tested 22 open models of 1B to 32B on the 300-task InterCode-ALFA set. Baseline task completion averaged 0.60. Qwen3-14B scored 0.80 to 0.82, Qwen3-8B 0.75 and Qwen3-32B 0.75 to 0.78. These are Qwen3 models, not 3.8 — [LAST-X paper](https://www.ndss-symposium.org/wp-content/uploads/lastx2026-49.pdf).
- That paper rejected Terminal-Bench as a fit for this question because it is "specifically designed to evaluate complex agents through difficult, multi-turn scenarios" — [LAST-X paper](https://www.ndss-symposium.org/wp-content/uploads/lastx2026-49.pdf).
- The NL2SH work at NAACL 2025 provides 600 manually verified test pairs and 40,939 training pairs, with a functional-equivalence check. It reports that parsing, in-context learning, in-weight learning and constrained decoding can raise accuracy by up to 32% — [NAACL 2025 paper](https://preview.aclanthology.org/setup/2025.naacl-long.555).
- A 2026 paper builds a 9,930-command benchmark over 482 tools from the tldr corpus and checks flags against `--help` and man pages, but it is a verifier, not a model exam. I saw it only as a search excerpt — [arXiv 2609.11957](https://arxiv.org/pdf/2609.11957).

#### Git-specific studies (older models only)
- GitGoodBench (May 2025) has 900 samples in its full suite and 120 in a prototyping suite. GPT-4o with custom tools solved 21.11% of the prototyping suite — [arXiv 2505.22583](https://arxiv.org/abs/2505.22583).
- Git-Assistant (July to September 2026) ran 200 paraphrased requests. A plain GPT-4o request matched the ground truth 12.0% of the time in both environments, and 19.0% and 16.0% with repository state added. For o4-mini, the figures were 19.0% and 9.0%, then 24.0% and 26.0% with state — [arXiv 2607.09224](https://arxiv.org/html/2607.09224).
- By operation in the base environment, plain GPT-4o scored 10.0% on rebase, 8.3% on branch creation, and 0% on commit, merge, reset, squash, tagging and update or move — [arXiv 2607.09224](https://arxiv.org/html/2607.09224).
- About 92% of plain-LLM errors came from checking out branches despite a conflicting working tree, or pulling without committing or stashing. Models also invented options, such as `--no-edit` during a rebase — [arXiv 2607.09224](https://arxiv.org/html/2607.09224).

### Inferences
- Terminal-Bench rewards an agent that can try a command, read the error and retry. A single-shot Git multiple-choice answer has no such feedback, so a high Terminal-Bench score does not show exact recall. This is my reasoning from the benchmark design.
- The Git-Assistant numbers measure planning against unseen repository state, not recall. They are harsh and should not be read as a Git knowledge score. They do show that models miss Git rules that depend on working-tree state, which is the kind of "small wrong detail" this project cares about.
- The 2.1 gaps between AA and Vals on the same harness name suggest provider, resource or timeout differences. Neither source confirms a cause.
- The change in Vals' Grok 4.7 figure from 12.12 to 28.79 looks like a re-run at a named effort, but Vals does not say so.

### Gaps
- No per-task results were available from AA or Vals, so the five Git-named tasks in 2.x cannot be scored on their own.
- The `legacy` folder has no README confirming that it is the 2.x task set. I infer that from its task names and count (90 entries).
- `hub.harborframework.com` failed DNS resolution from here, so the hub's own task list was not checked. The 66 task folders on GitHub match 4.0's stated task count, and the repository's `dataset.toml` comment still reads "terminal-bench-3".
- Gemini 3.8 Flash's Terminal-Bench 2.1 figure conflicts between sources: Google says 89.4, while one Chinese-language article reports 90.8 — [Inside](https://www.inside.com.tw/article/42285-google-gemini-3-8-flash). I saw that only as a search excerpt and did not resolve it.
- I found no independent run of any model on InterCode-ALFA or NL2SH-ALFA at the versions in scope.

## Question 2: Are there studies of LLMs on GitHub certifications or similar developer exams?

### Takeaway
I found no study of any LLM on GitHub Foundations, Actions, Administration, Advanced Security or Copilot certification questions. The nearest evidence is one strong study on software-testing exams and one on Scrum, and both used earlier models.

### Cited Findings
- GitHub's certification page lists the Foundations, Actions, Advanced Security, Administration and Copilot exams — [GitHub certifications](https://resources.github.com/learn/certifications/). Targeted searches for these exams returned practice-test courses and study guides, not research — for example [Udemy GH-300 practice tests](https://www.udemy.com/course/gh-300-github-copilot-certification-practice-exams/) and [TheServerSide GH-300 post](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/GH-300-GitHub-Copilot-braindump-and-exam-questions).
- **ISTQB software-testing exams (March 2026, older models).** 60 multimodal models answered 1,171 questions from 30 sample exams — [arXiv 2603.23142](https://arxiv.org/abs/2603.23142).
  - Gemini-3-flash-preview scored 1024/1171 (about 87%) and GPT-5-2025-08-07 scored 983/1171 (about 84%). They were the only two to pass all 30 exams — [full paper](https://arxiv.org/html/2603.23142).
  - Claude Opus 4.5 scored 971/1171 and Qwen2.5-VL-72B scored 864/1171 — [full paper](https://arxiv.org/html/2603.23142).
  - gemini-2.5-flash-lite passed 22 of 30 exams, and gemini-2.0-flash-lite passed 24. DeepSeek and Grok were not evaluated. Fifteen questions were missed by all 60 models — [full paper](https://arxiv.org/html/2603.23142).
- **Scrum PSM-aligned questions (June 2026, GPT-5).** On 993 validated questions, all prompts exceeded 85%, and the citation prompt reached 89.1%. Single-answer items were stronger and multi-select items weaker — [arXiv 2607.00049](https://arxiv.org/abs/2607.00049).
- **Professional certifications (2023, old GPT models).** GPT models passed about 39% of broad certifications without fine-tuning. I saw this only as a search excerpt — [arXiv 2305.05377](https://arxiv.org/pdf/2305.05377).
- **Cloud certification (April 2026, vendor blog).** An exam-prep company tried 25 questions per exam. It reports GPT-5 misstating an AWS Lambda limit and quoting a deprecated GCP IAM role. This is a seller's anecdote without a shown method, and I saw only a search excerpt — [ExamCert blog](https://www.examcert.app/blog/chatgpt-vs-claude-vs-gemini-for-certification-study-2026/).
- **GitHub Actions generation (2025, older models).** Six models generated workflows from 1,318 description and YAML pairs taken from GitHub's docs. GPT-4o reached 0.69 cosine similarity but a perfect match in only 3% of cases. Manual review found speculative additions such as an assumed `actions/checkout@v4` step — [arXiv 2507.17165](https://arxiv.org/html/2507.17165v1). This is generation scored by similarity, not an exam.

### Inferences
- The ISTQB study is the best method template for a GitHub test: real exam-style questions, many models and a rewritten-question robustness check.
- A Gemini Flash model doing well in the ISTQB study hints at strength on certification-style questions, but the model and the subject both differ from this project's.

### Gaps
- Nothing covers GitHub certification content on any model, including the models in scope.
- Official GitHub exam questions are not public, and third-party practice sets have unknown accuracy, so a replication would need its own verified question set.
- I found no peer-reviewed study on AWS, Azure, Kubernetes, CompTIA Linux+ or similar developer exams for the models in scope.

## Question 3: What multiple-choice benchmarks cover these models, and what are the scores on a common scale?

### Takeaway
The two standard multiple-choice benchmarks stopped being run just as the newer models arrived. Vals has archived GPQA Diamond and MMLU-Pro, and AA has moved both out of its index. As a result, Grok 4.7, DeepSeek V4.1 Flash 1017 and Gemini 4 Argon have almost no pure multiple-choice data. Gemini 3.8 Flash, Qwen3.8-27B and the Flash-Lite models have the fullest coverage.

### Cited Findings

#### Multiple-choice and mixed scores (percent correct; each column is its own test)

| Model and config | GPQA Diamond: AA | GPQA Diamond: Vals | GPQA Diamond: Epoch | MMLU-Pro: Vals | MMMU-Pro (with images): AA | MMMU-Pro: Vals | HLE: AA, text only | HLE-Diamond: AA (knowledge split) |
|---|---|---|---|---|---|---|---|---|
| Grok 4.7 | No row | Not listed | 93 | Not listed | 78.2 (Low only) | Not listed | 43.1 xhigh | 23.2 xhigh (15.4) |
| Qwen3.8-27B | 90.5 xhigh | 88.89 | No row found | 84.34 | 76.3 xhigh | 83.93 | 33.9 xhigh | 15.3 xhigh (8.6) |
| DeepSeek V4.1 Flash 1017 | No row | Not listed | No 1017 row found (10 Sep snapshot: 90) | Not listed | 80.6 max | Not listed | 43.3 max | 25.3 max (15.8) |
| Gemini 3.8 Flash | 95.3 high | 94.44 | 95 | 90.22 | 85.6 high | 89.08 | 47.8 high | 33.1 high (29.0) |
| Gemini 3.5 Flash-Lite | 83.8 | 83.84 | 83 | 85.84 | 79.0 | 83.58 | 18.8 | 9.9 (not published) |
| Gemini 3.1 Flash-Lite (preview ID) | 82.2 | 81.06 | Not checked | 86.24 | 75.5 | 82.49 | 17.2 | No row |
| Gemini 4 Argon | No row | Not listed | Not on page | Not listed | No row | Not listed | 57.1 high | 56.7 high (48.6) |
| DeepSeek V4 Pro 0813 (reference, no images) | 92.8 max | 92.42 | 92 | 86.97 | Not applicable | Not applicable | 41.0 max | 19.5 max (13.8) |

Sources: [AA GPQA Diamond](https://artificialanalysis.ai/evaluations/gpqa-diamond); [Vals GPQA](https://www.vals.ai/benchmarks/gpqa); [Epoch Grok 4.7](https://epoch.ai/models/grok-4-7), [Epoch Gemini 3.8 Flash](https://epoch.ai/models/gemini-3-8-flash), [Epoch Gemini 3.5 Flash-Lite](https://epoch.ai/models/gemini-3-5-flash-lite), [Epoch V4.1 Flash page](https://epoch.ai/models/deepseek-v4-1-flash) for V4 Pro 0813; [Vals MMLU-Pro](https://www.vals.ai/benchmarks/mmlu_pro); [Vals MMMU-Pro](https://www.vals.ai/benchmarks/mmmu); [AA HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam); [AA HLE-Diamond](https://artificialanalysis.ai/evaluations/hle-diamond). AA's MMMU-Pro rows come from the same embedded page data as its other evaluations.

#### Benchmark status and format
- GPQA Diamond has 198 questions. Vals uses zero-shot chain-of-thought prompting and has archived the benchmark as saturated, with the page last updated on 1 September 2026 — [Vals GPQA](https://www.vals.ai/benchmarks/gpqa). AA removed it from its Index in v4.2 (September 2026) — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).
- MMLU-Pro is a multiple-choice benchmark covering 14 subjects. Vals has archived it, with the page last updated on 1 September 2026. Its top scores are Claude Fable 5.1 at 92.38 and Claude Opus 5 at 91.59 — [Vals MMLU-Pro](https://www.vals.ai/benchmarks/mmlu_pro).
- AA removed MMLU-Pro from its Index in v4.0 (January to June 2026) — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking). AA's MMLU-Pro page shows only older models, led by Gemini 3 Pro Preview at 89.8%, and has no model in scope — [AA MMLU-Pro](https://artificialanalysis.ai/evaluations/mmlu-pro).
- I found no scores for the original MMLU on any model in scope.
- MMMU-Pro is the image-based multiple-choice test: 4 options, about 1,700 questions, 30 subjects. Vals ran it at temperature 0, with about 1% standard deviation, and has archived it, with the page last updated on 1 September 2026 — [Vals MMMU-Pro](https://www.vals.ai/benchmarks/mmmu).
- AA's HLE uses 2,158 text-only questions, scored pass@1 by an LLM equality checker — [AA HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam). HLE mixes multiple-choice and short-answer items — [arXiv 2501.14249](https://arxiv.org/abs/2501.14249). A secondary source puts multiple-choice at 24% — [Wikipedia](https://en.wikipedia.org/wiki/Humanity%27s_Last_Exam). So HLE is not a pure multiple-choice test.
- HLE-Diamond is a refined 1,000-question set: 500 reasoning, 500 knowledge, 272 with images, run without tools — [AA HLE-Diamond](https://artificialanalysis.ai/evaluations/hle-diamond). AA says it is not directly comparable with HLE — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).

#### Other HLE variants that should not be mixed
- For Gemini 3.8 Flash alone there are several published figures: AA HLE 47.8, AA HLE-Diamond 33.1, Scale's board 44.52 ±1.96, Epoch 45, and Google's HLE-Verified 54.9 — [AA HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam); [AA HLE-Diamond](https://artificialanalysis.ai/evaluations/hle-diamond); [Scale leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam); [Epoch](https://epoch.ai/models/gemini-3-8-flash); [Google model card](https://deepmind.google/models/model-cards/gemini-3-8-flash/).
- Scale's board was last updated on 17 September 2026 for its HLE-Rolling fork. It lists no Grok, Qwen or DeepSeek models — [Scale leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam).
- Vendor HLE figures: Qwen3.8-27B 30.8, judged by GPT-4o — [Alibaba card](https://huggingface.co/Qwen/Qwen3.8-27B). V4.1 Flash 1017 42.6, or 44.0 on the text-only subset — [DeepSeek 1017 card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017).
- Vendor GPQA Diamond figures: Qwen3.8-27B 89.2 — [Alibaba card](https://huggingface.co/Qwen/Qwen3.8-27B). V4.1 Flash of 10 September 90.9 — [DeepSeek V4.1 Flash card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash).

#### LiveBench, Epoch and LMArena
- LiveBench 2.0 now describes itself as long-horizon real work such as decks, research reports and bug fixes. The site is a script shell and returned no data here, so I took no scores from it — [LiveBench](https://livebench.ai/). Its description shows no multiple-choice category.
- Epoch's hub says GPQA Diamond is run 16 times per model — [Epoch benchmarks](https://epoch.ai/benchmarks). Its dedicated GPQA page instead describes 198 questions × 8, and shows only Grok 4 from July 2025, at 87% ±2% — [Epoch GPQA Diamond](https://epoch.ai/benchmarks/gpqa-diamond). The newer figures above come from Epoch's per-model pages, which do not name the evaluator or run date.
- Direct requests to the LMArena and Arena leaderboards returned HTTP 403, so no values were taken — [LMArena](https://lmarena.ai/leaderboard/text).

### Inferences
- GPQA Diamond is close to saturated for strong models. On AA, Gemini 3.8 Flash and Qwen3.8-27B differ by under 5 points at their top settings, yet they differ by 33 points on Omniscience accuracy and 52 points on its Software Engineering net score (see Question 4). A high GPQA score alone says little about exact-detail recall.
- AA, Vals and Epoch agree closely on GPQA Diamond for the same model (within about 2 points), so these repeated measurements are trustworthy for that test. AA and Vals differ more on MMMU-Pro, by 3.5 to 7.6 points, which suggests prompt or token-limit differences. Neither source explains this.
- Vals' GPQA and MMLU-Pro pages were last updated on 1 September, which likely explains why models released after that have no row. Gemini 3.8 Flash, released 2 September, does have rows, so the cutoff is approximate.
- AA's GPQA rows stop with models released around early September, matching its removal from the Index in v4.2.
- Ranking gaps widen on HLE-Diamond compared with HLE, but the two tests are not on one scale, so this is only a note about relative order.

### Gaps
- I found no GPQA Diamond result for Gemini 4 Argon or V4.1 Flash 1017 from AA, Vals or Epoch.
- I found no MMLU-Pro result for Grok 4.7, V4.1 Flash 1017 or Gemini 4 Argon.
- I found no MMMU-Pro result for Gemini 4 Argon, or for Grok 4.7 above Low effort.
- Epoch's Qwen 3.8 27B page shows no GPQA Diamond, HLE or SimpleQA Verified row — [Epoch Qwen 3.8 27B](https://epoch.ai/models/qwen-3-8-27b). That page's rows may be incomplete, since it links to fuller results I did not open.
- I could not confirm the 24% multiple-choice share of HLE from a primary source, and it may apply only to the original release.

## Question 4: Which models make things up most often?

### Takeaway
On AA-Omniscience v1.1, DeepSeek V4 Pro and V4.1 Flash 1017 give the most wrong answers, and they attempt the most questions (99.6% and 82.5%). Gemini 4 Argon gives the fewest wrong answers while abstaining on nearly half of questions. Abstaining does not transfer directly to forced-choice multiple-choice questions.

### Cited Findings

#### AA-Omniscience v1.1 (3,000 questions, 6 domains) and SimpleQA Verified

| Model and config | Net score (−100 to 100) | Accuracy % | Hallucination rate % | Attempt rate % | Wrong answers as % of all questions (derived) | Correct share of attempts % (derived) | Software Engineering net score | SimpleQA Verified, Epoch % |
|---|---|---|---|---|---|---|---|---|
| Grok 4.7 xhigh | 31.2 | 42.7 | 20.0 | 55.7 | 11.5 | 76.7 | 41.0 | 56 |
| Qwen3.8-27B xhigh | −6.4 | 17.3 | 28.6 | 42.6 | 23.7 | 40.6 | −20.5 | No row found |
| DeepSeek V4.1 Flash 1017 max | 0.9 | 39.6 | 64.1 | 82.5 | 38.7 | 48.0 | 20.8 | No row (10 Sep snapshot: 43) |
| Gemini 3.8 Flash high | 23.3 | 50.5 | 55.1 | 80.6 | 27.3 | 62.7 | 31.8 | 70 |
| Gemini 3.5 Flash-Lite | 6.9 | 26.5 | 26.7 | Not published | 19.6 | Not available | Not published | No row found |
| Gemini 4 Argon high | 46.1 | 48.3 | 4.3 | 52.4 | 2.2 | 92.1 | 66.5 | 76 |
| DeepSeek V4 Pro 0813 max (reference) | −6.4 | 45.2 | 94.1 | 99.6 | 51.6 | 45.4 | 13.8 | 53 |

Sources: [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience); [Epoch Grok 4.7](https://epoch.ai/models/grok-4-7), [Epoch Gemini 3.8 Flash](https://epoch.ai/models/gemini-3-8-flash), [Epoch Gemini 4 Argon](https://epoch.ai/models/gemini-4-argon), [Epoch V4.1 Flash page](https://epoch.ai/models/deepseek-v4-1-flash). The derived columns use my arithmetic. Wrong share equals hallucination rate × (1 − accuracy), and this reproduces every published net score in the table. Correct share of attempts equals accuracy ÷ attempt rate, with partial answers counted as not correct.

#### How to read these metrics
- AA grades answers as correct, incorrect, partial or not attempted. Net score rewards correct answers, penalises wrong ones and does not penalise refusals — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).
- Hallucination rate is "incorrect / (incorrect + partial answers + not attempted)", so it measures what share of a model's non-correct outcomes were wrong answers rather than abstentions — [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience). A model can lower this rate by refusing more.
- v1.1 launched in October 2026 with 3,000 questions, down from 6,000. It removes 600 public questions, filters saturated ones and fixes errors, and is not directly comparable with v1 — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).
- Old and new figures circulate together. Argon's "15 percent" hallucination rate in The Batch is the v1 figure, while its v1.1 figure is 4.3% — [The Batch](https://www.deeplearning.ai/the-batch/argon-a-low-hallucination-model-build-for-knowledge-work); [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience).
- Epoch runs the 1,000-question SimpleQA Verified, which Google built on OpenAI's SimpleQA. Epoch reports the simple proportion correct, while Google's official score uses an F1-based mean — [Epoch SimpleQA Verified](https://epoch.ai/benchmarks/simpleqa-verified).

#### The closest proxy for exact developer facts
- Omniscience's Software Engineering domain breaks down by language: C, R, Go, PHP, Dart, HTML, Java, Rust, Julia, Swift, Kotlin, Python, JavaScript and TypeScript. It has no Shell, Bash or Git category — [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience).
- Net scores in that domain for Python: Gemini 4 Argon 68.1, Grok 4.7 46.8, Gemini 3.8 Flash 34.0, V4.1 Flash 1017 19.1, V4 Pro 0813 11.7, Qwen3.8-27B −37.2 — [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience).
- Net scores in that domain for JavaScript: Gemini 4 Argon 89.6, Gemini 3.8 Flash 74.6, V4.1 Flash 1017 70.1, Grok 4.7 68.7, V4 Pro 0813 62.7, Qwen3.8-27B 4.5 — [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience).
- Of 37 AA models with this breakdown, the top is Claude Opus 5.5 at 84.7, and Qwen3.8-27B is last at −20.5 — [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience).

#### Confidently wrong answers
- Scale's HLE board reports calibration error: Gemini 3.8 Flash 51, and gemini-3.1-flash-lite-preview 83. Other models in scope are not listed — [Scale leaderboard](https://labs.scale.com/leaderboard/humanitys_last_exam).
- On GPQA, gpt-4.1 reached agreement of at least 0.8 on 77% of cases, and 48% of those high-agreement answers were wrong. This is an audit of an older model — [When LLMs Agree, Are They Right?](https://www.alphaxiv.org/abs/2607.08065.md).

#### Data I did not use
- BenchLM lists V4.1 Flash at −5.3 net, 46.4 accuracy and 96.5 hallucination, sourced to AA — [BenchLM](https://benchlm.ai/md/models/deepseek-v4-1-flash.md). AA's current data has no Omniscience row for that replaced snapshot, so I could not confirm it.

### Inferences
- A wrong answer on Omniscience and a wrong pick on a multiple-choice question are different failures. In forced choice a model cannot abstain, so a high abstention rate only helps if the tool offers an "I don't know" path. The Batch makes the same point about needing a fallback — [The Batch](https://www.deeplearning.ai/the-batch/argon-a-low-hallucination-model-build-for-knowledge-work).
- The derived correct share of attempts is the closest available measure of how much to trust an answer a model chooses to give. It separates a low-coverage, careful pattern (Argon, Grok 4.7) from a high-coverage, guessing pattern (V4 Pro, V4.1 Flash 1017).
- Qwen3.8-27B's low accuracy (17.3%) and negative Software Engineering score are the largest warning sign in this table for exact-detail questions. Note that AA tested it at xhigh, not on Groq.
- Grok 4.7's SimpleQA Verified result (56) is low compared with its Omniscience rank. If it abstains on SimpleQA as it does on Omniscience, this would fit, because Epoch gives no credit for abstaining. I did not verify this.

### Gaps
- There is no SimpleQA Verified row for Qwen3.8-27B, V4.1 Flash 1017 or any Flash-Lite model.
- The classic SimpleQA has no comparable current rows that I found. Respan lists Gemini 3.8 Flash at 69.7 on SimpleQA Verified, but its page returned HTTP 429 and I could not check its source — [Respan](https://www.respan.ai/models/compare/gemini-3-8-flash-vs-grok-4-6).
- Omniscience breakdowns (attempt rate and domains) exist for only 37 models in the AA page data I could read. That set has no Flash-Lite model and no non-reasoning variant of the models in scope.
- No hallucination measure exists for Git or GitHub facts on any model in scope.

## Question 5: What makes LLMs fail on multiple-choice questions, and does it differ by model?

### Takeaway
Research consistently shows that question format changes accuracy, with "select all that apply" and "none of the above" having the largest documented drops. Evidence on "which is NOT" wording is thin, and I found no study isolating "all of the above". Almost none of this was measured on the models in scope.

### Cited Findings

#### Select all that apply
- SATA-Bench (revised October 2025, older models) tested models on multi-answer questions in six domains. The best exact-match score was 41.77% (o3) and the best Jaccard score was 75.23% (GPT-4.1) — [arXiv 2506.00643](https://arxiv.org/html/2506.00643v3).
- Family examples from that paper: Grok 3 Think 39.71, Gemini 2.5 Think 36.46, Gemini 2 Flash 34.60, DeepSeek R1 28.17, Qwen Plus 21.12, non-expert human 17.93 — [arXiv 2506.00643](https://arxiv.org/html/2506.00643v3).
- Nearly all models pick too few answers. The best model got the correct count in only 48% of questions, and all models exceeded a 20% false-positive rate — [arXiv 2506.00643](https://arxiv.org/html/2506.00643v3).
- Multi-select items were also a weak spot for GPT-5 on Scrum questions and in the ISTQB error analysis — [arXiv 2607.00049](https://arxiv.org/abs/2607.00049); [arXiv 2603.23142](https://arxiv.org/html/2603.23142).

#### None of the above and pair options
- On MMLU, 28 models lost 30% to 50% when "none of the above" was the correct answer. The loss was about 14.6% in maths and 48.1% in business ethics (March 2025) — [arXiv 2503.01550](https://arxiv.org/abs/2503.01550).
- In the ISTQB robustness test, the largest drop came from swapping in irrelevant options and adding "none of the above": 12 errors for GPT-5 and 8 for Gemini-3-flash-preview. Overall the two scored 93.6% and 91.5% on 515 rewritten questions — [arXiv 2603.23142](https://arxiv.org/html/2603.23142).
- MMLU-Pro+ (2024) adds "Both X and Y are correct" options. Accuracy fell by 7.5 points for o1-preview, 8.5 for Claude Sonnet 3.5, 9.5 for Llama 3.1 405B, 10.2 for Gemini 1.5 Pro, 11.9 for Qwen2-72B and 14.3 for GPT-4o — [arXiv 2409.02257](https://arxiv.org/html/2409.02257).

#### Negation ("which is NOT", "except")
- The one direct test I found: gpt-3.5-era ChatGPT scored about 6% lower on "except" questions in MedMCQA. The authors called the gap "not that large", and no sample size for this subset is given — [arXiv 2402.14881](https://ar5iv.arxiv.org/html/2402.14881).
- Thunder-NUBench is a negation multiple-choice benchmark, though not a "which is NOT" test. Llama-3.1-8B-Instruct scored about 46% to 54% at zero-shot baseline. Local negation accounted for about 66% to 88% of wrong picks — [arXiv 2506.14397](https://arxiv.org/html/2506.14397v4).
- A 2024 paper says LLaMA-2-chat, Vicuna and Orca-2 "hallucinate considerably" on negation tasks including multiple choice. The abstract gives no figures — [arXiv 2406.05494](https://arxiv.org/abs/2406.05494v1).
- One medical-education table says ChatGPT performed acceptably on negative-phrase questions, which cuts the other way. I saw only that table excerpt — [PMC table](https://pmc.ncbi.nlm.nih.gov/articles/PMC10625095/table/table2).

#### All of the above
- I found no study isolating "all of the above" as an answer option. The closest evidence is the "Both X and Y" work above.
- A position paper lists leakage, unanswerability, shortcuts and saturation as problems of multiple-choice datasets, and recommends rubrics and scoring that discourages guessing — [arXiv 2502.14127](https://arxiv.org/abs/2502.14127).

#### Answer order, letter labels and option length
- "ABCD: All Biases Come Disguised" (February 2026) tested 13 open models on meaningless questions, where chance is 25%. Under standard letter labels some models exceeded 95% median accuracy by exploiting labels and few-shot patterns, and none averaged below about 40% — [arXiv 2602.17445](https://arxiv.org/html/2602.17445).
- On MMLU-Pro in that study, many models peaked on the original answer order, and the proposed fix helped least there (variance ratio 0.99) — [arXiv 2602.17445](https://arxiv.org/html/2602.17445).
- In a GPQA audit, shuffling options reduced accuracy and changed majority answers, and gpt-4.1 under-selected option D — [When LLMs Agree, Are They Right?](https://www.alphaxiv.org/abs/2607.08065.md).
- A Korean-language 100-option study found position bias toward early options under uncertainty — [arXiv 2604.14634](https://arxiv.org/abs/2604.14634).
- Changing only option length moved Qwen 2.5 1.5B on MMLU from 60 to 89 and from 89 to 36. GPT-4o lost about 6 points across all three modification types — [arXiv 2502.12459](https://arxiv.org/abs/2502.12459).

#### Near-duplicate and plausible distractors
- I found no study that directly varies how similar answer options are.
- The ISTQB error analysis names "very similar distractors" and options "too similar to judge" as failure causes — [arXiv 2603.23142](https://arxiv.org/html/2603.23142).
- LEXam kept the same 385 legal questions and raised the option count from 4 to 32. Gemini-2.5-Pro fell from 68.61 to 35.62, and DeepSeek-R1 fell from 57.54 to 24.93 (older models) — [arXiv 2505.12864](https://arxiv.org/html/2505.12864).
- Adding plausible-looking options to MMLU-style questions also lowered accuracy, in adversarial work I saw only as a search excerpt — [arXiv 2502.06738](https://arxiv.org/html/2502.06738v1).

#### Does it differ by model?
- Yes, in every study that reports per-model results, though none covers the versions in scope. In ISTQB rewriting, Gemini-3-flash-preview was more sensitive than GPT-5 to synonym substitution and neutral-sentence additions — [arXiv 2603.23142](https://arxiv.org/html/2603.23142).
- In ABCD, per-model drops under the fix ranged from 12.5% (Ministral-3) to 52% (Nemotron-3-Nano), and Qwen3-30B showed little improvement on some benchmarks — [arXiv 2602.17445](https://arxiv.org/html/2602.17445).
- On MMLU-Pro+, the anchoring effect was most pronounced for GPT-4o and Qwen2-72B-Instruct — [arXiv 2409.02257](https://arxiv.org/html/2409.02257).

### Inferences
- Git and GitHub exam items often combine these traps: near-identical flags, "select two", and negative stems. The worst-case risk for a tool is therefore higher than single-answer benchmark scores suggest. This is my reasoning, not a tested result.
- The evidence that "select all that apply" is hard is the strongest and most consistent here, because three independent studies point the same way.
- Letter-label and order artefacts suggest that shuffling options is a cheap robustness check for any test of these models.

### Gaps
- No study covers negation, "all of the above", near-duplicate distractors or select-all on Grok 4.7, Qwen3.8-27B, V4.1 Flash 1017, Gemini 3.8 Flash, the Flash-Lite models or Gemini 4 Argon.
- I found no study on a modern frontier model of a negated stem like "which is NOT".
- Most failure-mode work uses open or older models and is preprint-level.

## Question 6: Does reasoning effort improve MCQ accuracy, and does asking twice help?

### Takeaway
Turning reasoning on gives large gains. Raising effort further gives small and uneven gains, and on factual recall accuracy barely moves. Asking twice works as a filter rather than a fix: agreement is only a weak signal of correctness, and challenging a model with "are you sure?" tends to make it worse.

### Cited Findings

#### Same model at different effort on AA (percent correct, except net score)

| Model, effort order | GPQA Diamond | HLE | HLE-Diamond | MMMU-Pro | Omniscience accuracy | Omniscience hallucination rate | Omniscience net |
|---|---|---|---|---|---|---|---|
| Gemini 3.8 Flash: Low → Medium → High | 92.0 → 93.5 → 95.3 | 37.1 → 42.1 → 47.8 | 24.3 → 29.1 → 33.1 | 84.5 → 84.2 → 85.6 | 48.3 → 49.6 → 50.5 | 68.1 → 51.5 → 55.1 | 13.0 → 23.7 → 23.3 |
| Grok 4.7: Low → High → Xhigh | No rows | 39.2 → 42.3 → 43.1 | 18.5 → 23.6 → 23.2 | 78.2 at Low only | 45.7 → 41.8 → 42.7 | 33.8 → 20.2 → 20.0 | 27.4 → 30.0 → 31.2 |
| Qwen3.8-27B: None → Low → Medium → Xhigh | 81.8 → 84.5 → 84.5 → 90.5 | 12.1 → 14.0 → 14.1 → 33.9 | 4.2 → 6.8 → 6.7 → 15.3 | 69.9 → 73.8 → 74.2 → 76.3 | 9.1 → 18.3 → 17.9 → 17.3 | 18.0 → 48.7 → 65.4 → 28.6 | −7.3 → −21.5 → −35.9 → −6.4 |
| DeepSeek V4.1 Flash 1017: None → Max | No rows | 11.5 → 43.3 | 7.1 → 25.3 | 69.2 → 80.6 | 21.9 → 39.6 | 25.3 → 64.1 | 2.1 → 0.9 |
| DeepSeek V4 Pro 0813: None → Max | Max only, 92.8 | 10.6 → 41.0 | 7.2 → 19.5 | Not applicable | 38.6 → 45.2 | 93.9 → 94.1 | −19.1 → −6.4 |

Sources: [AA GPQA Diamond](https://artificialanalysis.ai/evaluations/gpqa-diamond); [AA HLE](https://artificialanalysis.ai/evaluations/humanitys-last-exam); [AA HLE-Diamond](https://artificialanalysis.ai/evaluations/hle-diamond); [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience). AA uses temperature 0.6 for reasoning models and temperature 0 for non-reasoning models unless a lab recommends otherwise, and runs Omniscience and HLE-Diamond once — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking). Single runs carry noise, so small steps should not be over-read.

#### Earlier-version pairs on AA (flagged as older)
- GPQA Diamond for Grok 4.3 went from 65.8 without reasoning to 90.1 at High. DeepSeek V4 Pro 0424 went from 71.7 without reasoning to 88.8 at Max — [AA GPQA Diamond](https://artificialanalysis.ai/evaluations/gpqa-diamond).
- More effort can lower the score. DeepSeek V4 Pro 0424 scored 90.5 at High and 88.8 at Max. Grok 4.6 scored 87.9 Low, 93.5 Medium, 95.0 High and 93.5 Xhigh — [AA GPQA Diamond](https://artificialanalysis.ai/evaluations/gpqa-diamond).

#### Published research on effort
- "The Reasoning Tax" (Lenovo, 2026, AA data plus self-run checks, prices as of late May 2026) finds that task structure predicts the value of reasoning better than difficulty. Knowledge-recall tasks such as MMLU-Pro show low value because "additional thinking cannot reliably recover missing facts" — [arXiv 2608.26235](https://arxiv.org/pdf/2608.26235).
- That paper's effort transitions: GPT-5.2 on MMLU-Pro, Medium to Xhigh, +1.5 points. GPT-5.5 on GPQA Diamond, High to Xhigh, +0.3. DeepSeek V4 Pro on GPQA Diamond, High to Max, −1.7. DeepSeek V4 Pro on HLE, High to Max, +2.4 — [arXiv 2608.26235](https://arxiv.org/pdf/2608.26235).
- On NL2Bash, requesting chain-of-thought lowered average task completion from 0.60 to 0.56, and 16 of 22 local models declined. Larger models declined less — [LAST-X paper](https://www.ndss-symposium.org/wp-content/uploads/lastx2026-49.pdf).
- On Git command sequences, a stronger reasoning model (o4-mini) beat GPT-4o in one of two plain-LLM settings (19.0% versus 12.0%) and lost in the other (9.0% versus 12.0%) — [arXiv 2607.09224](https://arxiv.org/html/2607.09224).
- On select-all questions, large reasoning models scored slightly better on Jaccard but did not reduce selection bias. Claude 3.7 Think scored 37.92 exact match against 37.82 without thinking — [arXiv 2506.00643](https://arxiv.org/html/2506.00643v3).
- GPT-5 prompt variants on Scrum questions gave "modest but consistent improvements" — [arXiv 2607.00049](https://arxiv.org/abs/2607.00049).

#### Asking twice and comparing answers
- **Agreement is a weak positive signal.** On GPQA Diamond and AIME, Spearman correlation between self-consistency and majority correctness ranged from about 0.20 to 0.59. The frontier model had the highest agreement and the lowest GPQA correlation (0.20). About 265,000 samples were used, on the gpt-4.1 family, with an exploratory Claude check — [When LLMs Agree, Are They Right?](https://www.alphaxiv.org/abs/2607.08065.md).
- **Agreement across models is not proof.** Confident errors were partly shared between GPT and Claude models in that audit. Stop-when-consensus sampling saved about 60% of samples at similar majority error — [When LLMs Agree, Are They Right?](https://www.alphaxiv.org/abs/2607.08065.md).
- **Filtering to unanimous runs raises accuracy at a coverage cost.** On HotpotQA (200 questions, four models, 8,000 runs), answering only when 3 of 3 runs agree reached 87% to 88% accuracy, a gain of 6 to 14 points, with 54% to 62% coverage — [arXiv 2602.11619](https://arxiv.org/abs/2602.11619).
- **Two calls can forecast voting gains.** Two samples per example on a validation set bound what majority voting can gain, tested on binary tasks — [arXiv 2605.03379](https://arxiv.org/abs/2605.03379).
- **Small models are less stable.** Asked each MMLU-Redux and MedQA question 10 times, 2B to 8B models answered consistently on roughly half to four-fifths of questions, while 50B to 80B models were much more consistent — [arXiv 2509.09705](https://arxiv.org/abs/2509.09705).
- **Abstaining on repetition worked best in one study.** Repetition within sampled outputs outperformed likelihood and self-verification as an abstention basis on ambiguous questions — [arXiv 2305.14613](https://export.arxiv.org/abs/2305.14613).
- **Thinking budget alone is not the most effective use of compute.** On AIME24 with Qwen3-8B, Summary 3x reached 80.00% against 66.67% for plain thinking at the same 24k-token budget, but Self-Consistency 3x gave 63.33% — [arXiv 2512.19585](https://arxiv.org/html/2512.19585). This is maths, not multiple choice.
- **Challenging the model hurts.** "Are you sure?" in the same chat flipped answers about 46% of the time, and accuracy fell by 17% on average across 10 models (2023 to 2024, older models) — [arXiv 2311.08596](https://arxiv.org/abs/2311.08596).
- **Retries help agents, which is a different case.** On the official Terminal-Bench 4.0 board, Grok 4.7 goes from 37.6% on one trial to 48.3% with two tries and 60.6% with five. Gemini 3.8 Flash goes from 19.1% to 28.8% to 43.9% — [tbench.ai leaderboard](https://www.tbench.ai/leaderboard). Those pass@k figures assume a verifier that knows which attempt succeeded, which a multiple-choice tool does not have.

### Inferences
- Exact Git flags and GitHub settings are recall items, so the Omniscience pattern is the most relevant one here: going from low to high effort barely changes accuracy for Gemini 3.8 Flash, Grok 4.7 and Qwen3.8-27B. Effort may matter more for scenario questions that require working through repository state.
- Turning reasoning on can raise right and wrong answers together on factual recall. V4.1 Flash 1017 gains 17.7 points of Omniscience accuracy, but its hallucination rate rises from 25.3% to 64.1% and its net score does not improve.
- Qwen3.8-27B's gains on HLE and GPQA appear mostly at Xhigh. Low and Medium sit near the non-reasoning level on HLE. If Groq's `high` behaves more like Medium than Xhigh, Groq-hosted results could fall well short of AA's Xhigh row. That is untested.
- With only two calls there is no majority, so comparing them gives a yes-or-no agreement flag. Its value is routing disagreements to a stronger model or to "unsure", not improving the answer. The evidence above supports this use only weakly on multiple-choice questions, and shows it can miss repeated confident errors.
- Re-asking with shuffled options may be a stronger check than repeating the same prompt, since part of the agreement on GPQA is positional. No study I found tests this directly on the models in scope.

### Gaps
- No effort-level multiple-choice data exists on Groq-hosted Qwen3.8-27B, and AA has no row at `high` for it.
- AA has only None and Max for DeepSeek V4.1 Flash 1017, so intermediate effort is unknown.
- Gemini 4 Argon has a High row only on AA, so effort sensitivity is unknown.
- AA's Grok 4.7 lacks GPQA rows and has an MMMU-Pro row only at Low.
- Pure multiple-choice data at multiple effort levels exists mainly for Gemini 3.8 Flash and Qwen3.8-27B.
- I found no study of asking twice on any model in scope, and no study of it on Git or GitHub questions.

## Question 7: What evidence is missing?

### Takeaway
Nothing tests Git multiple-choice questions on these exact models, and I found no test of GitHub feature knowledge on them either. Every conclusion about Git or GitHub accuracy must be inferred from proxies.

### Cited Findings

#### Evidence strength by topic

| Topic | Best available evidence | Strength for this project |
|---|---|---|
| Git and GitHub MCQ accuracy on models in scope | None found | None |
| Git command accuracy on any model | [Git-Assistant](https://arxiv.org/html/2607.09224), [GitGoodBench](https://arxiv.org/abs/2505.22583) | Weak: older models, not multiple choice |
| Shell command generation | [LAST-X NL2Bash](https://www.ndss-symposium.org/wp-content/uploads/lastx2026-49.pdf) | Weak: small open models only |
| Terminal agent ability on models in scope | [Official board](https://www.tbench.ai/leaderboard), [AA](https://artificialanalysis.ai/evaluations/terminalbench-4-0), [Vals](https://www.vals.ai/benchmarks/terminal-bench-4) | Strong as measurement, weak as a proxy: no Git tasks in 4.0 |
| General MCQ accuracy | [AA GPQA](https://artificialanalysis.ai/evaluations/gpqa-diamond), [Vals GPQA](https://www.vals.ai/benchmarks/gpqa), [Vals MMLU-Pro](https://www.vals.ai/benchmarks/mmlu_pro), [Vals MMMU-Pro](https://www.vals.ai/benchmarks/mmmu) | Strong for Gemini 3.8 Flash and Qwen3.8-27B; partial for Grok 4.7 and V4.1 Flash 1017; very thin for Gemini 4 Argon |
| Factual recall and hallucination | [AA-Omniscience v1.1](https://artificialanalysis.ai/evaluations/omniscience), [Epoch SimpleQA Verified](https://epoch.ai/benchmarks/simpleqa-verified) | Strong and independent; the Software Engineering domain is the nearest proxy |
| MCQ wording traps | Papers cited in Question 5 | Moderate in general, none on models in scope |
| Effort effects | AA same-model rows, [Reasoning Tax](https://arxiv.org/pdf/2608.26235) | Strong within AA's configs, none on Groq |
| Asking twice | Papers cited in Question 6 | Moderate in general, none on models in scope |

#### Pages that could not be reached or gave no data
- LMArena and Arena leaderboards returned HTTP 403 — [LMArena](https://lmarena.ai/leaderboard/text).
- LiveBench returned only a script shell with no scores — [LiveBench](https://livebench.ai/).
- Respan returned HTTP 429 — [Respan](https://www.respan.ai/models/compare/gemini-3-8-flash-vs-grok-4-6).
- The Harbor task hub failed DNS resolution, so I used the GitHub repository instead — [repository](https://github.com/harbor-framework/terminal-bench).
- Epoch's dedicated SimpleQA Verified and GPQA Diamond pages show no scores for the models in scope, so those values come from per-model pages — [Epoch SimpleQA Verified](https://epoch.ai/benchmarks/simpleqa-verified); [Epoch GPQA Diamond](https://epoch.ai/benchmarks/gpqa-diamond).
- No figure in these notes comes from a guess about an unreachable page.

#### Scale warning for index figures
- AA's Intelligence Index changed composition in v5.0 (October 2026) — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking). An article quoting Qwen3.8-27B at 52 predates that version — [Let's Data Science](https://letsdatascience.com/news/qwen38-27b-reaches-52-on-artificial-analysis-intelligence-in-228acf1c). On v5.0 it reads 20.1 at Xhigh — [AA model page](https://artificialanalysis.ai/models/qwen3-8-27b). Likewise, The Batch reported Argon at 53 on 9 October, and it now reads 50.4 on v5.0 — [The Batch](https://www.deeplearning.ai/the-batch/argon-a-low-hallucination-model-build-for-knowledge-work); [AA model page](https://artificialanalysis.ai/models/gemini-4-argon).

### Inferences
- A small first-party test is the only way to close the main gap: verified Git and GitHub multiple-choice questions, run on the exact API routes and effort settings the tool will use, with shuffled options.
- Such a test would need to cover the Groq route specifically, because no accuracy figure in these notes was measured there, as far as any source states.
- Knowledge cutoffs will matter for GitHub features that change often. Gemini 3.8 Flash's is March 2026 — [Google model card](https://deepmind.google/models/model-cards/gemini-3-8-flash/). I did not collect cutoffs for the other models.

### Gaps
- **Git MCQs:** no test on any model in scope.
- **GitHub certifications:** no study on any model at all.
- **GitHub features:** nothing found on Actions, branch protection, pull requests, Codespaces, CODEOWNERS or the `gh` CLI as knowledge questions. The one Actions study tests workflow generation on older models.
- **Shell knowledge:** NL2Bash studies exist, but none covers the models in scope. I found no flag-level recall exam.
- **Pure MCQ scores:** missing for Gemini 4 Argon, and sparse for Grok 4.7 and V4.1 Flash 1017, because the main benchmarks were archived.
- **Groq:** no accuracy data at all on `qwen/qwen3.8-27b`, and Groq's 16,384-token output cap may limit long reasoning. That effect is untested.
- **Flash-Lite:** no Omniscience attempt rate or domain breakdown, no official Terminal-Bench row, and the 3.1 AA row is keyed to a shut-down preview ID. No text-capable 3.8 Flash-Lite is listed.
- **Image-based technical MCQs:** MMMU-Pro is the only image multiple-choice benchmark here, and it is academic. Nothing tests screenshots of Git, GitHub or terminal output.
- **Wording traps:** no measurement on the models in scope.
- **Run dates:** AA, and Epoch's model pages, give no per-row run dates, so it is unknown exactly when each row was measured or whether a model was updated since.
