# Screenshot reading and on-screen pointing: grok-4.7, Qwen3.8-27B, DeepSeek V4.1 Flash, Gemini models (state as of 2026-11-01)

## 1. What do multimodal benchmarks show for these models?

### Takeaway
Three boards hold several of these models under one method: Artificial Analysis (AA) MMMU-Pro, Arena Vision and Roboflow Vision Evals. None of them tests browser screenshots, they measure different things, and coverage has holes: Gemini 4 Argon appears only on Roboflow, and Roboflow has no DeepSeek V4.1 Flash row.

### Cited Findings

**Evidence labels used in these notes.** [Independent] = run by a party that did not build the model. [Vendor] = the model's maker reported it. [Mirror] = a third-party copy of another board. [Predecessor] = an earlier model, not the one asked about. [Snippet] = seen only in a search result; the page was not opened.

**Model identity and revisions**
- `grok-4.7`: released 21 Sep 2026; effort levels low, medium, high (default), xhigh; knowledge cutoff May 2026 — [launch post](https://x.ai/news/grok-4-7); [developer guide](https://docs.x.ai/developers/grok-4-7).
- `qwen/qwen3.8-27b` on Groq: status "Preview"; `reasoning_effort` is `default`, `none`, `low`, `medium` or `high` — [Groq model page](https://console.groq.com/docs/model/qwen/qwen3.8-27b). AA dates the release 2026-08-14 — [AA](https://artificialanalysis.ai/evaluations/mmmu-pro).
- `deepseek-flash` is "now served by DeepSeek-V4.1-Flash-1017" — [DeepSeek](https://api-docs.deepseek.com/news/v4-1-flash). Boards differ on revision: Arena's row is DeepSeek-V4.1-Flash-20260910, an earlier revision — [Arena](https://arena.ai/leaderboard/vision).
- `gemini-3.8-flash`: stable; card published 2 Sep 2026; thinking levels low, medium, high; "`minimal` is not supported and returns an error" — [model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash); [card](https://deepmind.google/models/model-cards/gemini-3-8-flash/).
- Flash-Lite: `gemini-3.5-flash-lite` (stable, 21 Jul 2026), `gemini-3.1-flash-lite` (stable, card 3 Mar 2026), `gemini-2.5-flash-lite` (legacy, limited access) — [Gemini models list](https://ai.google.dev/gemini-api/docs/models); [3.5 card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/); [3.1 card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite/).
- `gemini-4-argon`: stable; card published 13 Oct 2026 — [model page](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon); [card](https://deepmind.google/models/model-cards/gemini-4-argon/). AA gives 2026-09-30 as its release date, which does not match the card date — [AA](https://artificialanalysis.ai/evaluations/mmmu-pro).

**AA MMMU-Pro** [Independent]. Setup: 1,730 questions, 10-option multiple choice, regex extraction, pass@1, no tools, 1 repeat, not part of Intelligence Index v5.0 — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking). AA's benchmark page gives no version or evaluation date, and it says 3,460 questions where the methodology says 1,730 — [AA MMMU-Pro](https://artificialanalysis.ai/evaluations/mmmu-pro). "AA page" below means the value was read from that page's embedded chart data on 2026-11-01; that data holds only 27 charted configurations. No separate AA vision index was found: Intelligence Index v5.0 is described as nine text-oriented evaluations — [AA Argon page](https://artificialanalysis.ai/models/gemini-4-argon).

| Model and setting | Score | Provenance |
|---|---|---|
| Gemini 3.8 Flash, High | 85.61 | [AA page](https://artificialanalysis.ai/evaluations/mmmu-pro) |
| Gemini 3.8 Flash, Low | 84.5 | [Mirror: LLMLearner](https://llmlearner.com/rankings/mmmu-pro) |
| Gemini 3.8 Flash, Medium | 84.2 | [Mirror: LLMLearner](https://llmlearner.com/rankings/mmmu-pro) |
| DeepSeek V4.1 Flash 1017, Max | 80.64 | [AA page](https://artificialanalysis.ai/evaluations/mmmu-pro) |
| Gemini 3.5 Flash-Lite, thinking (level not given) | 79.0 | [Mirror: LLMLearner](https://llmlearner.com/rankings/mmmu-pro); [BenchGecko](https://benchgecko.ai/benchmark/aa-mmmu-pro) |
| Grok 4.7, Low | 78.2 | [Mirror: LLMLearner](https://llmlearner.com/rankings/mmmu-pro) only |
| DeepSeek V4.1 Flash (earlier revision), Max | 77.0 | [Mirror: LLMLearner](https://llmlearner.com/rankings/mmmu-pro); [BenchGecko](https://benchgecko.ai/benchmark/aa-mmmu-pro) |
| Qwen3.8 27B, Xhigh | 76.30 | [AA page](https://artificialanalysis.ai/evaluations/mmmu-pro) |
| Qwen3.8 27B, Medium / Low / Normal | 74.2 / 73.8 / 69.9 | [Mirror: LLMLearner](https://llmlearner.com/rankings/mmmu-pro) |
| Gemini 3.1 Flash-Lite, thinking (level not given) | 75.5 | [Mirror: LLMLearner](https://llmlearner.com/rankings/mmmu-pro) |
| Gemini 4 Argon | No score found | AA's model page lists MMMU-Pro with no value shown — [AA](https://artificialanalysis.ai/models/gemini-4-argon) |

Cautions on this table:
- The Grok 4.7 row is weak. AA's embedded data lists Grok 4.7 Low, High and Xhigh as selectable but holds no score for them — [AA](https://artificialanalysis.ai/evaluations/mmmu-pro). LLMLearner says its AA data was read on 2026-09-14, a week before Grok 4.7 existed, so that date note cannot apply to this row — [LLMLearner](https://llmlearner.com/rankings/mmmu-pro). BenchGecko has no Grok 4.7 row — [BenchGecko](https://benchgecko.ai/benchmark/aa-mmmu-pro).
- Same-model conflict: Google reports 76.8% for Gemini 3.1 Flash-Lite (High) [Vendor, Mar 2026] against 75.5 above — [card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite/).
- Different settings, not on this scale: DeepSeek's card gives V4.1-Flash-Base 56.5 (MMMU-Pro, EM metric, 4-shot, base model) — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash). A Moonshot table gives 82.5 for the 1017 revision with tools, seen through a mirror — [LLMLearner](https://llmlearner.com/rankings/mmmu-pro).
- BenchGecko's FAQ says its scores come from "Epoch AI or the model provider", which does not fit an AA board, so its sourcing statement is unreliable — [BenchGecko](https://benchgecko.ai/benchmark/aa-mmmu-pro).
- MMMU-Pro background [Predecessor models, 2024–2025]: a "vision-only input setting where questions are embedded within images" exists, performance across models was 16.8% to 26.9% lower than on MMMU, and OCR prompts had minimal effect — [paper](https://arxiv.org/abs/2409.02813). The dataset has three configs of 1.73k rows each: standard (10 options), standard (4 options), vision — [HF dataset](https://huggingface.co/datasets/MMMU/MMMU_Pro).

**Arena Vision** [Independent, human preference votes, official board, last updated 19 Oct 2026] — [Arena](https://arena.ai/leaderboard/vision). This measures which answer people prefer, not accuracy.

| Rank | Model as listed | Score | Votes |
|---|---|---|---|
| 12 | Gemini 3.8 Flash (High) | 1291±10, marked Preliminary | 4,645 |
| 38 | Gemini 3.5 Flash-Lite | 1267±8 | 9,238 |
| 46 | DeepSeek-V4.1-Flash-20260910 (Max) | 1261±10 | 4,100 |
| 56 | Grok 4.7 (xHigh) | 1250±11 | 3,736 |
| 63 | Qwen3.8-27B | 1242±8 | 7,614 |
| 70 | Gemini 3.1 Flash-Lite Preview | 1235±6 | 27,657 |

Gemini 4 Argon has no row in ranks 1–159, the portion retrieved. Mirrors disagree with this board (for example [Metatext](https://metatext.io/benchmarks/lmarena-vision) shows Gemini 3.8 Flash at 1315), so these notes use only the official values.

**Roboflow Vision Evals** [Independent of the model makers; Roboflow sells vision tooling]. Snapshot 26 Oct 2026, 65 models, low-effort pass, 3 runs per task except OCR (1 run, preliminary). Object detection is scored by mAP@50, OCR deterministically, and counting, identification and reasoning by Gemini 3.5 Flash acting as judge. The overall score is an unweighted mean — [Vision Evals](https://playground.roboflow.com/evals).

| Model | Overall (rank of 65) | Detection | Counting | Identification | OCR | Reasoning |
|---|---|---|---|---|---|---|
| Gemini 4 Argon | 87.5 (#1) | 82.5 | 86.0 | 93.8 | 85.7 | 89.4 |
| Gemini 3.8 Flash | 79.8 (#8) | 68.1 | 78.8 | 97.9 | 72.8 | 81.2 |
| Qwen3.8 27B | 69.5 (#24), 4 of 5 tasks | 65.7 | 64.9 | 85.4 | none | 62.0 |
| Grok 4.7 | 63.5 (#33) | 40.4 | 61.7 | 87.5 | 63.6 | 64.2 |
| Gemini 3.5 Flash-Lite | 61.7 (#35) | 57.5 | 52.7 | 84.4 | 65.8 | 48.3 |
| DeepSeek V4 Flash Vision Exp [Predecessor] | 47.2 (#60) | 45.3 | 46.0 | 68.8 | 44.0 | 31.8 |

Roboflow has no Gemini 3.1 Flash-Lite row and no DeepSeek V4.1 Flash row — [Vision Evals](https://playground.roboflow.com/evals). Its Qwen3.8 27B runs are self-hosted, not on Groq; the overall score was 69.5 at BF16, 68.7 at FP8 and 69.5 at AWQ-INT4 — [comparison page](https://playground.roboflow.com/models/compare/gemini-3-8-flash-vs-qwen3-8-27b).

**Vision results in model cards** [Vendor]. Each row is the maker's own setup; do not line these up across models.

| Model | Card date | Benchmark and setting | Score |
|---|---|---|---|
| Gemini 4 Argon | Oct 2026 | Chartography; LVBench | 71.6%; 91.7% — [card](https://deepmind.google/models/model-cards/gemini-4-argon/) |
| Gemini 3.8 Flash | Sep 2026 | CharXiv Reasoning, no tools; LVBench agentic; GDP.PDF all-pass | 86.2%; 87.8%; 35.0% — [card](https://deepmind.google/models/model-cards/gemini-3-8-flash/) |
| Gemini 3.5 Flash-Lite | Jul 2026 | CharXiv Reasoning, no tools; with tools | 74.5%; 76.5% — [card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) |
| Gemini 3.1 Flash-Lite | Mar 2026 | MMMU-Pro (High); CharXiv Reasoning; Video-MMMU | 76.8%; 73.2%; 84.8% — [card](https://deepmind.google/models/model-cards/gemini-3-1-flash-lite/) |
| Qwen3.8-27B | Aug 2026 | MathVision without/with CI; BabyVision without/with CI; CharXiv (RQ) without/with CI; RealWorldQA | 90.0/94.6; 65.7/85.6; 83.7/90.2; 85.9 — [HF card](https://huggingface.co/Qwen/Qwen3.8-27B) |
| DeepSeek V4.1 Flash | Undated (2026); revision not stated | Instruct, max effort, Claude Code harness, 512k context: Chartography w/ tools Pass@1; BabyVision w/ tools Pass@1; ZeroBench-main w/ tools Pass@5 | 78.9; 89.6; 49.0 — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) |
| DeepSeek V4.1 Flash | Same | Base model: CVBench (EM) 4-shot; DocVQA (LLM-Judge) 4-shot | 77.9; 95.6 — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) |
| Grok 4.7 | Sep 2026 | No vision benchmark. The card calls it "primarily a text model" that accepts text and images | None — [card](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf); [launch post](https://x.ai/news/grok-4-7) |

### Inferences
- MMMU-Pro is the closest public proxy for "answer a multiple-choice question from an image", but its content is academic figures, not rendered web pages. It says little about small interface text.
- Reasoning setting moves these numbers. Qwen3.8 27B spans 69.9 to 76.3 by setting. Groq's list of efforts has no "xhigh", so AA's best Qwen figure may not be reachable on Groq.
- Roboflow's three LLM-judged tasks use a Google model as judge. That is a possible bias for the Gemini rows; the size of any effect is unknown.

### Gaps
- No plain MMMU score was found for any target model.
- No board was confirmed to have tested Groq's hosted Qwen3.8-27B. AA does not name its provider for the Xhigh run in the data retrieved.
- AA does not say whether it uses MMMU-Pro's vision-only config, which is the one that resembles this user's input.
- Medical and licensing-exam studies report accuracy drops on image-based questions, but they test image interpretation, not text rendered as an image, and none covers these models [Snippet] — [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0317423); [BMC Medical Education](https://link.springer.com/article/10.1186/s12909-025-08542-4). No study was found that compares the same question as text and as a whole-screen screenshot.

## 2. How accurately do they read text in screenshots, including small UI text and code? Any OCR or document-reading benchmark covering these models?

### Takeaway
No benchmark found tests small UI text or code in browser screenshots on any of these models. The nearest evidence is Roboflow's OCR task, which uses real-world images and is preliminary, and ParseBench, which uses enterprise PDF pages. Grok 4.7 has Roboflow data only, and Qwen3.8-27B has ParseBench and a vendor score but no Roboflow OCR row.

### Cited Findings

**Roboflow OCR** [Independent, preliminary, 1 run per model, snapshot 26 Oct 2026]. Image types listed: meters, digital displays, shipping labels, tickets, forms, passports, comics, technical drawings. Screenshots, UI and code are not listed. Single value needs an exact match; transcription uses character similarity; text localization needs a box overlapping the ground truth by more than half and exactly matching text — [OCR eval](https://playground.roboflow.com/evals/ocr).

| Model | Effort | OCR overall | Single value | Transcription | Structured JSON | Text localization |
|---|---|---|---|---|---|---|
| Gemini 4 Argon | High | 88.0 | 80.0 | 98.8 | 94.8 | 84.7 |
| Gemini 4 Argon | Low | 85.7 | 78.3 | 95.5 | 92.6 | 81.5 |
| Gemini 3.8 Flash | High | 78.7 | 70.9 | 94.1 | 90.9 | 58.6 |
| Gemini 3.8 Flash | Low | 72.8 | 73.5 | 91.3 | 86.1 | 26.4 |
| Gemini 3.5 Flash-Lite | High | 71.2 | 66.1 | 88.6 | 82.1 | 46.4 |
| Gemini 3.5 Flash-Lite | Low | 65.8 | 64.3 | 87.5 | 75.8 | 31.9 |
| Grok 4.7 | Low | 63.6 | 54.4 | 89.5 | 86.4 | 14.8 |
| DeepSeek V4 Flash Vision Exp [Predecessor] | High | 44.7 | 34.8 | 69.3 | 64.3 | 6.1 |
| DeepSeek V4 Flash Vision Exp [Predecessor] | Low | 44.0 | 34.4 | 65.2 | 64.9 | 3.4 |
| Qwen3.6 27B [Predecessor] | High | 59.8 | not retrieved | 80.9 | not retrieved | 36.8 |
| Qwen3.5-27B [Predecessor] | High | 61.7 | not retrieved | 86.1 | not retrieved | 40.3 |

No OCR row exists for Qwen3.8 27B, Gemini 3.1 Flash-Lite or DeepSeek V4.1 Flash, and no high-effort row for Grok 4.7 — [OCR eval](https://playground.roboflow.com/evals/ocr). Cost of effort: Gemini 3.8 Flash used 2.2K tokens and 12.60 s per sample at low effort, and 10.5K tokens and 79.76 s at high effort — [OCR eval](https://playground.roboflow.com/evals/ocr).

**ParseBench** [Run by LlamaIndex, whose LlamaParse products lead the board, so treat as interested]. Enterprise PDF documents, 500 pages — [repo](https://github.com/run-llama/ParseBench). Values below are from [leaderboard.csv](https://raw.githubusercontent.com/run-llama/ParseBench/main/leaderboard.csv); the file's latest commit is dated 2026-10-28 ([commit history](https://api.github.com/repos/run-llama/ParseBench/commits?path=leaderboard.csv&per_page=3)). The repo does not say whether scanned or screenshot pages are included.

| Row as listed | Overall | Content faithfulness | Semantic formatting | Tables | Charts | Visual grounding |
|---|---|---|---|---|---|---|
| Gemini 3.8 Flash (Thinking High) | 71.50 | 89.68 | 76.36 | 89.12 | 32.34 | 70.01 |
| Gemini 3.8 Flash (Thinking Medium) | 69.90 | 88.42 | 71.8 | 89.08 | 32.72 | 67.46 |
| Gemini 3.8 Flash (Thinking Low) | 69.32 | 88.25 | 66.99 | 88.18 | 35.09 | 68.08 |
| Qwen 3.8 27B (Thinking) | 69.72 | 88.28 | 59.77 | 66.82 | 69.17 | 64.56 |
| Qwen 3.8 27B | 60.30 | 86.57 | 55.29 | 84.52 | 16.59 | 58.53 |
| DeepSeek V4.1 Flash (Thinking High) | 64.56 | 87.33 | 73.48 | 82.82 | 51.11 | 28.04 |
| DeepSeek V4.1 Flash (No Thinking) | 55.20 | 88.09 | 66.05 | 79.65 | 20.46 | 21.75 |
| Gemini 3.5 Flash Lite (Thinking High) | 59.66 | 86.85 | 54.03 | 83.31 | 19.27 | 54.85 |
| Gemini 3.5 Flash Lite | 55.50 | 82.22 | 57.74 | 73.48 | 6.26 | 57.81 |
| Gemini 3.5 Flash Lite (Thinking Medium) | 52.22 | 78.8 | 48.05 | 72.85 | 6.23 | 55.18 |
| Gemini 3.1 Flash Lite | 58.32 | 89.46 | 58.38 | 85.48 | 9.92 | 48.38 |
| Gemini 3.1 Flash Lite (Thinking Medium) | 56.83 | 87.67 | 56.17 | 83.43 | 14.35 | 42.52 |
| Gemini 3.1 Flash Lite (Thinking High) | 56.28 | 83.28 | 56.61 | 76.76 | 30.89 | 33.84 |

There is no Grok row and no Gemini 4 Argon row in the file — [leaderboard.csv](https://raw.githubusercontent.com/run-llama/ParseBench/main/leaderboard.csv). Conflicts: DeepSeek's card lists a ParseBench mean of 56.57 against the CSV's 55.20, though the text figures match — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash). Kaggle's ParseBench board shows Gemini 3.8 Flash at 67.8%, 12th, updated 9 Oct 2026 [Snippet] — [Kaggle](https://www.kaggle.com/benchmarks/llamaindex-org/parsebench).

**Other reading evidence**
- OmniDocBench 1.5: Qwen3.8-27B 91.1, Qwen3.6-27B 89.4 [Vendor, Aug 2026]. No other target model is in that table — [HF card](https://huggingface.co/Qwen/Qwen3.8-27B).
- OCRBench on LLM-Stats: 24 entries, all self-reported. No Gemini or Grok, and DeepSeek appears only as VL2 models. Qwen3.5-27B and Qwen3.6-27B are 0.894 [Predecessor]; Qwen3.8-27B is absent — [LLM-Stats](https://llm-stats.com/benchmarks/ocrbench).
- DeepSeek-V4-Flash-Vision-Exp scored 835/1000 on OCRBench in a vLLM Recipes run, with images capped at about 387 tokens [Predecessor, pre-release recipe] — [vLLM Recipes](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp).
- DeepSeek's guide names "reading text from screenshots" as an example use and makes no accuracy claim — [Vision guide](https://api-docs.deepseek.com/guides/vision).
- Google states that higher resolutions improve "the model's ability to read fine text or identify small details", without figures — [image understanding](https://ai.google.dev/gemini-api/docs/image-understanding).
- A hands-on post using 4-bit quantized Qwen3.8-27B reports that very small or low-contrast text is a weakness. It has no ground-truth scoring and no UI tests, dated 4 Oct 2026 — [LearnOpenCV](https://learnopencv.com/qwen3-8-27b-computer-vision/).
- One reviewer of the older vision-exp model says fine chart labels can be lost on resizing [Predecessor, 384-token cap] — [IntuitionLabs](https://intuitionlabs.ai/articles/deepseek-v4-flash-vision-document-understanding).

**Code** [Predecessor only]
- CodeOCR (Feb 2026) tested Gemini-3-Flash, Gemini-3-Pro, Gemini-2.5-Pro, Qwen-3-VL 235B, GPT-5-mini, GPT-5.1 and GLM-4.6v. At 8× compression Gemini-3 kept high CodeBLEU in code reconstruction while other models hit a "performance cliff". Early errors were token-level, such as 1 vs l and 0 vs O. Base font size was 40 px with no font-size sweep — [CodeOCR](https://arxiv.org/html/2602.01785v1).
- A July 2026 study of input-token accounting found Gemini image costs were non-monotonic across a page boundary. It did not measure reading accuracy — [Pixels for Programs?](https://arxiv.org/abs/2607.21672).

### Inferences
- Among the current target models on Roboflow, plain transcription is close (87.5 to 98.8), while exact-match single values spread more widely (54.4 to 80.0). A quiz that depends on one exact token, such as `1` vs `l` in code, sits nearer the exact-match case. This is an analogy, not a measurement.
- ParseBench Content Faithfulness is tightly grouped for all but one configuration (about 82 to 90; Gemini 3.5 Flash Lite at Thinking Medium is 78.8), so it separates these models less than Visual Grounding does.
- More thinking does not always help reading. Gemini 3.1 Flash Lite's overall, content and grounding scores all fall from its default row to Thinking High.

### Gaps
- No evidence was found on any target model for small interface text (for example 12 to 14 px), syntax-highlighted code, dark themes, or JPEG compression artifacts.
- A paper titled "Do multimodal LLMs understand programming screenshots?" appeared in search but was not read — [listing](https://eurekamag.com/research/105/243/105243922.php).
- Roboflow's DeepSeek row is the retired vision-exp model. DeepSeek now routes that name to the Flash model, so it is unclear which model produced those runs — [DeepSeek](https://api-docs.deepseek.com/news/v4-1-flash).

## 3. How accurately can each model locate UI elements? Which models document coordinate output, in what format, and with what accuracy?

### Takeaway
Only Gemini documents coordinate output. Qwen has a family convention that the Qwen3.8-27B card and Groq's docs do not state, and DeepSeek and xAI document nothing. No target model has a ScreenSpot-Pro score, and the only target model in independent screenshot-pointing tests is Gemini 3.1 Flash-Lite. Other localization data comes from vendor-reported agent benchmarks and from non-UI tests.

### Cited Findings

**Documented coordinate output**

| Model | Documented format | Published pointing accuracy from the provider |
|---|---|---|
| Gemini (image understanding) | `box_2d` as [ymin, xmin, ymax, xmax], relative to image dimensions, scaled to 0–1000; descale using the original size. Segmentation masks use polygon [x, y] on the same scale — [docs](https://ai.google.dev/gemini-api/docs/image-understanding) | None found |
| Gemini (Computer Use tool) | Action tables say x and y are integers 0–999; the execution code describes normalized 1000×1000 and divides by 1000, so the page is inconsistent — [docs](https://ai.google.dev/gemini-api/docs/computer-use) | None found |
| Qwen3.8-27B | Not stated on the [HF card](https://huggingface.co/Qwen/Qwen3.8-27B), [GitHub README](https://github.com/QwenLM/Qwen3.8) or [Groq docs](https://console.groq.com/docs/vision) | None found |
| DeepSeek `deepseek-flash` | Not mentioned in the [Vision guide](https://api-docs.deepseek.com/guides/vision); not described on the [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | Base model only: RefCOCO-avg Acc@0.5, 0-shot, 86.0 [Vendor] — [HF card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) |
| Grok 4.7 | Not stated — [image understanding](https://docs.x.ai/developers/model-capabilities/images/understanding); [developer guide](https://docs.x.ai/developers/grok-4-7) | None found |

Qwen family convention, from sources other than the 3.8-27B documentation:
- Roboflow, testing Qwen3.8-Max: "Qwen models work best with XYXY coordinates normalized to a range from 0 to 1000". A search excerpt of the same post adds that changing order, scale or response structure often lowers detection [Snippet for that second point] — [Roboflow](https://roboflow.com/blog/qwen3-8-max).
- Qwen's Qwen3-VL computer-use cookbook says "The screen's resolution is 1000x1000" and divides by 1000 in code [Predecessor] — [cookbook](https://raw.githubusercontent.com/QwenLM/Qwen3-VL/main/cookbooks/computer_use.ipynb).
- A Qwen3.8-27B guide asks for pixels, then notes the outputs are 0–1000 and need rescaling, and does not reconcile the two — [LearnOpenCV](https://learnopencv.com/qwen3-8-27b-computer-vision/).

Gemini prompt notes:
- With a single image, Google advises placing the text prompt before the image — [image understanding](https://ai.google.dev/gemini-api/docs/image-understanding).
- The same page advises `minimal` thinking for segmentation only, but `gemini-3.8-flash` rejects `minimal` with an error, so the two pages conflict for that model — [image understanding](https://ai.google.dev/gemini-api/docs/image-understanding); [model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash).

**Agentic computer use** [All Vendor]. These are multi-step task scores. They do not isolate pointing accuracy.

| Benchmark, version, metric | Model | Score | Reported by, date |
|---|---|---|---|
| OSWorld-Verified | Qwen3.8-27B | 84.3 | Alibaba, Aug 2026 — [HF card](https://huggingface.co/Qwen/Qwen3.8-27B) |
| OSWorld-Verified | Gemini 3.5 Flash-Lite | 74.0% | Google, Jul 2026 — [card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) |
| OSWorld-Verified | Gemini 3.1 Flash-Lite | 54.3% | Google, Jul 2026 — [card](https://deepmind.google/models/model-cards/gemini-3-5-flash-lite/) |
| OSWorld-2.0, partial score, batch tool enabled | Gemini 3.8 Flash | 59.0% | Google, Sep 2026 — [card](https://deepmind.google/models/model-cards/gemini-3-8-flash/) |
| OSWorld-2.0, offline subset, partial score | Gemini 4 Argon | 69.2% | Google, Oct 2026 — [card](https://deepmind.google/models/model-cards/gemini-4-argon/) |
| Agent's Last Exam, pass rate | Gemini 4 Argon | 39.5% | Google, Oct 2026 — [card](https://deepmind.google/models/model-cards/gemini-4-argon/) |
| WebArena-Verified, official grader, OSWorld scaffold | Qwen3.8-27B | 64.8 | Alibaba, Aug 2026 — [HF card](https://huggingface.co/Qwen/Qwen3.8-27B) |
| AndroidWorld | Qwen3.8-27B | 81.9 | Alibaba, Aug 2026 — [HF card](https://huggingface.co/Qwen/Qwen3.8-27B) |

- The rows above span different versions and subsets. OSWorld-Verified, OSWorld-2.0 and the OSWorld-2.0 offline subset are not one scale.
- LLM-Stats lists 28 OSWorld-Verified entries: 0 verified, all self-reported, with no Grok or DeepSeek — [LLM-Stats](https://llm-stats.com/benchmarks/osworld-verified).
- OSWorld 2.0's primary metric is binary completion at 500 steps. Partial credit is reported separately and reads far higher (Claude Opus 4.8: 20.6% binary, 54.8% partial). The leaderboard table did not load, and no Gemini, Grok, Qwen or DeepSeek entry appears in the retrieved text — [OSWorld 2.0](https://osworld-v2.xlang.ai/).
- Grok 4.7's model card has no mention of OSWorld, WebArena, Mind2Web, ScreenSpot or MMMU (text-searched) — [Grok card](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf). DeepSeek's card does not mention computer use — [DeepSeek card](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash).

**ComponentBench** [Independent, COLM 2026, arXiv Aug 2026, mostly Predecessor models]. Short web component tasks, 2,910 tasks across 97 component types, BrowserGym with headless Chromium, 1280×720 viewport, 20-step budget. Pixel mode means screenshot only, acting through coordinates. Gemini models were called through AI Studio and output 0–1000 values mapped by the harness; Qwen3-VL also output 0–1000, on local vLLM at FP8. Table 1 confidence half-width is 1.9% per cell. Thinking settings are not given for the Gemini models — [paper](https://arxiv.org/pdf/2608.18307).

| Model | Pixel, all tasks | Pixel, Command & Navigation (includes button, link, pagination) | Pixel, Discrete Choice (includes radio group, checkbox) |
|---|---|---|---|
| Gemini 3 Flash [Predecessor] | 85.4 | 96 | 96 |
| GPT-5.4 (comparator) | 83.8 | 95 | 93 |
| Gemini 3.1 Flash-Lite (target model) | 63.3 | 85 | 78 |
| Qwen3-VL-235B [Predecessor] | 50.5 | 68 | 62 |

The family columns are from Figure 3 of the [paper](https://arxiv.org/pdf/2608.18307); I confirmed the column mapping by checking that the six-model means match its Table 3 (Discrete Choice Pixel 79.0). On the harder suite, Gemini 3 Flash Pixel falls from 85.4% to 60.9% — [paper](https://arxiv.org/pdf/2608.18307). Changing only the observation and action space shifts success by more than 30% for the same model — [abstract](https://arxiv.org/abs/2608.18307).

**GUI-Primitives** [Independent, EMNLP 2026, closed APIs queried May 2026]. 994 contrastive spatial-relation items, strict point-in-box — [abstract](https://arxiv.org/abs/2608.21832).
- Gemini 3.1 Flash Lite scored 0.073 (Full, n=994) and 0.076 (Clean, n=185). The best of 19 models, Claude Opus 4.7, scored 0.313. Qwen2.5-VL-7B-Instruct scored 0.220 [Predecessor] — [paper](https://arxiv.org/html/2608.21832).
- Predictions fell outside both candidate regions on 60–92% of items, and authors attribute most failures to candidate localization rather than relation understanding — [abstract](https://arxiv.org/abs/2608.21832).
- The core prompt was "respond with only the pixel coordinate to click", and images were pre-resized to a long side of at most 1500 px and rescaled back — [paper](https://arxiv.org/html/2608.21832).

**ScreenSpot-Pro** (grounding on high-resolution professional screens).
- No row for Grok, DeepSeek, gemini-3.8-flash, Flash-Lite, Argon or Qwen3.8-27B. Nearest rows: Qwen3.8-Max 84.5 (2026-08-03), Qwen3.5-122B-A10B 70.4, Gemini 3 Flash (Thinking) 69.1 (2025-12-17) [Predecessor]. Setups differ across rows, with tags such as "w/ tools" and "crop zoom", and no pass rule is stated. Board not verified against the original papers — [Papers With Code mirror](https://paperswithcode.co/benchmark/screenspot-pro?eval=5370).
- Alibaba's Qwen3.8-Max table gives Gemini 3.1-Pro 68.1 evaluated in-house [Vendor, about a competitor]. The 27B table has no ScreenSpot Pro row — [OpenLM mirror](https://openlm.ai/qwen3.8/).
- Source conflict: GUI-Primitives says generalist VLMs score under 2% on ScreenSpot-Pro in prior reports — [paper](https://arxiv.org/html/2608.21832). The board above shows general models near 70 or higher, so that statement looks out of date.

**Roboflow object detection** [Independent; not UI]. mAP@50, snapshot 26 Oct 2026. One shared prompt, boxes as [y_min, x_min, y_max, x_max] integers 0–1000. Sample domains: sports, aerial, industrial, pharmaceutical — [detection eval](https://playground.roboflow.com/evals/object-detection).

| Model | Low effort | High effort |
|---|---|---|
| Gemini 4 Argon | 82.5 | 85.1 |
| Gemini 3.8 Flash | 68.1 | 74.8 |
| Qwen3.8 27B (self-hosted) | 65.7 | 66.1 |
| Gemini 3.5 Flash-Lite | 57.5 | not listed |
| DeepSeek V4 Flash Vision Exp [Predecessor] | 45.3 | not listed |
| Grok 4.7 | 40.4 | 41.2 |

**Locating text.** Roboflow's text localization column (Section 2) requires box and exact text together. ParseBench's Visual Grounding column (Section 2) traces extracted elements to page locations — [repo](https://github.com/run-llama/ParseBench). On documents it gives Gemini 3.8 Flash 67.46–70.01, Qwen 3.8 27B 58.53–64.56, Gemini 3.5 Flash Lite 54.85–57.81, Gemini 3.1 Flash Lite 33.84–48.38, DeepSeek V4.1 Flash 21.75–28.04, and no Grok or Argon row — [CSV](https://raw.githubusercontent.com/run-llama/ParseBench/main/leaderboard.csv).

**Other** [Predecessor]: AutoGUI-v2 (Apr 2026) functional element grounding: Qwen3-VL-32B-Instruct 71.1, Gemini-2.5-Pro-Thinking 67.7 — [paper](https://arxiv.org/html/2604.24441v1).

### Inferences
- Grid-format fit is a live confound. Roboflow's shared prompt uses Gemini's native [y, x] order, while Roboflow itself says Qwen prefers [x, y] and that format changes hurt. Its page does not say whether format is tuned per model. So Grok 4.7's 40.4 and Qwen's 65.7 may partly reflect the output format, not only spatial skill. This matters directly here because the user's agent also imposes a format.
- Effort has a large effect on localization for some models. Gemini 3.8 Flash text localization goes from 26.4 at low to 58.6 at high, while Gemini 4 Argon moves only from 81.5 to 84.7.
- GUI-Primitives is deliberately harder than this task. A target named by its visible text ("Next", or an option's text) is closer to ScreenSpot-Pro or Roboflow text localization than to contrastive relations such as "the item left of X". Its 0.073 for Gemini 3.1 Flash Lite should not be read as a click-miss rate for labelled buttons. ComponentBench shows the same model completing 85% of Command & Navigation tasks in Pixel mode.
- ComponentBench's 1280×720 viewport is not a 1920×1080 full-screen capture, so these figures may not transfer.
- Vendor-reported agent scores can reflect harness and retries, so they cannot show that a single-shot coordinate is accurate, which is what this agent needs.

### Gaps
- No target model has a measured single-shot click accuracy on a browser quiz or similar form page.
- Grok 4.7: no UI pointing evidence at all, only non-UI detection and text localization.
- DeepSeek V4.1 Flash: no UI pointing evidence, no coordinate documentation, and only document-level grounding data of unknown prompt fit.
- Qwen3.8-27B: no independent pointing evidence.
- Gemini 3.8 Flash and Argon: no independent UI pointing evidence.
- Mind2Web and ScreenSpot v1: no results found for any target model.

## 4. How does each provider resize or tokenize a 1920x1080 image, what does that mean for small text, and do normalized coordinates stay valid?

### Takeaway
DeepSeek publishes a resize rule; Google publishes token budgets but no pixel sizes; Groq publishes a flat 2,048-token count with no pixel or resize rule; xAI publishes neither tokens nor resizing. Coordinates on a 0–1000 grid survive resizing by design where the model emits them relative to the image, but only Gemini documents that behavior.

### Cited Findings

| Provider, model | Documented handling | Tokens for 1920×1080 | Documented limits | Not documented |
|---|---|---|---|---|
| Google, Gemini 3 and 4 | `media_resolution` caps tokens per image: default 1120, low 280, medium 560, high 1120, ultra_high 2240 (per item only) — [docs, updated 2026-10-13](https://ai.google.dev/gemini-api/docs/media-resolution) | 1120 at default per that table. An older tile rule gives 1,548 (see below) | Inline data counts toward a 20 MB request limit — [docs](https://ai.google.dev/gemini-api/docs/image-understanding) | Pixel size the model receives; any resize rule |
| DeepSeek, `deepseek-flash` | `low` = 512×512. `high` and `auto` currently equal `original`. Under about 544×544 total pixels, images scale up; larger images scale down, keeping aspect ratio, to about the pixel count of 1300×1300 — [Vision guide](https://api-docs.deepseek.com/guides/vision) | Upper bound 1024 — [Vision guide](https://api-docs.deepseek.com/guides/vision) | 8192 px per side (4096 with 15+ images), 32 MiB per image for base64 or URL — [Vision guide](https://api-docs.deepseek.com/guides/vision) | Exact rounding; calculator logic is not visible as text — [token usage](https://api-docs.deepseek.com/quick_start/token_usage) |
| Groq, `qwen/qwen3.8-27b` | "Each image counts as 2048 input tokens." No resize statement and no `detail` setting — [Vision docs](https://console.groq.com/docs/vision) | 2048 flat | 3 images; 20 MB for a request with an image URL; base64 handling not stated — [Vision docs](https://console.groq.com/docs/vision); [model page](https://console.groq.com/docs/model/qwen/qwen3.8-27b) | Any pixel cap; whether images are resized |
| xAI, `grok-4.7` | `detail` is `auto` (default), `low` or `high`; low "may miss finer details", high is "slower and more expensive in terms of token usage" — [legacy guide](https://docs.x.ai/developers/model-capabilities/legacy/chat-completions) | Not published — [image understanding](https://docs.x.ai/developers/model-capabilities/images/understanding); [models page](https://docs.x.ai/developers/models) | 20 MiB per image; jpg/jpeg or png; no image-count limit — [models page](https://docs.x.ai/developers/models) | Resize rule; token cost; pixel size at each detail level |

**Gemini detail**
- Conflict: the image understanding page says images over 384 px are tiled at 258 tokens per 768×768 tile, and gives a crop-unit formula. It does not say which model families that applies to — [image understanding](https://ai.google.dev/gemini-api/docs/image-understanding); [tokens page](https://ai.google.dev/gemini-api/docs/tokens). Applying its formula to 1920×1080 gives a crop unit of 720, 6 tiles and 1,548 tokens (my calculation), which does not match the 1120 budget.
- Global setting: the legacy Generate Content page documents `generation_config.media_resolution` for all multimodal models and a per-part setting labelled experimental, with per-part taking precedence — [legacy page](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution). The current page describes only per-item control — [current page](https://ai.google.dev/gemini-api/docs/media-resolution).
- Guidance: images at `high`; `ultra_high` for uses such as computer use — [current page](https://ai.google.dev/gemini-api/docs/media-resolution). The legacy page says "required for specific use cases such as computer use" — [legacy page](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution).
- Gemini 2.5 default image cost is listed as "256 + Pan & Scan (~2048)", relevant only to legacy `gemini-2.5-flash-lite` — [legacy page](https://ai.google.dev/gemini-api/docs/generate-content/media-resolution).
- Chat Completions: images go as base64 data URLs. `extra_body` lists `cached_content` and `thinking_config`, and `media_resolution` is not listed in the page body — [OpenAI compatibility, updated 2026-10-28](https://ai.google.dev/gemini-api/docs/openai). The media resolution page does not mention the OpenAI endpoint — [docs](https://ai.google.dev/gemini-api/docs/media-resolution). Whether `image_url.detail` maps to it on that endpoint is undocumented.
- Third parties such as LiteLLM translate `detail` in their own layers [Snippet], which says nothing about Google's endpoint — [LiteLLM](https://docs.litellm.ai/docs/providers/gemini).
- One paper describes Gemini's server-side downsampling as "variable" — [GUI-Primitives](https://arxiv.org/html/2608.21832).

**DeepSeek detail**
- Weights config: `patch_size` 14, `downsample_ratio` 3, `max_image_tokens` 1024, `min_pixels` 295936 — [config.json](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash/raw/main/config.json). That min_pixels equals 544², matching the guide.
- The guide says `original` "keeps the original image" and also says large images are scaled down. Its 2000×2000 vs 5000×5000 same-tokens example suggests the scaling still applies — [Vision guide](https://api-docs.deepseek.com/guides/vision).
- Old reviews describe a stricter cap of 384 tokens and about 800×800, which belongs to the retired vision-exp model [Predecessor] — [IntuitionLabs](https://intuitionlabs.ai/articles/deepseek-v4-flash-vision-document-understanding); [vLLM Recipes](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp).

**Qwen detail**
- The open-weights default preprocessor: `patch_size` 16, `merge_size` 2, size `longest_edge` 16777216 and `shortest_edge` 65536 — [preprocessor_config.json](https://huggingface.co/Qwen/Qwen3.8-27B/raw/main/preprocessor_config.json). Nothing states that Groq uses this config.

**xAI detail**
- Docs examples pass `"detail": "high"` without explaining it — [image understanding](https://docs.x.ai/developers/model-capabilities/images/understanding). The AI SDK says unset means full resolution, which differs from xAI's stated `auto` default — [AI SDK](https://ai-sdk.dev/providers/ai-sdk-providers/xai).

**Coordinate validity**
- Gemini: coordinates are "relative to image dimensions" and scale to 0–1000, to be descaled from the original size — [docs](https://ai.google.dev/gemini-api/docs/image-understanding).
- Qwen3-VL: a community GitHub issue says relative coordinates are unaffected by resizing [Predecessor] — [issue](https://github.com/QwenLM/Qwen3-VL/issues/1486). The cookbook resizes with `smart_resize` and multiplies relative values by the resized size — [cookbook](https://raw.githubusercontent.com/QwenLM/Qwen3-VL/main/cookbooks/computer_use.ipynb).
- Pixel requests are the failure case. GUI-Primitives lists "Type F", where coordinates come back in the downsampled frame. Rescaling was needed on 1,297 of 1,581 Claude Sonnet ScreenSpot-Pro records and about 1,500 of 1,581 for GPT-5 — [paper](https://arxiv.org/html/2608.21832). Those are other vendors' models, but they show that pixel output depends on the hidden resize.
- Output conventions vary by family: pixel, normalized [0,1], or normalized [0,1000] — [paper](https://arxiv.org/html/2608.21832).
- xAI and DeepSeek document no coordinate convention, so nothing states how those models' output relates to a resized image — [xAI](https://docs.x.ai/developers/model-capabilities/images/understanding); [DeepSeek](https://api-docs.deepseek.com/guides/vision).

### Inferences
All arithmetic below is mine.
- Grid resolution is not the limit. On 1920×1080 one grid unit is 1.92 px across and 1.08 px down. A 16 px radio button is about 8.3 × 14.8 units.
- DeepSeek: 1920×1080 is 2,073,600 px, above the documented budget. Scaling to the guide's 1300² gives about 1733×975. Scaling to 1024 tokens at 42 px per token (14 × 3) gives about 1792×1008. Either way the image shrinks by about 7–10% per side, so a 14 px glyph lands near 12.6–13 px.
- Qwen weights at default: `smart_resize` with factor 32 gives 1920×1088, or 60 × 34 = 2,040 tokens, close to Groq's flat 2,048. If Groq preserves that behavior, a 1080p image stays near native size, but Groq does not say so, and a flat billing count does not prove what the model sees. The 8 px height change is a tiny stretch that does not disturb normalized coordinates.
- Token budget per pixel at this size: Gemini default 1120 tokens is about 43×43 px per token; `ultra_high` 2240 about 30×30; Qwen 2,040 about 32×32. Encoders differ, so this shows information budget only and cannot rank legibility.
- On Chat Completions, a Gemini request can reasonably be assumed to get the default 1120 budget, since the default equals `high`. Going to 2240 has no documented path there.
- Cropping to the quiz area before sending raises effective resolution on every provider, at the cost of mapping coordinates back. ScreenSpot-Pro entries tagged "crop zoom" and "two-step zoom" show researchers use this approach, but those rows do not isolate its gain.

### Gaps
- No provider publishes the pixel dimensions at which a 1920×1080 image reaches the model, except DeepSeek's approximate rule.
- Whether Gemini's 0–1000 values stay valid under `ultra_high` or any letterboxing is not addressed in docs. The docs imply yes through "relative to image dimensions".
- No test was found measuring how small-text accuracy changes across `media_resolution` or `detail` levels on these models.
- Direct measurement is the only route for xAI: send one image at each `detail` and compare the `usage` values.

## 5. How well do models detect UI state, such as which radio button or checkbox is selected?

### Takeaway
No benchmark found measures selected-state reading for any target model. The closest numbers are task-completion rates for choice widgets on older models, plus toggle studies on models older than these, and those show agents misjudging state. This is the thinnest of the three requirements.

### Cited Findings
- ComponentBench "Discrete Choice" family (checkbox, checkbox group, tristate checkbox, radio group, switch, toggle button, toggle button group, segmented control, rating): Pixel pass rates are Gemini 3 Flash 96, GPT-5.4 93, GPT-5.4 mini 86, Gemini 3.1 Flash-Lite 78, Qwen3-VL-235B 62, GPT-5 mini 59. The six-model mean by mode is Browser-Use 97.2, AX-tree 85.7, SoM 83.3, Pixel 79.0 — [paper](https://arxiv.org/pdf/2608.18307). These measure finishing a task, not reporting state, and the paper has no case study on selected-state perception for these controls — [paper HTML](https://arxiv.org/html/2608.18307).
- ComponentBench's failure taxonomy has "Missing commit or confirmation" at 11.6% and "Target acquisition / wrong instance" at 11.2% of failures across five models — [paper HTML](https://arxiv.org/html/2608.18307). It includes one case labelled "a wrong belief about the target state", on a kanban board with GPT-5.4 mini — [paper HTML](https://arxiv.org/html/2608.18307).
- See, Think, Act (CVPR 2026, v5 Mar 2026) [Predecessor: GPT-5, GPT-4o, Gemini 2.5 Pro, Qwen-2-VL-72B and others]: most agents had toggle execution accuracy "below 50%". Agents were most unreliable when the current state already matched the desired one and showed a bias toward toggling. Qwen-2-VL-72B correctly left such toggles alone 78.96% of the time and wrongly toggled 20.67%; OS-Atlas-7B wrongly toggled 64.10% — [paper](https://arxiv.org/html/2509.13615v5). Having agents perceive the state first, then act, improved toggle accuracy "by over 30%" — [abstract](https://arxiv.org/abs/2509.13615).
- EvoGUI (Jul 2026) tests understanding of state changes, not widget state, at `max_image_side` 512 [mostly Predecessor]. EvoGain: Gemini-3-Flash-Preview 60.4 (highest of 28), Qwen3.5-27B 39.6, Qwen3.6-27B 38.5, Grok-4.20 35.7. No DeepSeek model. Authors say models "can often detect salient visual changes but fail to recover value-bearing details" — [paper](https://arxiv.org/html/2607.17050).
- A developer's design note argues pixels give no absolute checkbox state, since a disabled box, an already-selected radio and a missed click all look alike after clicking. It is an argument, not a measurement [Snippet] — [flowproof PR](https://github.com/automators-com/flowproof/pull/711).
- One blog's claim of over 95% checkbox accuracy for DeepSeek OCR is unsourced and is excluded here as unreliable.

### Inferences
- A small radio dot gives the model little signal. At 16 px it is about one encoder patch for Qwen (16 px) and DeepSeek (14 px, before about 7–10% downscaling). A highlighted row carries far more pixels, so quiz styling may matter as much as the model. This is untested.
- The "state already matches" failure bears directly on this agent: it must decide not to click when the right option is already selected. The StaR result suggests asking the model to state the current selection before choosing an action, but that was measured only on older models.
- Comparing screenshots before and after a click would give a check that does not rely on the model's reading of a single frame, in line with the design note above.

### Gaps
- No selected-state accuracy for grok-4.7, Qwen3.8-27B, DeepSeek V4.1 Flash, gemini-3.8-flash, Flash-Lite or gemini-4-argon.
- A Stanford Legal Design Lab post scored selected and unselected checkboxes on legal forms across 15 vision models, but no per-model checkbox figures were retrieved [Snippet] — [post](https://medium.com/legal-design-and-innovation/best-vision-enabled-llms-for-data-extraction-cost-performance-benchmark-b62fe7bc5430).
- A small labelled test set of quiz screenshots with known selected states would be the only way to close this gap.

## 6. Does xAI or DeepSeek have a documented computer-use capability, and does Gemini have one that a Chat Completions request can use?

### Takeaway
xAI and DeepSeek document no computer-use tool. Gemini has one, but its documentation shows it only on the Interactions API. No documented path exists through Chat Completions, although coordinate output by prompt is a separate feature that needs no tool.

### Cited Findings

**xAI**
- Tools listed: Web Search, X Search, Code Execution, Image Generation, Collections Search, and client-side Function Calling. No computer-use, browser-control or screenshot tool — [tools overview](https://docs.x.ai/developers/tools/overview).
- The Grok 4.7 guide lists function calling, web search, X search and code execution — [developer guide](https://docs.x.ai/developers/grok-4-7). The launch post says nothing about computer use — [launch post](https://x.ai/news/grok-4-7).
- In the model card, "computer-use review" appears only as a verifier inside SWE-Marathon v1.1, not as a capability of the model — [card](https://media.x.ai/v1/website/card4p7-3a96f40b.pdf).

**DeepSeek**
- The Vision guide and V4.1 notice describe no computer-use tool — [Vision guide](https://api-docs.deepseek.com/guides/vision); [V4.1 notice](https://api-docs.deepseek.com/news/v4-1-flash).
- The Anthropic-compatible page does not mention any `computer_*` tool type, so its status there is undocumented — [Anthropic API guide](https://api-docs.deepseek.com/guides/anthropic_api).
- DataCamp's tutorial (22 Sep 2026) says "built-in types like web search and computer use are silently ignored" on the Responses API. Its working pattern uses function tools that return a Playwright screenshot as `input_image` inside `function_call_output`, which "DeepSeek then reads ... as an image" — [DataCamp](https://www.datacamp.com/tutorial/deepseek-v4-1-api-tutorial). This is a secondary source with no matching official statement found.
- Community packs add screenshot, click and type through their own tooling, not the API [Snippet] — [example 1](https://github.com/bensblueprints/deepseek-v4.1-flash-computer-use); [example 2](https://github.com/secretxuan/dsh-computer-use-win).

**Groq** (not asked, listed for completeness)
- Features listed for Qwen3.8-27B: Tool Use, JSON Object Mode, JSON Schema Mode, Reasoning, Vision. No computer-use tool — [model page](https://console.groq.com/docs/model/qwen/qwen3.8-27b).

**Gemini**
- Computer Use supports `gemini-4-argon`, `gemini-3.8-flash` (recommended), `gemini-3.5-flash-lite` and `gemini-3-flash-preview`. `gemini-3.1-flash-lite` is not listed. Tool type `computer_use`, with `environment` of browser, mobile or desktop. All examples use the Interactions API (`client.interactions.create` or `/v1/interactions`), google-genai 2.7.0 or higher, and a client-side action loop — [computer use, updated 2026-10-30](https://ai.google.dev/gemini-api/docs/computer-use).
- The OpenAI compatibility page covers function calling, structured output, image input and `reasoning_effort`. Computer use appears only in the site navigation, not the body — [OpenAI compatibility, updated 2026-10-28](https://ai.google.dev/gemini-api/docs/openai).
- Model pages list Computer Use as "Supported" for Gemini 3.8 Flash and 3.5 Flash-Lite — [3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash); [3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite).
- `ultra_high` is per-part and is the level linked to computer use — [media resolution](https://ai.google.dev/gemini-api/docs/media-resolution). No per-part setting is documented on the compatibility page — [OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai).

### Inferences
- A Chat Completions agent on Gemini can use prompted coordinates with structured output, because `box_2d`-style output is a prompt behavior, not a tool. It would not get the Computer Use tool's action schema, safety decisions or documented `ultra_high` path.
- On xAI, DeepSeek and Groq, function calling can carry click coordinates, but the model then has no documented screen convention. The harness must define the grid and check the results.
- "Undocumented" does not prove a Chat Completions request cannot reach these features. It means nothing supports relying on them.

### Gaps
- No live test was run, since this research made no API calls to any provider.
- Whether `tools` entries of type `computer_use` pass through or are dropped on Gemini's compatibility endpoint was not found.
- DeepSeek has no official statement on computer-use tool types.

## 7. What evidence is missing?

### Takeaway
No model here has a direct, independent test of the full task: reading a browser quiz, reporting the selected option, and returning a usable click point. The strongest coverage is for Gemini, but on most of the specific tasks even that coverage comes from non-UI data, vendor reports or earlier versions. Grok 4.7 and DeepSeek V4.1 Flash have the least relevant evidence.

### Cited Findings

Coverage by evidence type. "Direct" means this model was tested. All entries are sourced in Sections 1–6.

| Model | MMMU-Pro (AA) | Arena Vision | Roboflow detection | Roboflow OCR | ParseBench | OSWorld family | ScreenSpot-Pro | Independent UI pointing | Coordinate docs | UI state test |
|---|---|---|---|---|---|---|---|---|---|---|
| `grok-4.7` | Mirror only (Low) | Direct | Direct | Low effort only | None | None | None | None | None | None |
| `qwen/qwen3.8-27b` | Direct, not on Groq | Direct | Direct, self-hosted | None | Direct | Vendor | None | None | Family convention only | None |
| `deepseek-flash` | Direct (1017) | Earlier revision | Predecessor | Predecessor | Direct, revision unknown | None | None | None | None | None |
| `gemini-3.8-flash` | Direct | Direct, preliminary | Direct | Direct | Direct | Vendor | None | None | Yes | None |
| `gemini-3.5-flash-lite` | Mirror only | Direct | Direct (low) | Direct | Direct | Vendor | None | None | Yes | None |
| `gemini-3.1-flash-lite` | Mirror and vendor | Preview model | None | None | Direct | Vendor | None | Direct | Yes | Indirect (task success) |
| `gemini-4-argon` | None found | No row seen | Direct | Direct | None | Vendor | None | None | Yes | None |

**Pages that could not be fully read** (no values guessed)
- [arena.ai](https://arena.ai/leaderboard/vision): retrieved to rank 159, then truncated. A direct download returned only a 5 KB page.
- [Qwen blog](https://qwen.ai/blog?id=qwen3.8) returned only the word "Qwen", and the [Alibaba Medium post](https://alibaba-cloud.medium.com/qwen3-8-max-a-new-bar-for-coding-and-cowork-b1ed265e03f0) returned HTTP 403, so its tables come from the [OpenLM mirror](https://openlm.ai/qwen3.8/).
- [Kaggle ParseBench](https://www.kaggle.com/benchmarks/llamaindex-org/parsebench) returned only a title, and [parsebench.ai](https://parsebench.ai) had no table.
- [OSWorld 2.0](https://osworld-v2.xlang.ai/) leaderboard table did not load.
- [NVIDIA's DeepSeek card](https://build.nvidia.com/deepseek-ai/deepseek-v4.1-flash/modelcard) returned only a page shell.
- A `preprocessor_config.json` for DeepSeek V4.1 Flash returned 404, and Roboflow's DeepSeek model page slug returned 404.
- AA's embedded data covers only 27 charted configurations, so other rows rest on mirrors.
- Google's evals-methodology pages linked from the cards were not opened.

### Inferences
- The evidence separates into three quality tiers for this task: (1) target model, on-task, independent, which is empty; (2) target model, off-task, independent, such as Roboflow, AA and ParseBench; (3) on-task but vendor-reported or on earlier versions, such as OSWorld and ComponentBench.
- Differences between models on Tier 2 boards are real for those tasks. How far they carry over to quiz screenshots is unknown.
- A small test of the user's own screenshots would add more than any further literature search. It would cover exact text, selected state, and hit rate on option and Next targets, across effort levels, with a coordinate format suited to each model.

### Gaps
**Undocumented**
- Coordinate output for Grok 4.7 and DeepSeek V4.1 Flash.
- A coordinate format specific to Qwen3.8-27B.
- Image token cost and resizing for xAI.
- Pixel limits and resizing for Groq.
- Pixel dimensions after processing for Gemini.
- `media_resolution` on Gemini's Chat Completions endpoint.

**Untested on these models**
- Small interface text, code in browser screenshots, and JPEG artifact effects.
- Radio and checkbox state reading.
- Single-shot click accuracy at 1920×1080.
- Any evaluation run on Groq's hosted endpoint.
- Reading performance on the `deepseek-flash` 1017 revision outside AA's MMMU-Pro.
