# How Current LLMs Handle Solution Architecture and Scenario-Based Judgement Questions (state as of 1 November 2026)

## Are there studies or tests of LLMs on cloud certification exams (AWS, Azure, Google Cloud)?

### Takeaway
I found no study or test of any target model (grok-4.7, Qwen3.8-27B, DeepSeek V4.1 Flash, gemini-3.8-flash, Flash-Lite, gemini-4-argon) on a cloud certification exam; the only named AWS, Azure and GCP results are 2023-era tests of GPT-3, GPT-3.5 and GPT-4. Two 2026 academic benchmarks (SAKE, CAKE) test architecture knowledge on older model versions, and both show MCQ scores bunched near the top, which hides gaps that appear in free-response answers and in vendor-specific certification questions.

### Cited Findings

#### Direct cloud-certification tests (all OLD: GPT-3, GPT-3.5, GPT-4 era)

| Source | Date | Model | Exam and sample | Method | Result |
|---|---|---|---|---|---|
| [Noever and Ciolino, arXiv 2305.05377](https://arxiv.org/abs/2305.05377) | May 2023 | GPT-3, Turbo-GPT3.5 | 1,149 certification panels; 5,197 questions over about 1,100 practice exams, plus 940 synthetic questions | Zero-shot, temperature 0, letter answer; pass is above 70%; questions came from [ExamTopics](https://arxiv.org/pdf/2305.05377), a community question bank | AWS SAA-C03: 50% for both models. AWS Solutions Architect Professional: 50% for both. AZ-305: 100% (Turbo) / 75% (GPT-3). AZ-304: 100% / 50%. AZ-303: 25% / 25%. Google Professional Cloud Architect: 80% (Turbo; GPT-3 value not readable from the PDF layout). Google Associate Cloud Engineer: 25% / 25%. |
| [tecRacer, Moehn](https://www.tecracer.com/blog/2023/01/can-chatgpt-tackle-the-aws-certification-challenge.html) | 29 Jan 2023 | ChatGPT (version not stated) | AWS SAA: 10 official sample questions; 65 Whizlabs practice questions | One question at a time, unaltered | 8/10; 41/65 (63%) against the article's 72% threshold. Struggled with "multiple similar answers" and in-depth knowledge. Wrong answers were usually plausible options. |
| [ElasticScale blog](https://elasticscale.com/blog/chatgpt-score-on-the-solution-architect-professional-exam/) | Not dated | ChatGPT 4.0, ChatGPT 3.5 | AWS SA Professional; question count not stated | Links a chat transcript; method not described | 832 (GPT-4) and 733 (GPT-3.5) against a 750 pass mark. |
| [Salva, Medium](https://medium.com/@miguelsalva/chatgpt-goes-certified-aws-82747a2e4619) | Not confirmed | ChatGPT (version not confirmed) | AWS sample exams | Page returned 403 to my fetch; search snippet only | SAA-C03 scored 700/1000, FAIL. [GPT-4 update post](https://medium.com/@miguelsalva/chatgpt-goes-certified-aws-gpt-4-updated-5c41ade4795b) also returned 403, so its scores are unknown. |

- Certification percentages in the Noever paper come from very small samples. About 5,197 questions across about 1,100 exams is under 5 per exam, and many scores fall on 25% steps — [Noever and Ciolino PDF](https://arxiv.org/pdf/2305.05377). I extracted the table rows from a multi-column PDF layout, so check them before quoting them singly.
- Searches for AZ-305 and Google Professional Cloud Architect results on modern models returned only human pass reports and question-bank sellers, with no model scores — [AZ-305 pass report](https://www.softbank.jp/biz/blog/cloud-technology/articles/202512/az-305/); [Examtopics PCA bank](https://www.examtopics.com/exams/google/professional-cloud-architect/view/).

#### 2026 architecture benchmarks (OLDER model versions; no target model tested)

**SAKE** (arXiv 2606.29520, 28 June 2026, University of Southern Denmark): 2,154 four-option MCQs across eight architecture categories, 11 models, temperature 0, zero-shot and five-shot, prompt ends "Answer with a single letter" — [SAKE](https://arxiv.org/pdf/2606.29520).

| Model (older than target models) | Zero-shot | Five-shot | Architectural Solutions (ASO), zero-shot | ASO, prompts over 266 words |
|---|---|---|---|---|
| GPT 5.4 | 93.95 | 94.13 | 88.6 | 86.6 |
| Gemini 3.1 Flash Lite | 93.66 | 93.14 | 91.1 | 87.8 |
| DeepSeek v3.2 | 93.61 | 89.4 | 90.2 | 87.8 |
| Claude Opus 4.6 | 93.57 | 94.23 | 90.2 | 87.8 |
| Qwen 3 235B A22B | 93.38 | 93.0 | 89.8 | 86.6 |
| Grok 4.2 | 93.28 | 93.14 | 90.2 | 85.4 |
| Grok 4.1 Fast | 92.05 | 92.57 | 90.2 | 87.8 |
| GPT 5.4 Nano | 90.96 | 89.31 | 86.6 | 84.2 |

- SAKE's authors call overall accuracy "high and tightly clustered (89.31–94.23%)" and say that on knowledge recall the strongest models are "close to interchangeable" — [SAKE](https://arxiv.org/pdf/2606.29520).
- ASO is the closest SAKE category to "which option is best". It asks models to connect architectural choices to effects, "reflecting the kind of reasoning that practitioners apply when selecting between competing solutions", and it was the weakest category at 89.5% zero-shot and 88.4% five-shot — [SAKE](https://arxiv.org/pdf/2606.29520).
- ASO accuracy falls as question text gets longer. It runs 89.7–100% for 0–134 word questions and 84.2–87.8% above 266 words. Overall accuracy moves the opposite way — [SAKE Table 5](https://arxiv.org/pdf/2606.29520).
- Five-shot prompting hurt DeepSeek v3.2 most (−4.21 points; its Structural Patterns score fell to 78.3%), and the authors link this to longer prompts — [SAKE](https://arxiv.org/pdf/2606.29520).
- SAKE limits: review was by the three authors only, and they state that MCQ "cannot capture the full complexity of real architectural decision-making". The paper gives no reasoning-effort setting and asks for a single-letter answer, so these are not shown to be high-reasoning results — [SAKE](https://arxiv.org/pdf/2606.29520).

**CAKE** (arXiv 2604.05755, 7 April 2026, University of Southern Denmark): 188 cloud-native architecture questions, 130 MCQ and 58 free-response, drawing on the AWS Well-Architected Framework and Azure Architecture Patterns. It covered 22 configurations of Qwen 2.5, Qwen3-Coder, Llama 3.x, Mistral 3.1, GPT-4o-Mini and GPT-5-Mini — [CAKE](https://arxiv.org/html/2604.05755).

- MCQ saturates: 16 of 22 configurations exceed 90%, five reach 99.2%, and gains above 3B parameters shrink to 1–3 points per size step — [CAKE](https://arxiv.org/html/2604.05755).
- Free-response keeps separating models: GPT-4o-Mini and GPT-5-Mini both score 99.2% on MCQ but 3.77 and 4.52 out of 5 on free-response — [CAKE](https://arxiv.org/html/2604.05755).
- The authors warn that the longest option tends to be correct, and experts found elaboration bias in some distractors, so CAKE's MCQs may be easier than exam-style MCQs — [CAKE](https://arxiv.org/html/2604.05755).
- Each MCQ ran three times with shuffled options: unanimous answers were 89.5% accurate and split-majority answers 55.0% — [CAKE](https://arxiv.org/html/2604.05755).
- Limits: Krippendorff's alpha for expert ratings was near zero, and free-response grading relied mainly on one LLM judge, DeepSeek-R1:32B — [CAKE](https://arxiv.org/html/2604.05755).

#### Adjacent benchmarks that show tier gaps (OLDER models, different domains)

- **CyberCertBench** (April 2026, 45 models, 437 certification questions from itexams, ExamTopics and free-braindumps, 5-shot): tier gaps are much wider than in SAKE. Gemini 2.5 Flash Lite vs Gemini 2.5 Pro scored 74.0 vs 91.5 on Cisco CCNx, 52.5 vs 61.7 on Fortinet NSE, and 64.2 vs 73.6 on ISA/IEC 62443. The best Fortinet NSE score was only 62.4, and one model passed ISA/IEC 62443 at the 80% bar — [CyberCertBench](https://arxiv.org/html/2604.20389v1).
- **QuArch** (computer hardware architecture, not cloud; v2 stamp 21 July 2026; 2,671 questions, 10 frontier models): recall is 84.2–90.9 for all models, while reasoning spans 33.7–73.2. On Design questions, Gemini-3-Pro scored 73.8 and Gemini-3-Flash 66.7, though Flash led slightly on overall reasoning (71.9 vs 71.0). The source's table headers are misaligned, so these columns are read by the paper's own arithmetic — [QuArch](https://arxiv.org/html/2510.22087v2).

#### Real exam format

- AWS SAP-C02 has 65 scored and 10 unscored questions and a 750/1000 pass mark. It uses multiple choice (one correct, three distractors) and multiple response (two or more correct out of five or more, and all must be selected for credit) — [AWS SAP-C02 guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-professional-02/solutions-architect-professional-02.html).
- AWS SAA-C03 has 50 scored and 15 unscored questions and a 720 pass mark — [AWS SAA-C03 guide](https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html).

### Inferences
- The tier gap depends on question type. On concept MCQs grounded in textbooks (SAKE), a low-cost tier sits within about 0.3 points of the top. On product-specific certification MCQs (CyberCertBench), the gap between Gemini 2.5 Flash Lite and Gemini 2.5 Pro reached 17.5 points on Cisco. Cloud exams combine scenario reasoning with named-product detail, so the SAKE gap is probably a lower bound. This is my reading, not a tested result.
- Long scenario questions are likely harder than SAKE's headline numbers suggest. Models landed near 84–88% on long ASO items, but step sizes in Table 5 imply about 40–80 questions per bin, so gaps between models there are only a few questions.
- The 2023 results show only that GPT-4 class models could reach pass-level on small or undocumented samples, and that plausible distractors were the main failure mode. They say nothing about current models.
- Family carry-over is weak evidence. SAKE tested Grok 4.1 Fast and 4.2, not 4.7; DeepSeek v3.2, not V4.1; Gemini 3.1 Flash Lite, not 3.5 Flash-Lite. Section 2 shows Grok results moving between 4.6 and 4.7, so family results should not be assumed to carry over.

### Gaps
- No current-model score on any real or practice AWS, Azure or GCP architect exam was found.
- No Azure or GCP architect result newer than the 2023 Noever paper was found.
- The MDPI paper "An Empirical Evaluation of LLMs Applying Software Architectural Patterns" ([DOI](https://doi.org/10.3390/ai7060195)) returned 403, so its models and scores are unknown.

---

## Which benchmarks measure professional judgement or knowledge work on a common scale, and what are the scores?

### Takeaway
Each benchmark gives a common scale only within one version, and none of them tests architecture judgement directly. The target models also rank very differently across benchmarks: among them, Grok 4.7 and DeepSeek V4.1 Flash 1017 score highest on knowledge-work deliverables, while Gemini 4 Argon and Gemini 3.8 Flash score highest on most reasoning-style tests and human preference votes.

### Cited Findings

#### What each API ID maps to

| API ID | What the benchmarks tested | Effort settings | Notes |
|---|---|---|---|
| `grok-4.7` | Grok 4.7, released 21 Sep 2026 | low, medium, high, xhigh; default high — [xAI docs](https://docs.x.ai/developers/models/grok-4.7) | Text and image input. AA lists the maker as SpaceXAI — [AA](https://artificialanalysis.ai/models/grok-4-7) |
| `qwen/qwen3.8-27b` on Groq | Other hosts, not Groq. [AA's provider list](https://artificialanalysis.ai/models/qwen3-8-27b/providers) names 10 providers and Groq is not one | Groq: none, default, low, medium, high; context 131,072; max output 16,384; preview status; max 3 images — [Groq docs](https://console.groq.com/docs/model/qwen/qwen3.8-27b) | The model's own default is xhigh — [Hugging Face](https://huggingface.co/Qwen/Qwen3.8-27B). Groq's page does not say what "default" maps to |
| `deepseek-flash` | Now serves V4.1 Flash **1017** (since 17 Oct 2026) — [DeepSeek changelog](https://api-docs.deepseek.com/updates) | low, high, max; default high; medium and xhigh run as high — [DeepSeek docs](https://api-docs.deepseek.com/guides/thinking_mode) | Base V4.1 Flash is deprecated on [AA](https://artificialanalysis.ai/models/deepseek-v4-1-flash). Arena lists only the 20260910 build |
| `gemini-3.8-flash` | Gemini 3.8 Flash, released 2 Sep 2026 | low, medium, high; `minimal` returns an error; default not stated — [Google docs](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash) | Text, image, video, audio, PDF |
| Flash-Lite | Newest is Gemini 3.5 Flash-Lite. Pricing page lists 3.5, 3.1 and 2.5; no 3.8 Flash-Lite — [Google pricing](https://ai.google.dev/gemini-api/docs/pricing) | ARC tested minimal to high; [AA](https://artificialanalysis.ai/models/gemini-3-5-flash-lite) states no effort level | Text, image, speech, video |
| `gemini-4-argon` | Gemini 4 Argon. Announced 30 Sep 2026 — [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/); Vals dates it 13 Oct 2026 — [Vals](https://www.vals.ai/models/google_gemini-4-argon) | low, medium, high; default not stated by Google — [Google docs](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon). A secondary source says the API defaults to medium — [Oasis](https://joinoasis.com/blog/gemini-4-argon-review) | AA tested High only |
| `deepseek-v4-pro` (reference) | DeepSeek V4 Pro 0813 (variants 0424 and 0813 exist) | Not checked per variant | **Text only:** "does not support image input" — [AA](https://artificialanalysis.ai/models/deepseek-v4-pro) |

#### Artificial Analysis (AA): version facts

- Intelligence Index v5.0 was announced 27 Oct 2026 and has nine evaluations in four categories at 25% each. Knowledge Work is AA-Briefcase v1.1 (15%), AutomationBench-AA (5%) and GDP.pdf (5%) — [AA announcement](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5); [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).
- GDPval-AA v2.1 is now standalone. It "was removed from the Intelligence Index in v5.0, having been a constituent up to and including v4.3.2" — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).
- GDPval-AA v2.1 is Elo, anchored by pinning DeepSeek V4.1 Flash (max) at 1600. AA-Briefcase v1.1 is Elo, anchored to GPT-5.5 (medium) at 1000. The two Elo scales therefore have different anchors and cannot be read against each other — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).
- AA-Briefcase covers multi-week business workflows producing spreadsheets, presentations and memos, graded by rubric and pairwise comparison — [AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase). GDPval-AA covers 44 occupations with blind pairwise comparison — [AA evaluations](https://artificialanalysis.ai/evaluations).
- AA's methodology does not state how contestant effort variants are chosen. Variants are listed separately. Temperature is 0 for non-reasoning models and 0.6 for reasoning models unless the lab recommends otherwise — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).

#### AA scores: Intelligence Index v5.0, AA-Briefcase v1.1, GDPval-AA v2.1

Sources: [AA leaderboard](https://artificialanalysis.ai/leaderboards/models), [AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase), [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa). Confidence intervals are roughly ±10 for Briefcase and ±20 for GDPval-AA.

| Model (effort) | Index v5.0 | Cost per Index task | Briefcase v1.1 | GDPval-AA v2.1 |
|---|---|---|---|---|
| Gemini 4 Argon (High) | 50 | $7.68 | 1484 | 1631 |
| Grok 4.7 (High) | 35 | $6.18 | 1629 | 1716 |
| Grok 4.7 (Xhigh) | 34 | $7.51 | 1638 | 1718 |
| Grok 4.7 (Low) | 31 | $2.92 | 1495 | 1591 |
| DeepSeek V4.1 Flash 1017 (Max) | 32 | $0.60 | 1570 | 1746 |
| DeepSeek V4.1 Flash 1017 (Non-reasoning) | 19 | not shown | 1426 | not shown |
| DeepSeek V4.1 Flash base (Max), deprecated | N/A on [model page](https://artificialanalysis.ai/models/deepseek-v4-1-flash) | N/A | 1417 | 1600 (anchor) |
| DeepSeek V4.1 Flash base (Non-reasoning) | not shown | not shown | 1119 | 1349 |
| Gemini 3.8 Flash (High) | 31 | $7.77 | 1203 | 1445 |
| Gemini 3.8 Flash (Medium) | 30 | $6.26 | 1183 | 1431 |
| Gemini 3.8 Flash (Low) | 22 | not shown | 1062 | 1316 |
| Qwen3.8 27B (Xhigh) | 20 | $3.53 | 1393 | 1427 |
| Qwen3.8 27B (Medium) | 17 | $2.16 | 1373 | 1389 |
| Qwen3.8 27B (Low) | 16 | $1.91 | 1270 | 1370 |
| Qwen3.8 27B (Non-reasoning) | 10 | $3.77 | 901 | 1082 |
| DeepSeek V4 Pro 0813 (Max), reference | 23 | $1.77 | 1254 | 1457 |
| DeepSeek V4 Pro 0813 (Non-reasoning), reference | not shown | not shown | 928 | 1066 |
| DeepSeek V4 Pro 0424 (Max), reference | not shown | not shown | 922 | 1166 |
| Gemini 3.5 Flash-Lite (effort not stated) | 12 | $0.69 | 651 | 995 |
| Gemini 3.1 Flash-Lite | not listed | not listed | 208 | 438 |

- Reference top scores: Index v5.0 Gemini 4 Carbon (High) 59 and Claude Opus 5.5 (Max) 58 — [AA Index page](https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index). The announcement names Opus 5.5 at 58 as top, so Carbon appears to have been added after it — [AA announcement](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5). AA-Briefcase top: Claude Sonnet 5.5 (Max) 1814. GDPval-AA top: Claude Opus 5.5 (Max) 1866 — [AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase); [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa).

#### AA per-evaluation scores inside Index v5.0

Sources: [Grok vs Gemini 3.8 Flash](https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-gemini-3-8-flash), [Argon vs DeepSeek 1017](https://artificialanalysis.ai/models/comparisons/gemini-4-argon-vs-deepseek-v4-1-flash-1017), [Qwen vs Gemini 3.8 Flash](https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-gemini-3-8-flash), [Flash-Lite vs Gemini 3.8 Flash](https://artificialanalysis.ai/models/comparisons/gemini-3-5-flash-lite-vs-gemini-3-8-flash).

| Evaluation | Argon (High) | Grok 4.7 (High) | DeepSeek 1017 (Max) | Gemini 3.8 Flash (High) | Qwen3.8 27B (Xhigh) | Gemini 3.5 Flash-Lite |
|---|---|---|---|---|---|---|
| AutomationBench-AA (a guardrail violation scores 0) | 78% | 64% | 67% | 60% | 48% | 25% |
| GDP.pdf (all-pass, long professional documents) | 22% | 23% | 17% | 21% | 16% | 14% |
| HLE-Diamond (no tools, reasoning and knowledge) | 57% | 24% | 25% | 33% | 15% | 10% |
| CritPt v2 Hard Subset | 53% | 35% | 24% | 44% | 4% | 4% |
| AA-Omniscience v1.1 (net score, −100 to 100; wrong answers penalised) | 46 | 30 | 1 | 23 | −6 | 7 |
| FrontierCode 2.0 | 26% | 28% | 28% | 19% | 15% | 6% |
| Terminal-Bench 4.0 | 57% | 25% | 34% | 20% | 6% | 1% |
| Terminal-Bench-Science 0.1 | 53% | 10% | 13% | 10% | 0% | 0% |

- Omniscience scoring: 0 means as many correct as incorrect answers; refusals are not penalised. Argon has the lowest listed hallucination rate at 4% — [AA-Omniscience](https://artificialanalysis.ai/evaluations/omniscience).
- The closest AA evaluation to cloud operations is ITBench-AA (Kubernetes incident root-cause analysis, 59 tasks). Of the target models only Gemini 3.8 Flash (High) appears in the fetched content, at 52.5%, against a top score of 56.2% — [ITBench-AA](https://artificialanalysis.ai/evaluations/itbench-aa).
- The [DeepSeek V4.1 Flash vs Gemini 3.8 Flash comparison](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-vs-gemini-3-8-flash) shows single values on some rows, including the Index. These match Gemini's numbers, so I did not assign them to DeepSeek.

#### LiveBench 2.0, release 2026-10-14 (read from the site's own data files)

LiveBench 2.0 is a new edition, and a third-party page states that scores are not comparable with v1 — [DataLearner](https://www.datalearner.com/benchmarks/livebench-2-0). The Reasoning suite is 202 short logic, spatial and theory-of-mind questions with one correct answer, scored from a single run, with models at their highest supported effort — [notes.json](https://livebench.ai/data/20261014/notes.json). The v1 GitHub README still names 2025-04-25 as current, so it is out of date — [LiveBench README](https://raw.githubusercontent.com/LiveBench/LiveBench/main/README.md).

Sources: [table.csv](https://livebench.ai/data/20261014/table.csv), [breakdown.json](https://livebench.ai/data/20261014/breakdown.json). Overall is my mean of the seven suites and matches [DataLearner's](https://www.datalearner.com/benchmarks/livebench-2-0) listed values. Effort labels come from the [site bundle](https://livebench.ai/).

| Model (effort) | Overall | Reasoning | Rank of 55 on Reasoning | Theory of mind | Zebra puzzles | Spatial | Logic with navigation |
|---|---|---|---|---|---|---|---|
| Gemini 4 Argon (high) | 84.10 | 95.1 | 1 | 92.3 | 100.0 | 100.0 | 88.0 |
| Gemini 3.8 Flash (high) | 67.34 | 89.3 | 18 | 76.9 | 98.2 | 100.0 | 82.0 |
| DeepSeek V4.1 Flash 1017 (max) | 79.20 | 89.1 | 20 | 88.5 | 100.0 | 98.0 | 70.0 |
| DeepSeek V4.1 Flash base (max) | 78.04 | 86.7 | 28 | 80.8 | 100.0 | 98.0 | 68.0 |
| Grok 4.7 (xhigh) | 74.09 | 82.7 | 38 | 84.6 | 86.0 | 94.0 | 66.0 |
| Grok 4.6 (older, reference) | 74.94 | 91.2 | 9 | 90.4 | 96.5 | 98.0 | 80.0 |
| Qwen3.8 27B ("max" in LiveBench metadata) | 62.66 | 80.0 | 42 | 59.6 | 96.5 | 96.0 | 68.0 |

- Absent from table.csv: every Gemini Flash-Lite model, DeepSeek V4 Pro, and Gemini 4 Carbon — [table.csv](https://livebench.ai/data/20261014/table.csv).
- The last v1 release listed in the site bundle is 2026-06-25, before every target model's release, so v1 cannot hold scores for them — [LiveBench](https://livebench.ai/).

#### Arena (formerly LMArena) text leaderboards, dated 27 Oct 2026

Arena scores are human preference votes, not accuracy, and each category is computed separately. Format is rank, score ± interval. Sources: [Overall](https://arena.ai/leaderboard/text), [Expert](https://arena.ai/leaderboard/text/expert), [Hard Prompts](https://arena.ai/leaderboard/text/hard-prompts), [Hard Prompts English](https://arena.ai/leaderboard/text/hard-prompts-english), [Software & IT](https://arena.ai/leaderboard/text/industry-software-and-it-services), [Business, Management & Financial Ops](https://arena.ai/leaderboard/text/industry-business-and-management-and-financial-operations).

| Model as listed | Overall | Expert | Hard Prompts | Hard (English) | Software & IT | Business |
|---|---|---|---|---|---|---|
| Gemini 4 Argon (High) | #2 1520±6 | #4 1541±17 | #2 1544±8 | #2 1543±12 | #2 1550±10 | #2 1512±14 |
| Gemini 3.8 Flash (High), Preliminary | #10 1496±4 | #16 1527±9 | #11 1517±5 | #14 1514±7 | #23 1518±6 | #28 1482±7 |
| DeepSeek-V4.1-Flash-20260910 (Max) | #35 1476±6 | #23 1516±15 | #37 1499±7 | #30 1504±11 | #27 1514±9 | #30 1478±12 |
| DeepSeek-V4-Pro | #65 1458±4 | #78 1479±8 | #66 1480±5 | #68 1484±6 | #72 1491±5 | #62 1459±7 |
| Gemini 3.5 Flash-Lite | #71 1456±4 | #93 1470±10 | #76 1475±5 | #81 1477±7 | #78 1489±6 | #72 1454±8 |
| Grok 4.7 (xHigh) | #96 1441±6 | #76 1480±15 | #91 1463±7 | #86 1473±10 | #100 1478±9 | #112 1437±12 |
| Qwen3.8-27B | #106 1436±5 | #83 1476±11 | #100 1460±6 | #117 1458±8 | #84 1486±7 | #108 1439±9 |
| Gemini 3.1 Flash-Lite Preview | #112 1433±4 | #128 1445±8 | #126 1445±4 | #143 1442±6 | #136 1455±5 | #130 1420±6 |

- Expert prompts are about 5.5% of all prompts and are tagged from prompt text by an LLM. Occupational tagging is also LLM-based — [Arena Expert post](https://arena.ai/blog/arena-expert/).
- Vote counts are small for some entries: Argon Expert 1,219 votes, Grok 4.7 Expert 1,606 — [Expert](https://arena.ai/leaderboard/text/expert).

#### Vals Index v2.2 (updated 29 Oct 2026; v2.2 released 19 Oct)

The index is GDP-weighted: Finance 8.0, Coding 5.6, Legal 1.2, Tax 0.5. It is not an architecture measure — [Vals Index](https://www.vals.ai/benchmarks/vals_index).

| Model | Vals Index v2.2 | Rank of 32 |
|---|---|---|
| Gemini 4 Argon (high) | 69.24% ±1.09 | 4 |
| DeepSeek V4.1 Flash 1017 (max) | 61.26% ±1.05 | 10 |
| Grok 4.7 (xhigh) | 58.56% ±1.01 | 15 |
| Gemini 3.8 Flash (high) | 55.95% ±1.14 | 18 |
| DeepSeek V4 Pro 0813 | 52.97% | 23 |

Sources: [Vals Index](https://www.vals.ai/benchmarks/vals_index), [Argon](https://www.vals.ai/models/google_gemini-4-argon), [1017](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash-1017), [Grok 4.7](https://www.vals.ai/models/grok_grok-4.7), [Gemini 3.8 Flash](https://www.vals.ai/models/google_gemini-3.8-flash).

- Not on v2.2: Qwen3.8 27B, Flash-Lite and base V4.1 Flash. Their pages show 53.54% (no rank), 36.71% (#29 of 43) and 57.86% (#15 of 56). The different pool sizes suggest earlier index runs, though the pages do not state a version, so these do not belong in the table above — [Qwen](https://www.vals.ai/models/alibaba_qwen3.8-27b); [Flash-Lite](https://www.vals.ai/models/google_gemini-3.5-flash-lite); [V4.1 Flash](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash).
- Name trap: Vals "SRE Bench" means software **reverse engineering**, not site reliability. It says nothing about cloud operations — [SRE Bench](https://www.vals.ai/benchmarks/srebench).

#### MCQ-format benchmarks on exact models (nearest format match, but academic subjects)

| Model | Vals MMLU Pro | Vals GPQA Diamond | Vals MMMU Pro (image MCQ) |
|---|---|---|---|
| Gemini 3.8 Flash (high) | 90.22% ±0.29 (5/138) | 94.44% ±1.48 (4/138) | 89.08% ±0.75 (4/93) |
| DeepSeek V4 Pro 0813 | 86.97% | 92.42% | not checked |
| Gemini 3.1 Flash-Lite Preview | 86.24% | 81.06% | not checked |
| Gemini 3.5 Flash-Lite (high) | 85.84% ±0.34 (54/138) | 83.84% ±1.85 (56/138) | 83.58% ±0.89 (30/93) |
| Qwen3.8 27B (xhigh) | 84.34% ±0.36 (65/138) | 88.89% ±1.58 (33/138) | 83.93% ±0.88 (28/93) |
| Grok 4.7, DeepSeek V4.1 Flash, Gemini 4 Argon | Absent | Absent | Absent |

Sources: [MMLU Pro](https://www.vals.ai/benchmarks/mmlu_pro), [GPQA](https://www.vals.ai/benchmarks/gpqa), [Gemini 3.8 Flash](https://www.vals.ai/models/google_gemini-3.8-flash), [Flash-Lite](https://www.vals.ai/models/google_gemini-3.5-flash-lite), [Qwen](https://www.vals.ai/models/alibaba_qwen3.8-27b).

- Vals has stopped these runs: "we no longer run this benchmark on new model releases" (MMLU Pro), and GPQA is archived because performance "has saturated". Both pages are dated 1 Sep 2026, so later models are missing. That date is one day before Gemini 3.8 Flash's listed release, and the pages do not explain this — [MMLU Pro](https://www.vals.ai/benchmarks/mmlu_pro); [GPQA](https://www.vals.ai/benchmarks/gpqa).
- AA also shows Gemini 3.8 Flash (High) at 95.3% on GPQA Diamond, and Grok 4.7, Argon and the DeepSeek models are absent from the fetched text — [AA GPQA](https://artificialanalysis.ai/evaluations/gpqa-diamond).
- A fresh 198-question independent run of Qwen3.8 27B gave 89.9% at xhigh — [Quesma](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/).

#### ARC-AGI-2 Semi-Private (visual puzzle reasoning, read from ARC Prize's data file)

The leaderboard HTML does not expose rows, so I read its [evaluations.json](https://arcprize.org/media/data/evaluations.json). Values are share solved, then cost per task.

| Model | None / Minimal | Low | Medium | High | Top setting |
|---|---|---|---|---|---|
| Gemini 4 Argon | n/a | 42.1%, $0.074 | 87.1%, $0.137 | 91.3%, $0.325 | High |
| Gemini 3.8 Flash | n/a | 77.5%, $0.154 | 82.9%, $0.248 | 89.2%, $0.400 | High |
| DeepSeek V4.1 Flash 1017 | 2.1%, $0.010 | 73.6%, $0.134 | n/a | 68.6%, $0.147 | Max 78.1%, $0.163 |
| Grok 4.7 | n/a | 16.7%, $0.174 | 58.8%, $1.476 | 58.3%, $1.549 | Xhigh 61.4%, $2.015 |
| DeepSeek V4 Pro 0813 (reference) | 0.8%, $0.040 | 56.3%, $0.370 | n/a | 59.7%, $0.597 | Max 61.3%, $0.598 |
| Qwen3.8-27B | 1.5%, $0.059 | 22.8%, $0.238 | 13.2%, $0.286 | n/a | Xhigh 42.4%, $0.447 |
| Gemini 3.5 Flash-Lite | 0.8%, $0.014 | 1.5%, $0.017 | 5.3%, $0.044 | 10.3%, $0.139 | High |

#### Conflicting numbers already in circulation (do not mix)

- Gemini 3.8 Flash on AA's Index: 59 on launch day, version not stated — [eesel](https://www.eesel.ai/blog/gemini-3-8-flash); 41 in a search snapshot of an AA comparison page, version not shown — [AA comparison](https://artificialanalysis.ai/models/comparisons/deepseek-v4-1-flash-vs-gemini-3-8-flash); **31 on v5.0** — [AA](https://artificialanalysis.ai/models/gemini-3-8-flash). These are index-version changes, not model changes.
- DeepSeek V4.1 Flash (Max): 45 reported on v4.3.2 — [Zeli](https://zeli.app/story/50148452); 39 in the same AA snapshot above. I could not resolve this, and the model page now shows N/A.
- Gemini 4 Argon: 52.6 (secondary, version not stated) — [NeuralTrust](https://neuraltrust.ai/blog/gemini-4-argon); 50 on v5.0 — [AA](https://artificialanalysis.ai/models/gemini-4-argon).
- Gemini 3.8 Flash GDPval: 1545 on **v2** — [Google model card](https://deepmind.google/models/model-cards/gemini-3-8-flash/); 1445 on **v2.1** — [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa). V2.1 changed how the Elo scale is fixed, so these are not comparable.
- Vals Index: Argon 68.90% (#1 of 41, 30 Sep update) vs 69.24% (#4 of 32) — [Vals](https://www.vals.ai/models/google_gemini-4-argon). Grok 4.7 60.22% (#10 of 59) vs 58.56% (#15 of 32) — [Vals](https://www.vals.ai/models/grok_grok-4.7).
- AA does not say whether v4 and v5 scores are comparable, but composition and weights both changed — [AA methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking).

### Inferences
- There is no single "judgement" ranking. Argon leads or nearly leads the reasoning and preference tests but sits below Grok 4.7 and DeepSeek 1017 on both AA-Briefcase and GDPval-AA. Gemini 3.8 Flash is near the top on reasoning-style tests and lower on agentic deliverables. A report should describe these as different skills.
- For scenario MCQs, reasoning-style, factual-recall and hard-prompt results are closer in shape than multi-week agentic deliverables, because an MCQ is a single, short, tool-free decision. This is my judgement. On that reading the most relevant fields are LiveBench Reasoning, HLE-Diamond, AA-Omniscience and Arena Software & IT. AA-Briefcase and GDPval-AA measure document production and project work more than choosing among options.
- AA-Omniscience may matter specifically for "which service" questions, since these depend on remembering product facts. DeepSeek 1017 at 1 and Qwen3.8 27B at −6 sit well below Argon at 46 and Grok 4.7 at 30. The dataset is not about cloud products, so this is suggestive only.
- MCQ format compresses gaps here too. Gemini 3.5 Flash-Lite trails Gemini 3.8 Flash by only 4.38 points on MMLU Pro but by 552 Elo on AA-Briefcase and 450 on GDPval-AA, which matches the SAKE and CAKE pattern.
- LiveBench Reasoning differences under about 5 points are likely noise for one run of 202 questions at this accuracy level (my calculation: 95% margin near ±4.9 points at 85%). So Gemini 3.8 Flash and DeepSeek 1017 are effectively tied there, while Argon's lead over Grok 4.7 and Qwen3.8 27B is larger than noise.
- Grok 4.7 scored below Grok 4.6 on LiveBench Reasoning (82.7 vs 91.2), while its knowledge-work scores are high. The evidence does not show why. This is one run, but the gap is larger than the noise estimate.
- Evidence strength: strong for the benchmark numbers themselves, since they come from primary pages or data files; weak for transfer to architecture MCQs, since none of these benchmarks covers that subject.

### Gaps
- AA does not publish a per-model Knowledge Work sub-score that I could reach.
- Arena's Grok 4.7 entry is xHigh only, and Qwen3.8-27B's effort and host are not labelled.
- Arena has not listed the 1017 build that `deepseek-flash` now serves.
- HLE-Diamond, GDP.pdf and AutomationBench-AA leaderboard pages rendered only the top entries, so target-model values come from AA comparison pages.
- AA-Omniscience, AutomationBench-AA and other per-evaluation scores for Grok 4.7 Xhigh and for lower-effort variants were not visible.
- The ARC HTML did not show a Verified or Community label per row, so I cannot state which tab each row belongs to.

---

## Are there independent system design head-to-heads on these exact models, and what weaknesses did they find?

### Takeaway
I found no independent system design or cloud architecture head-to-head on these exact models. The nearest evidence is small hands-on tests of related skills, plus older research; together they point to over-building, adding popular components nobody asked for, and doing better on familiar problem wording than on the same problem rephrased.

### Cited Findings

#### Exact-model tests (none is a system design test)

- **DeepSeek V4.1 Flash vs Gemini 3.8 Flash** (DataCamp, 17 Sep 2026). One prompt for a single-file HTML scheduler, both at `high`, one attempt each. DeepSeek scored 5/5/5 and Gemini 4/5/4. Both got the conflict logic right, but Gemini added unrequested panels that hurt the layout it was graded on. The article states it covers only stateful UI and overlap logic. It tested the base model, not 1017 — [DataCamp](https://www.datacamp.com/blog/deepseek-v4-1-flash-vs-gemini-3-8-flash).
- **Grok 4.7 vs Grok 4.6** (Puter, 25 Sep 2026). Five runs per prompt per model, default effort, code graded by execution. Both scored 5/5 on a familiar median-function bug task, but only 2.4/5 and 2.0/5 on the same five bugs rephrased as `mid(xs)`. The author reads this as recall of a familiar snippet. In one Grok 4.7 run the model named a defect and shipped the code anyway. No detectable self-checking difference was found, and two of three tests saturated — [Puter](https://developer.puter.com/blog/grok-4-7-review/).
- **Gemini 4 Argon** (Oasis, 14 Oct 2026). Four tasks with checkable answers, one response each. Argon returned NO-GO when a gate failed, ignored embedded override text, and found the only feasible order of 24 in a scheduling task. It exceeded a 180-word limit once a table was counted. The author warns against treating this as a reliability score, and the article has internal count inconsistencies — [Oasis](https://joinoasis.com/blog/gemini-4-argon-review).
- **Qwen3.8 27B** (Simon Willison, 16 Aug 2026, local Q4_K_M build, not Groq). At xhigh it spent several minutes planning an elaborate animated design for "draw an svg of a circle", "entirely not what I had asked for", and built an over-engineered tool with unrequested features — [Willison](https://simonwillison.net/2026/Aug/16/qwen-38-27b/).
- **Gemini 3.8 Flash** anecdotes conflict: a Google DeepMind staff member says it verifies its work more often, one developer says it cannot test its own work, and another calls it unusable for software engineering. None is a controlled test — [eesel](https://www.eesel.ai/blog/gemini-3-8-flash).
- A secondary summary of a Grok 4.7 video review reports more than twice the output tokens of Grok 4.6 for a small gain, plus looping behaviour — [daily.dev](https://daily.dev/posts/grok-4-7-fully-tested-this-is-actually-sad-worst-than-glm-5-3-flash--zu0g0lmcu). The token claim fits LiveBench's measured data (section 4). The looping claim is unverified.
- Pages that looked relevant but contained no tests: [Layer3Labs Grok review](https://www.layer3labs.io/guides/grok-4-7-review) reports no measurements. [eesel Grok review](https://www.eesel.ai/blog/grok-4-7-review) documents no test, repeats xAI's table, and has a commercial interest.

#### Research on the named weaknesses (OLDER models, not target models)

- **Adding popular components not required.** On OpenAI o3 generating microservice designs from requirements (run May and June 2025, two small systems, one run each), experts flagged "connecting everything with everything", an "Auth service" appearing "without an explicit requirement", and an API Gateway that "doesn't seem to come strictly from the requirements". Zero-shot inter-service F1 was 0.61 and few-shot 0.82 — [Albuquerque et al.](https://arxiv.org/html/2607.28307).
- **Ignoring a stated constraint.** MS Copilot in a trade-off analysis exercise raised cost and usability trade-offs that participants were told to ignore, and it flagged risks for almost every scenario without judging criticality. One model, one case study, no statistical analysis — [Capilla et al.](https://arxiv.org/html/2603.28914v1).
- **Preferring one vendor.** Across seven older models and about 591,000 valid responses, median provider bias (Gini) was 0.80. In a cloud hosting example Amazon exceeded 30% while Azure was 2%, against cited market shares of 32% and 23%. Chain-of-thought and debiasing prompts did not meaningfully reduce it. In over 90% of scenarios, the providers models ranked in conversation did not correlate with what they generated — [Zhang et al.](https://arxiv.org/html/2501.07849v1). This is code generation, not MCQ.
- **Defaulting to the familiar.** A search summary of an ACL 2026 study reports libraries such as NumPy overused in up to 48% of cases, with Python chosen even where it was not the best fit — [llm-code-bias](https://github.com/itsluketwist/llm-code-bias/). I read this only through a search summary.
- **LLM-based architecture reviews depend on input quality.** A Fraunhofer study found LLM and expert reviews agreed more as document quality rose. I read this only through a search summary — [arXiv 2601.19693](https://arxiv.org/pdf/2601.19693).

#### Research on MCQ formats that make "several options look right" harder (OLDER models)

- When "None of the above" was correct, 28 LLMs on MMLU dropped 30–50% regardless of scale, including 48.1% on business ethics and 14.6% on mathematical reasoning — [Tam et al.](https://arxiv.org/abs/2503.01550).
- On "select all that apply" questions, the strongest of 27 models reached only 41.8% exact match, with selection bias and count bias named as causes. Domains were reading comprehension, law and biomedicine — [SATA-Bench](https://arxiv.org/abs/2506.00643v3).
- Option order can change answers, and accuracy and order sensitivity do not always move together — [Hanna and Feng](https://arxiv.org/abs/2608.11947). Search summaries of related work say option-order effects vary by benchmark — [arXiv 2308.11483](https://arxiv.org/pdf/2308.11483). One paper's title makes the claim that LLMs may answer by [selecting the least incorrect option](https://arxiv.org/html/2402.01349v3); I did not read it in full.

### Inferences
- The Puter result, the o3 expert comments and the provider-bias data all point the same way: models lean toward a familiar shape of answer. Whether target models do this on cloud MCQs is untested. The Puter test is the only exact-model evidence, and it is code rather than architecture.
- SAP-C02's multiple-response format matches the format SATA-Bench found hardest, so single-answer benchmarks may overstate performance on those items. SATA-Bench did not test cloud content.
- Over-building at high effort (Gemini 3.8 Flash at `high`, Qwen3.8 27B at xhigh) may not cost marks on an MCQ, where the answer is one letter. The same habit could still appear as favouring the option with more components. That link is speculation and needs testing.
- Provider-bias findings suggest AWS, Azure and GCP questions may not be equally reliable for the same model. No data exists on this for target models.
- Evidence strength for exact-model weaknesses is weak: every test is small, short and outside architecture.

### Gaps
- No test on these exact models of ignoring a stated constraint in an architecture scenario.
- No test on these exact models of picking a popular service over the better-fitting one.
- No data on whether Gemini models favour GCP or other models favour AWS in MCQ settings.
- IFBench, the nearest constraint-following benchmark, has no target model on the AA page — [AA IFBench](https://artificialanalysis.ai/evaluations/ifbench). Qwen reports 79.5 for itself, which is vendor-reported — [Hugging Face](https://huggingface.co/Qwen/Qwen3.8-27B).
- The 36Kr Gemini 3.8 Flash review appeared only as a search snippet, about a repository-wiki task rather than system design — [36Kr](https://eu.36kr.com/en/p/3968466249068804).

---

## Does higher reasoning effort improve accuracy on this kind of question, and what does it cost?

### Takeaway
Turning reasoning on gives the biggest gain on every target model where off-versus-on was measured, and top-tier settings usually add little more for a large token cost. The only exact-model MCQ-by-effort data is Quesma's GPQA run on Qwen3.8 27B, where low, medium and xhigh have overlapping confidence intervals; no target model has effort data on architecture questions.

### Cited Findings

#### Exact-model effort data: AA (knowledge work, not MCQ)

Sources: [AA leaderboard](https://artificialanalysis.ai/leaderboards/models), [AA-Briefcase](https://artificialanalysis.ai/evaluations/aa-briefcase), [GDPval-AA](https://artificialanalysis.ai/evaluations/gdpval-aa). Raw values are in section 2.

| Model and step | Index v5.0 change | Briefcase v1.1 change | GDPval-AA v2.1 change | Cost per Index task |
|---|---|---|---|---|
| Qwen3.8 27B, none to low | +6 | +369 | +288 | $3.77 to $1.91 |
| Qwen3.8 27B, low to medium | +1 | +103 | +19 | $1.91 to $2.16 |
| Qwen3.8 27B, medium to xhigh | +3 | +20 | +38 | $2.16 to $3.53 |
| DeepSeek 1017, none to max | +13 | +144 | not shown | not shown to $0.60 |
| DeepSeek V4.1 Flash base, none to max | not shown | +298 | +251 | not shown |
| DeepSeek V4 Pro 0813, none to max (reference) | not shown | +326 | +391 | not shown to $1.77 |
| Grok 4.7, low to high | +4 | +134 | +125 | $2.92 to $6.18 |
| Grok 4.7, high to xhigh | −1 | +9 (within interval) | +2 (within interval) | $6.18 to $7.51 |
| Gemini 3.8 Flash, low to medium | +8 | +121 | +115 | not shown to $6.26 |
| Gemini 3.8 Flash, medium to high | +1 | +20 | +14 (within interval) | $6.26 to $7.77 |

- Qwen3.8 27B's non-reasoning cost of $3.77 is higher than its low-effort cost of $1.91. This is as listed on the leaderboard, and AA gives no explanation — [AA leaderboard](https://artificialanalysis.ai/leaderboards/models).
- AA reports for other models that "Effort settings matter more in v5 than in v4.3". Claude Opus 5.5 scores 35 at low and 58 at max at 10x the cost — [AA announcement](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5).

#### Exact-model effort data: ARC-AGI-2 (reasoning puzzles)

See the table in section 2 — [evaluations.json](https://arcprize.org/media/data/evaluations.json). Main points from that data:
- Medium is where Argon jumps (42.1% at low, 87.1% at medium), and high adds 4.2 points at 2.4x the cost per task.
- Grok 4.7 jumps from low to medium, then stays flat: 58.8% medium, 58.3% high, 61.4% xhigh, with cost rising from $1.48 to $2.01.
- More effort does not always help. Qwen3.8-27B scores 22.8% at low and 13.2% at medium; DeepSeek 1017 scores 73.6% at low and 68.6% at high.

#### Exact-model MCQ effort data: Qwen3.8 27B on GPQA Diamond (198 four-option questions)

Self-hosted llama.cpp run, 21 Aug 2026 chart date, not Groq. Percentages with 95% intervals, read from the page's embedded chart data — [Quesma](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/).

| Build | Low | Medium | Xhigh |
|---|---|---|---|
| BF16 (full) | 86.4% (81–90) | 83.3% (77–88) | 89.9% (85–93) |
| Q8_0 | 82.3% (76–87) | 81.3% (75–86) | 89.8% (85–93) |
| Q4_K_M | 81.7% (76–86) | 83.3% (77–88) | 90.4% (85–94) |

- The article says thinking level "changed the score drastically" and that the best result needed "around 8k reasoning tokens" — [Quesma](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/).
- The table is less dramatic than that wording: on BF16 the three intervals overlap, and medium is below low. At 1-bit quantization longer reasoning hurt: scores fell at xhigh and 46–64% of final answers were empty — [Quesma](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/).

#### Token and cost data on short single-answer questions: LiveBench 2.0 Reasoning, highest effort

Sources: [cost.csv](https://livebench.ai/data/20261014/cost.csv), [table.csv](https://livebench.ai/data/20261014/table.csv). Per-question cost is my division of suite cost by 202. I read `out_reasoning` as mean output tokens per question, because tokens × output price × 202 closely reproduces the listed suite cost.

| Model | Reasoning score | Mean output tokens per question | Cost per question |
|---|---|---|---|
| Gemini 4 Argon | 95.1 | 7,571 | $0.078 |
| DeepSeek 1017 | 89.1 | 19,909 | $0.024 |
| Qwen3.8 27B | 80.0 | 24,786 | $0.075 at Alibaba list price |
| DeepSeek V4.1 Flash base | 86.7 | 37,763 | $0.046 |
| Gemini 3.8 Flash | 89.3 | 39,118 | $0.148 |
| Grok 4.7 | 82.7 | 63,769 | $0.385 |
| Grok 4.6 (older, reference) | 91.2 | 14,139 | $0.087 |

- Vals' GPQA run lists 16.51k tokens and 116.36 s for Qwen3.8 27B, and 8.37k tokens and 20.18 s for Gemini 3.8 Flash — [Vals GPQA](https://www.vals.ai/benchmarks/gpqa). The token definition is not stated.
- Argon's listed price in LiveBench's file is $2/$12, but the arithmetic fits $10 output, which matches Google's rate — [cost.csv](https://livebench.ai/data/20261014/cost.csv); [Google pricing](https://ai.google.dev/gemini-api/docs/pricing).
- Prices change soon. Argon goes from $2/$10 to $4/$20 on 1 Dec 2026, and Gemini 3.8 Flash from $0.75/$3.75 to $1.50/$7.50 on 1 Jan 2027. Output price includes thinking tokens — [Google pricing](https://ai.google.dev/gemini-api/docs/pricing). AA's Argon page already shows $4/$20 — [AA](https://artificialanalysis.ai/models/gemini-4-argon).
- Groq's Qwen list price is $0.80/$4.00, against $0.50/$3.00 on Alibaba's API — [Groq docs](https://console.groq.com/docs/model/qwen/qwen3.8-27b); [AA](https://artificialanalysis.ai/models/qwen3-8-27b).
- Qwen3.8 27B at its default xhigh used 22,276 reasoning tokens on one drawing prompt, and Willison advises low or no reasoning at first — [Willison](https://simonwillison.net/2026/Aug/16/qwen-38-27b/).

#### MCQ effort research (OLDER models)

- **ReasonLab** (IBM, v2 22 Sep 2026; 480,927 evaluations, 10 MCQ datasets, 27 configurations). No reasoning to low: GPT-5-4 went from 61.20% to 73.37%. Low to medium added 0.48–2.10 points for an eightfold budget increase. Models used only 7–20% of the medium budget, 590–1,611 tokens per question. Claude Sonnet 4 at low equalled no reasoning. The authors conclude that enabling reasoning is the main lever — [ReasonLab](https://arxiv.org/html/2607.14109v2).
- **QuArch.** GPT-5.2 beat non-reasoning GPT-5 by 24%, 22% and 33% on analyze, design and implement questions, against 2% on recall — [QuArch](https://arxiv.org/html/2510.22087v2).
- **CAKE.** Chain-of-thought on architecture MCQs was mixed: Llama 3.2 1B +38.5 points, Mistral 3.1 3B −13.1 points. Free-response mostly rose 0.15–0.42 out of 5, and latency rose about 3–7x — [CAKE](https://arxiv.org/html/2604.05755).
- **Overthinking.** DeepSeek-R1-32B on GPQA Diamond peaked at 55.6% with a 10,000-token budget, then fell to 53.1% at 16,000 — [Zhou et al.](https://arxiv.org/html/2604.10739v1).

### Inferences
- Well supported, across exact models and older ones: running with reasoning off is the weakest setting for this kind of question. Non-reasoning modes on `qwen/qwen3.8-27b` and `deepseek-flash` should not be read as representing those models' scores.
- Moderately supported: there is a useful middle. On AA and ARC data for Grok 4.7 and Gemini 3.8 Flash, most gain arrives by high or medium, and the top step adds cost with gains inside the interval. ReasonLab shows the same on MCQs for older models.
- Weakly supported: effort helps more for decision-type questions than recall (QuArch), which suggests scenario MCQs may gain more than general MCQ benchmarks do. No cloud data tests this.
- Possible Groq-specific limit: Groq caps output at 16,384 tokens, while Qwen3.8 27B averaged 24,786 output tokens on LiveBench's short questions at top effort and 16.51k tokens on Vals' GPQA. Quesma's best GPQA result needed about 8k reasoning tokens, so not every question would reach the cap. Empty or cut-off answers are a plausible risk at Groq's highest settings. This is my inference; I found no test, and Groq's page does not say whether reasoning tokens count toward the cap.
- More tokens did not buy higher reasoning scores across models. Grok 4.7 used about eight times Argon's tokens and scored lower. Token use is therefore a cost measure, not a quality measure.
- Costs on LiveBench's questions should not be read as cost for a cloud MCQ. The questions differ, and these were top-effort runs.

### Gaps
- No target model except Qwen3.8 27B has MCQ accuracy by effort level.
- No effort data for any target model on architecture or cloud questions.
- Gemini 4 Argon has AA results at High only, so Index effects by effort are unknown.
- Gemini 3.5 Flash-Lite effort variants exist on ARC only.
- DeepSeek 1017 at `high` (the API default) and `low` have no AA Briefcase or GDPval-AA results that I could see, though ARC has them.
- Groq-hosted Qwen3.8-27B has no measured accuracy at any effort.
- Grok 4.7 Medium has no AA row in the fetched data.

---

## Which scores are independent and which are vendor-reported?

### Takeaway
Artificial Analysis, Arena, LiveBench, Vals and ARC Prize results are independent of the model makers, as are the academic papers and Quesma's replication. Launch tables from xAI, Google, DeepSeek and Alibaba are vendor-reported, and Groq's page repeats vendor numbers; where vendor and independent figures can be matched, some agree and some differ by a lot.

### Cited Findings

#### Independent sources

| Source | What it provides | Caveats |
|---|---|---|
| [Artificial Analysis](https://artificialanalysis.ai/methodology/intelligence-benchmarking) | Index v5.0, AA-Briefcase, GDPval-AA | Commercial firm. Some evaluations are AA runs of third-party benchmarks: GDP.pdf from Surge AI, FrontierCode from Cognition, AutomationBench from Zapier — [AA announcement](https://artificialanalysis.ai/articles/artificial-analysis-intelligence-index-v5) |
| [Arena](https://arena.ai/leaderboard/text) | Human preference votes | Measures preference, not correctness |
| [LiveBench 2.0](https://livebench.ai/) | Reasoning and other suites | Sponsored by Abacus.AI, per the [site bundle](https://livebench.ai/). Single run per model |
| [Vals AI](https://www.vals.ai/benchmarks) | Index v2.2 and subject benchmarks | Finance-heavy index. Pages show some internal mismatches, for example Grok 4.7 and Argon update text vs current table — [Vals Grok 4.7](https://www.vals.ai/models/grok_grok-4.7) |
| [ARC Prize](https://arcprize.org/leaderboard) | ARC-AGI by effort | Puzzles, not domain knowledge |
| [Quesma](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) | Qwen3.8 27B replication | Company blog, not peer reviewed; self-hosted, not Groq |

#### Vendor-reported sources

- **xAI launch post** (21 Sep 2026): Grok 4.7 xHigh table, "checks its own work more carefully", no test results for that claim, and no explanation of what effort levels mean — [xAI](https://x.ai/news/grok-4-7).
- **Google Gemini 3.8 Flash model card** ("as of September, 2026"): effort level not stated, and who ran the evaluations not stated — [Google model card](https://deepmind.google/models/model-cards/gemini-3-8-flash/).
- **Google Gemini 4 Argon post** (30 Sep 2026): thinking level not stated. Benchmarks carry third-party names, but who ran them is not said — [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/). A secondary source says Google used the highest thinking setting while the API defaults to medium — [Oasis](https://joinoasis.com/blog/gemini-4-argon-review).
- **DeepSeek**: GPQA Diamond 90.9% comes from its paper; other values on its table were seen only in secondary summaries — [arXiv 2609.19969](https://arxiv.org/pdf/2609.19969); [Regolo](https://regolo.ai/deepseek-v4-1-flash-vs-v4-flash-which-open-weight-model-should-your-company-run/). The paper says evaluations ran "in our internal framework", per a search summary.
- **Alibaba Qwen3.8-27B card**: table compares with Opus 4.6 Max, and most rows have no stated runner. QwenSWEBench and CoWorkBench are in-house — [Hugging Face](https://huggingface.co/Qwen/Qwen3.8-27B).
- **Groq docs** repeat the same Qwen numbers (GPQA 89.2%, IFBench 79.5%) with no per-benchmark source. These are not Groq-hosted measurements as far as the page shows — [Groq docs](https://console.groq.com/docs/model/qwen/qwen3.8-27b).
- Review sites that rework vendor tables should be treated as vendor-reported: [eesel Grok 4.7](https://www.eesel.ai/blog/grok-4-7-review).

#### Vendor vs independent, same model and same named benchmark

| Model | Benchmark | Vendor | Independent | Reading |
|---|---|---|---|---|
| Grok 4.7 xHigh | AA Briefcase v1.1 | [1,657](https://x.ai/news/grok-4-7) | [1638](https://artificialanalysis.ai/evaluations/aa-briefcase) | Close; 19 Elo apart, outside the ±10 interval. May predate a later fit |
| Grok 4.7 | Terminal-Bench 4.0 | [37.6%](https://x.ai/news/grok-4-7) (xHigh) | [28.79% ±2.31](https://www.vals.ai/models/grok_grok-4.7) (xhigh); [25%](https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-gemini-3-8-flash) (High) | Vendor clearly higher |
| Gemini 3.8 Flash | Terminal-Bench 4.0 | [19.1%](https://deepmind.google/models/model-cards/gemini-3-8-flash/) | [19.70% ±2.31](https://www.vals.ai/models/google_gemini-3.8-flash); [20%](https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-gemini-3-8-flash) | Agree |
| Gemini 3.8 Flash | GDP.pdf all-pass | [35.0%](https://deepmind.google/models/model-cards/gemini-3-8-flash/) | [21%](https://artificialanalysis.ai/models/comparisons/grok-4-7-high-vs-gemini-3-8-flash) | Vendor clearly higher. AA warns its scores are not directly comparable with Surge AI's own numbers, so this gap may be partly method — [AA methodology, via search summary](https://artificialanalysis.ai/methodology/intelligence-benchmarking) |
| Qwen3.8 27B | GPQA Diamond | [89.2%](https://huggingface.co/Qwen/Qwen3.8-27B) | [88.89% ±1.58](https://www.vals.ai/benchmarks/gpqa); [89.9%](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/) | Agree |
| Qwen3.8 27B | Terminal-Bench 2.1 | [73.0](https://huggingface.co/Qwen/Qwen3.8-27B) | [58.43% ±5.25](https://www.vals.ai/models/alibaba_qwen3.8-27b) | Vendor clearly higher; harnesses may differ |
| DeepSeek V4.1 Flash | Terminal-Bench 2.1 | [90.6](https://blog.buildfastwithai.com/deepseek-v4-1-flash-review) (from a search summary of secondary reviews; page not opened) | [74.53%](https://www.vals.ai/models/deepseek_deepseek-v4.1-flash) | Vendor appears clearly higher; harnesses may differ; vendor figure unconfirmed |
| Gemini 4 Argon | AutomationBench | [51.3%](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) | [77.5%](https://artificialanalysis.ai/evaluations/automationbench-aa) | Not the same scoring or implementation; do not compare |

### Inferences
- Vendor numbers are most reliable when the task is well-defined and repeatable (GPQA Diamond) and diverge most on agentic benchmarks, where harness choice matters. This fits the table but rests on few rows.
- Vendor reports usually leave out effort level. Any vendor score with no effort label should be treated as a best case until shown otherwise; Google's Argon setup is one reported example.
- None of the vendors claims a solution architect or cloud certification result in the sources I read, so vendor marketing does not fill this gap.

### Gaps
- Who ran Google's third-party-named benchmarks, and at what effort, is not on the pages I read. The methodology page linked from the model card was not fetched.
- The primary DeepSeek benchmark table was not read directly; those values come from secondary reports and a search summary.
- xAI's GDPval chart values could not be read from the page text.

---

## What evidence is missing?

### Takeaway
No benchmark tests solution architect MCQs on these exact models. Every conclusion about them for this use is an indirect estimate from reasoning, knowledge-work, recall and preference benchmarks, or from older model versions.

### Cited Findings

- SAKE and CAKE are the closest benchmarks, and neither tests a target model. SAKE's newest related models are Grok 4.2, DeepSeek v3.2, Gemini 3.1 Flash Lite and Qwen3 235B — [SAKE](https://arxiv.org/pdf/2606.29520). CAKE tested Qwen 2.5, Qwen3-Coder, Llama, Mistral and GPT mini models — [CAKE](https://arxiv.org/html/2604.05755).
- SAKE says it releases questions, scripts and results as open source so evaluations can be re-run as new models appear — [SAKE](https://arxiv.org/pdf/2606.29520). The repository link in the paper is an anonymised review URL — [SAKE repository link](https://anonymous.4open.science/r/SAKE-1DD7/README.md); I did not open it.
- A September 2026 perspective paper argues general rankings are a starting point and not a substitute for representative testing, and that reports should disclose configuration and budget. It runs no evaluations of its own — [Amin](https://arxiv.org/html/2609.23201v1).
- Vals' MMLU Pro and GPQA stopped before Grok 4.7, V4.1 Flash and Argon, so the main public MCQ benchmarks cannot compare those three with the rest — [MMLU Pro](https://www.vals.ai/benchmarks/mmlu_pro); [GPQA](https://www.vals.ai/benchmarks/gpqa).

### Inferences
- The biggest single missing item is a controlled run of exam-style cloud scenario MCQs across these exact API IDs, at named effort settings, with separate results for single-answer and multiple-response items and for AWS, Azure and GCP. SAKE shows a public four-option architecture set could serve as a first step. It would still not cover named cloud services or trade-offs under constraints.
- Practice-exam banks carry their own risk as test data: answer keys are often community-sourced, and one app listing warns of outdated or wrong answers — [GCP-PCA app listing](https://apps.apple.com/us/app/id1624259317). Any test built on them needs checked keys. This is especially true because the Noever and CyberCertBench studies both drew on such banks.
- Given this gap, the evidence supports statements about general reasoning, recall and knowledge-work strength, not statements such as "model X will pass SAA-C03". The notes above make no winner claim.

### Gaps

**Missing evidence**
- Solution architect MCQs on any target model: none found.
- AWS SAA, AWS SAP, AZ-305 or Google PCA results on any model newer than GPT-4: none found.
- Independent system design head-to-head on these exact models: none found.
- Constraint-ignoring or popular-answer tests on these exact models in architecture scenarios: none found.
- Effect of reasoning effort on architecture MCQs: none found for any target model.
- Multiple-response (select two or three) cloud questions on any target model: none found.
- Any accuracy measured on the Groq-hosted endpoint: none found. All Qwen3.8 27B numbers are from other hosts or self-hosting.
- Image-based architecture questions, such as a scenario presented as a screenshot or diagram: none found. Vals MMMU Pro is the nearest image MCQ proxy, and it has no Grok 4.7, DeepSeek V4.1 Flash or Argon results.
- Any Flash-Lite result on LiveBench 2.0 or Vals Index v2.2: not present.
- Any model called Gemini 3.8 Flash-Lite: not on Google's pricing page.

**Pages that could not be reached or read**
- [MDPI paper on architectural patterns](https://www.mdpi.com/2673-2688/7/6/195): 403.
- [Medium GPT-4 AWS update](https://medium.com/@miguelsalva/chatgpt-goes-certified-aws-gpt-4-updated-5c41ade4795b): 403.
- [Arena "occupational" URL](https://arena.ai/leaderboard/text/occupational): 404. Individual category URLs worked. I checked Software & IT and Business only, of the 29 categories Arena lists.
- [Vals Index with a hyphen](https://www.vals.ai/benchmarks/vals-index): 404; the underscore URL worked.
- [ARC leaderboard HTML](https://arcprize.org/leaderboard) and [LiveBench HTML](https://livebench.ai/) render through scripts, so I used their published data files instead.
- Sections of AA pages rendered only partly through my fetch tool. Where a value is marked "not shown", it was not visible to me, which does not prove AA has no value.
