# Pricing, image input and practical API limits for xAI Grok, Groq, DeepSeek and Gemini (state as of 2026-11-01)

Figures below were read from the raw text of each page on 2026-11-01, not from summaries. Artificial Analysis (AA) figures come from the data embedded in AA's pages. This note compares facts only and picks no winner.

## 1. What are the exact input, cached-input and output prices per 1M tokens today, including scheduled changes, off-peak discounts and long-prompt tiers?

### Takeaway
Four price mechanics change the bill. DeepSeek halves its prices off-peak. Gemini 3.8 Flash, 3.6 Flash and 4 Argon are on introductory prices that double on fixed dates (1 Jan 2027 and 1 Dec 2026). xAI doubles all rates once a prompt reaches 200k tokens, which a single screenshot call will not reach. Groq lists no cached price for Qwen because prompt caching does not cover that model, and groq.com/pricing no longer shows prices.

### Cited Findings

#### xAI (the docs now use the brand "SpaceXSI"; the legal entity is SpaceX Super Intelligence LLC)
Pricing page date: "Last updated: October 10, 2026" — [xAI Pricing](https://docs.x.ai/developers/pricing). All rows below are from the [Pricing page Markdown](https://docs.x.ai/developers/pricing.md), per 1M tokens, for prompts under 200k tokens.

| Model | Input | Cached input | Output | At or above 200k prompt tokens | Accepts images |
|---|---|---|---|---|---|
| `grok-4.7` | $2.00 | $0.50 | $6.00 | $4.00 / $1.00 / $12.00 | [Yes](https://docs.x.ai/developers/models/grok-4.7.md) |
| `grok-4.6` | $2.00 | $0.50 | $6.00 | $4.00 / $1.00 / $12.00 | [Yes](https://docs.x.ai/developers/models/grok-4.6.md) |
| `grok-4.5` | $2.00 | $0.30 | $6.00 | $4.00 / $0.60 / $12.00 | [Yes](https://docs.x.ai/developers/models/grok-4.5.md) |
| `grok-4.3` | $1.25 | $0.20 | $2.50 | $2.50 / $0.40 / $5.00 | [Yes](https://docs.x.ai/developers/models/grok-4.3.md) |
| `grok-4.20-0309-reasoning` | $1.25 | $0.20 | $2.50 | $2.50 / $0.40 / $5.00 | [Yes](https://docs.x.ai/developers/models/grok-4.20-0309-reasoning.md) |
| `grok-4.20-0309-non-reasoning` | $1.25 | $0.20 | $2.50 | $2.50 / $0.40 / $5.00 | [Yes](https://docs.x.ai/developers/models/grok-4.20-0309-non-reasoning.md) |
| `grok-4.20-multi-agent-0309` | $1.25 | $0.20 | $2.50 | $2.50 / $0.40 / $5.00 | [Yes](https://docs.x.ai/developers/models/grok-4.20-multi-agent-0309.md) |
| `grok-build-0.1` | $1.00 | $0.20 | $2.00 | $2.00 / $0.40 / $4.00 | [Yes](https://docs.x.ai/developers/models/grok-build-0.1.md) |

- Long-prompt rule: "requests whose prompt reaches the listed token threshold are billed at the higher rate for all tokens in the request" — [xAI Pricing](https://docs.x.ai/developers/pricing.md).
- Batch API is 20% off for every model above except `grok-build-0.1`, whose model page says Batch is not supported — [xAI Pricing](https://docs.x.ai/developers/pricing.md); [grok-build-0.1](https://docs.x.ai/developers/models/grok-build-0.1.md).
- Priority processing costs 2x standard rates. The US regional endpoint costs 1.1x and serves only `grok-4.7` and `grok-4.6` — [xAI Pricing](https://docs.x.ai/developers/pricing.md).
- No scheduled token price change is listed on the page — [xAI Pricing](https://docs.x.ai/developers/pricing.md).
- Page conflict: the marketing page says "Usage-based pricing from $2/M tokens" and names only `grok-4.7` on its price table — [x.ai/api](https://x.ai/api). The docs list `grok-build-0.1` at $1.00 and several models at $1.25 — [xAI Pricing](https://docs.x.ai/developers/pricing.md).

#### Groq (the inference company)
- `qwen/qwen3.8-27b`: input $0.80, output $4.00 per 1M tokens; no cached price shown — [Qwen model page](https://console.groq.com/docs/model/qwen/qwen3.8-27b); [Groq Models](https://console.groq.com/docs/models).
- "Prompt caching is currently only supported for the following models": `openai/gpt-oss-20b`, `openai/gpt-oss-120b`, `openai/gpt-oss-safeguard-20b`. Qwen is not on that list — [Groq Prompt Caching](https://console.groq.com/docs/prompt-caching).
- The only other Groq-hosted model documented for images is `meta-models/muse-spark-open`, described as "Available in limited preview; contact us to discuss access" — [Groq Vision](https://console.groq.com/docs/vision). Its price is shown as Contact Sales — [Groq Models](https://console.groq.com/docs/models).
- No date appears on the Models page — [Groq Models](https://console.groq.com/docs/models). Groq's policies page says "last modified June 22, 2026" — [Groq Policies](https://console.groq.com/docs/legal).
- Page conflict: the Services Agreement says prices "are as published at https://groq.com/pricing/" — [Groq Services Agreement](https://console.groq.com/docs/legal/services-agreement). That URL returned the marketing home page with no model prices on 2026-11-01 — [groq.com/pricing](https://groq.com/pricing). Prices now live on the docs pages above.

#### DeepSeek
All rows are from the [DeepSeek pricing page](https://api-docs.deepseek.com/quick_start/pricing), per 1M tokens. The page shows no date; only "Copyright © 2026".

| Model (version) | Cache hit, off-peak / peak | Cache miss, off-peak / peak | Output, off-peak / peak | Vision |
|---|---|---|---|---|
| `deepseek-flash` (DeepSeek-V4.1-Flash-1017) | $0.003 / $0.006 | $0.15 / $0.30 | $0.60 / $1.20 | ✓ |
| `deepseek-v4-pro` (DeepSeek-V4-Pro-0813) | $0.022 / $0.044 | $0.66 / $1.32 | $1.98 / $3.96 | "Not supported" |

- "Off-peak rates are half of the peak rates. Peak hours are 01:00 - 04:00 and 06:00 - 10:00 UTC, Monday through Friday, excluding Chinese public holidays. All other hours are off-peak, including weekends and Chinese public holidays in full." — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing).
- These prices took effect at 04:00 UTC on 10 Sept 2026 — [DeepSeek V4.1 Flash release note](https://api-docs.deepseek.com/news/news260910.md).
- The only dated change on the pricing page is per-request Search and Fetch billing, starting at 00:00 Beijing time on 1 Nov 2026. It covers server-side tool calls and does not change token prices — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing).
- "Product prices may vary and DeepSeek reserves the right to adjust them." — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing).

#### Google Gemini API
Page date: "Last updated 2026-10-30 UTC" — [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing). All rows below are the Standard paid tier from that page, per 1M tokens, for text, image and video input. No model below has a long-prompt tier on this page.

| Model | Input | Cached input | Cache storage (per 1M tokens per hour) | Output (including thinking) | Scheduled change |
|---|---|---|---|---|---|
| `gemini-3.8-flash` | $0.75 | $0.075 | $0.50 | $3.75 | From 1 Jan 2027: $1.50 / $0.15 / $1.00 / $7.50 |
| `gemini-3.6-flash` | $0.75 | $0.075 | $0.50 | $3.75 | From 1 Jan 2027: $1.50 / $0.15 / $1.00 / $7.50 |
| `gemini-3.5-flash-lite` | $0.30 | $0.03 | $1.00 | $2.50 | None listed |
| `gemini-3.1-flash-lite` | $0.25 | $0.025 | $1.00 | $1.50 | None listed |
| `gemini-3-flash-preview` | $0.50 | $0.05 | $1.00 | $3.00 | None listed |
| `gemini-2.5-flash` | $0.30 | $0.03 | $1.00 | $2.50 | None listed |
| `gemini-2.5-flash-lite` | $0.10 | $0.01 | $1.00 | $0.40 | None listed |
| `gemini-4-argon` | $2.00 | $0.10 (implicit caching only) | Not listed | $10.00 | From 1 Dec 2026: $4.00 / $0.20 / $20.00 |

- Batch and Flex are half the standard input and output prices on all eight models. Priority is 1.8x (for example $1.35 and $6.75 on 3.8 Flash) — [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing).
- Gemini 4 Carbon is not on the pricing page — [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing). Google's blog gives an introductory $2 input and $10 output, cached input at 95% off, then $4 and $20 — [Google blog, Gemini 4 Carbon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/).

### Inferences
- A single screenshot call stays far below xAI's 200k prompt threshold, so only the lower row applies.
- Each screenshot is different, so cached rates would apply at most to a repeated text prefix such as a system prompt, not to the image.
- Gemini 3.5 Flash-Lite is newer than 3.1 Flash-Lite but costs more on both input and output ($0.30 / $2.50 against $0.25 / $1.50).

### Gaps
- Pages that could not be used: `aistudio.google.com/rate-limit` redirects to sign-in; `platform.deepseek.com` returned HTTP 202 with an empty body; the DeepSeek FAQ redirects to a JavaScript shell at `static.deepseek.com` with no readable text.
- `x.ai/api` returned 403 to one fetch tool but 200 to a direct request, and the direct copy was used.
- I did not confirm whether Qwen is eligible for Groq's Batch API. The 50% batch discount is stated only in general terms on the [Groq Prompt Caching page](https://console.groq.com/docs/prompt-caching).

## 2. How many tokens does one 1920x1080 screenshot cost on each provider, according to that provider's own formula or limit?

### Takeaway
Groq (2,048) and DeepSeek (1,024) publish clear numbers. Gemini publishes two rules that disagree for Gemini 3 and 4: 1,120 tokens by default under the media resolution table, or 1,548 under the older tile formula. xAI publishes no formula at all in its current docs, so the image cost of every Grok model is unknown until a test call is made.

### Cited Findings
- **xAI:** the Image Understanding page lists only size, count and format limits, with no token figure — [xAI Image Understanding](https://docs.x.ai/developers/model-capabilities/images/understanding). The legacy page says `low` "consumes fewer tokens" and `high` is "more expensive in terms of token usage", with no numbers — [xAI Chat Completions (Legacy)](https://docs.x.ai/developers/model-capabilities/legacy/chat-completions.md).
- **xAI actual counts are returned per call:** `prompt_tokens_details` includes `image_tokens` — [xAI Chat Completions reference](https://docs.x.ai/developers/rest-api-reference/inference/chat-completions.md). Every response also includes `cost_in_usd_ticks`, where 1 USD = 10,000,000,000 ticks — [xAI Cost Tracking](https://docs.x.ai/developers/cost-tracking.md).
- **xAI image limits:** "Maximum image size: 20MiB", "Maximum number of images: No limit", jpg/jpeg or png — [xAI Image Understanding](https://docs.x.ai/developers/model-capabilities/images/understanding).
- **Groq Qwen:** "Each image counts as 2048 input tokens." Maximum 3 images per request; a request containing an image URL is limited to 20MB — [Groq Vision](https://console.groq.com/docs/vision). The Qwen model page repeats the 2048 figure — [Qwen model page](https://console.groq.com/docs/model/qwen/qwen3.8-27b).
- **Groq Muse Spark Open:** "Each image counts as up to 1,026 input tokens, depending on its size." Maximum 5 images — [Groq Vision](https://console.groq.com/docs/vision).
- **DeepSeek:** larger images are scaled down "so that the total pixel count after resizing is roughly that of a 1300×1300 image", and "there is an upper bound of 1024 tokens per image" — [DeepSeek Vision](https://api-docs.deepseek.com/guides/vision.md).
- **DeepSeek detail levels:** `low` downscales to 512×512; `high`, `original` and `auto` keep the original image — [DeepSeek Vision](https://api-docs.deepseek.com/guides/vision.md). Estimates "may vary slightly", and the API `usage` is the source of truth — [DeepSeek Token Usage](https://api-docs.deepseek.com/quick_start/token_usage.md).
- **Gemini 3 and 4 (media resolution table):** unspecified (default) 1,120; `low` 280; `medium` 560; `high` 1,120; `ultra_high` 2,240 tokens per image — [Gemini Media Resolution](https://ai.google.dev/gemini-api/docs/media-resolution).
- **Gemini tile rule:** "258 tokens if both dimensions <= 384 pixels. Larger images are tiled into 768x768 pixel tiles, each costing 258 tokens." The rough formula is crop unit = floor(min(width, height) / 1.5), then divide each dimension by the crop unit and multiply. Google's worked example is 960x540, crop unit 360, 3 * 2 = 6 tiles — [Gemini Image Understanding](https://ai.google.dev/gemini-api/docs/image-understanding).
- **Page conflict on Gemini:** the token-counting page states the same 258-per-tile rule without limiting it to older models, right beside a `gemini-3.8-flash` code sample — [Gemini Tokens](https://ai.google.dev/gemini-api/docs/tokens). That disagrees with the 1,120 default for Gemini 3 and 4 — [Gemini Media Resolution](https://ai.google.dev/gemini-api/docs/media-resolution).
- **Gemini limits:** inline data limits the total request to 20MB; up to 3,600 image files per request; supported formats include JPEG and PNG — [Gemini Image Understanding](https://ai.google.dev/gemini-api/docs/image-understanding).

### Inferences
The calculations below apply each provider's rule to 1920x1080 (2,073,600 pixels). Prices are the standard rates from section 1.

| Model | Calculation | Image tokens | Image cost per call |
|---|---|---|---|
| `grok-4.7` | No formula published | Unknown | $0.002 per 1,000 image tokens |
| `grok-4.3`, `grok-4.20-*` | No formula published | Unknown | $0.00125 per 1,000 image tokens |
| `grok-build-0.1` | No formula published | Unknown | $0.001 per 1,000 image tokens |
| `qwen/qwen3.8-27b` | Fixed per image | 2,048 | $0.0016384 |
| `deepseek-flash`, peak | 2,073,600 > 1,690,000 (1300²), so scaled to about 1733×975 and capped | 1,024 | $0.0003072 |
| `deepseek-flash`, off-peak | Same | 1,024 | $0.0001536 |
| `gemini-3.8-flash`, `gemini-3.6-flash` | Default media resolution | 1,120 | $0.00084 now; $0.00168 from 1 Jan 2027 |
| `gemini-3.5-flash-lite` | Default media resolution | 1,120 | $0.000336 |
| `gemini-3.1-flash-lite` | Default media resolution | 1,120 | $0.00028 |
| `gemini-3-flash-preview` | Default media resolution | 1,120 | $0.00056 |
| `gemini-4-argon` | Default media resolution | 1,120 | $0.00224 now; $0.00448 from 1 Dec 2026 |
| `gemini-2.5-flash` | Crop unit floor(1080/1.5) = 720; 1920/720 = 2.67 → 3; 1080/720 = 1.5 → 2; 3 × 2 = 6 tiles × 258 | 1,548 | $0.0004644 |
| `gemini-2.5-flash-lite` | Same | 1,548 | $0.0001548 |

- If the tile rule applied to Gemini 3 models instead, the image would be 1,548 tokens: $0.00116 on 3.8 Flash, $0.00046 on 3.5 Flash-Lite and $0.00039 on 3.1 Flash-Lite.
- 1920x1080 has the same shape as Google's 960x540 example, so the rounding to 6 tiles follows that example exactly.
- At today's prices, Qwen's fixed 2,048 gives Groq the highest image cost of the models with a published count, apart from Gemini 4 Argon. Gemini 3.8 and 3.6 Flash pass it from 1 Jan 2027.

### Gaps
- No xAI image token figure exists in the current docs. The only figure found was a third-party "~2,000 tokens" claim for Grok 2 with no xAI source, so it should not be used — [LiveChatAI calculator](https://livechatai.com/grok-2-pricing-calculator).
- DeepSeek's page has an interactive calculator, but I could not read its logic, so the token count for `detail: low` is unknown — [DeepSeek Token Usage](https://api-docs.deepseek.com/quick_start/token_usage.md).
- It is not documented which Gemini rule applies to Gemini 3 and 4 when the two pages disagree. Google's `countTokens` or the `usage` field on a real call would settle it.

## 3. Do thinking or reasoning tokens count as billed output, and how many output tokens do these models typically use per answer?

### Takeaway
Yes on all four, though only xAI and Google say so outright. Reasoning is the larger cost driver for most options because it is priced at the output rate, and on Grok 4.7 and on Gemini 3 and 4 models it cannot be switched off. AA's verbosity data shows reasoning as roughly 67% to 82% of output tokens, but those are long agentic tasks. I found no measured token count for a one-question screenshot call.

### Cited Findings

#### Billing
- **xAI:** "Reasoning tokens | Full completion token price" — [xAI Prompt Caching pricing](https://docs.x.ai/developers/advanced-api-usage/prompt-caching/usage-and-pricing.md). "When you use a reasoning model, the reasoning tokens are billed as part of your total consumption." — [xAI Reasoning](https://docs.x.ai/developers/model-capabilities/text/reasoning.md).
- **xAI cap:** `max_completion_tokens` "only applies to visible output tokens (i.e. does not apply to tokens used for reasoning or function calls)" and defaults to 128,000 — [xAI Chat Completions reference](https://docs.x.ai/developers/rest-api-reference/inference/chat-completions.md).
- **Google:** the price row is "Output price (including thinking tokens)" — [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing). "When thinking is turned on, response pricing is the sum of output tokens and thinking tokens." — [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking). "Pricing is based on the full thought tokens the model needs to generate, despite only the summary being output from the API." — [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking).
- **Groq:** reasoning chains "are part of the token output" — [Groq Reasoning](https://console.groq.com/docs/reasoning). `completion_tokens_details.reasoning_tokens` is the "Number of tokens used for reasoning (for reasoning models)" — [Groq API reference](https://console.groq.com/docs/api-reference).
- **DeepSeek:** "We bill model usage based on the total number of input and output tokens by the model." — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing). `completion_tokens_details.reasoning_tokens` is "Tokens generated by the model for reasoning." — [DeepSeek Chat Completions](https://api-docs.deepseek.com/api/create-chat-completion.md).

#### Can reasoning be reduced or disabled?
| Model | Default | Can it be off? | Source |
|---|---|---|---|
| `grok-4.7`, `grok-4.6`, `grok-4.5` | `high` | No: "Reasoning cannot be disabled." Lowest is `low` | [xAI Reasoning](https://docs.x.ai/developers/model-capabilities/text/reasoning.md) |
| `grok-4.3` | `low` | Yes: `none` is supported | [grok-4.3](https://docs.x.ai/developers/models/grok-4.3.md) |
| `grok-4.20-0309-non-reasoning` | n/a | Reasoning: No | [grok-4.20 non-reasoning](https://docs.x.ai/developers/models/grok-4.20-0309-non-reasoning.md) |
| `grok-build-0.1` | Not stated | No off setting listed; Reasoning: Yes | [grok-build-0.1](https://docs.x.ai/developers/models/grok-build-0.1.md) |
| `qwen/qwen3.8-27b` | Conflict, see below | Yes: `none`, "The model will not use any reasoning tokens." | [Groq Reasoning](https://console.groq.com/docs/reasoning) |
| `deepseek-flash` | Thinking on, effort `high` | Yes: `{"thinking": {"type": "disabled"}}` | [DeepSeek Thinking](https://api-docs.deepseek.com/guides/thinking_mode.md) |
| `gemini-3.8-flash` | Medium | No; `minimal` "is not supported and returns an error" | [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking); [3.8 Flash page](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash) |
| `gemini-3.6-flash` | Medium | No; `minimal` available | [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking) |
| `gemini-3.5-flash-lite` | Minimal | No; `minimal` is the default | [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking) |
| `gemini-3-flash-preview` | High | No; `minimal` available | [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking) |
| `gemini-2.5-flash` | On | Yes: `reasoning_effort` "none" | [Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai) |
| `gemini-2.5-flash-lite` | Off | Yes | [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking) |
| `gemini-4-argon` | Medium | No; levels are low, medium, high | [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking) |

- "Reasoning cannot be turned off for Gemini 2.5 Pro or 3 models." — [Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai). Google also warns that `minimal` "does not guarantee that thinking is off" — [Gemini 3 guide](https://ai.google.dev/gemini-api/docs/gemini-3).
- `gemini-3.1-flash-lite` is not in the thinking table, though the OpenAI mapping table does list it — [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking); [Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai).

#### Conflicts between pages
- **Groq Qwen default:** the API reference says "Its default is `none`; `high` selects the model's native `xhigh` mode." — [Groq API reference](https://console.groq.com/docs/api-reference). The model page calls `reasoning_effort="default"` thinking mode — [Qwen model page](https://console.groq.com/docs/model/qwen/qwen3.8-27b). The reasoning page says that at `default`, Qwen "does not return reasoning tokens" — [Groq Reasoning](https://console.groq.com/docs/reasoning).
- **xAI `xhigh` on Grok 4.5:** the reasoning page says `xhigh` is not supported on `grok-4.5` and is treated as `high` — [xAI Reasoning](https://docs.x.ai/developers/model-capabilities/text/reasoning.md). The model page lists it as supported — [grok-4.5](https://docs.x.ai/developers/models/grok-4.5.md).
- **xAI levels on Grok 4.3:** the retirement guide lists 4 levels (none, low, medium, high) — [xAI May 15 retirement](https://docs.x.ai/developers/migration/may-15-retirement.md). The model page lists 5, adding `xhigh` — [grok-4.3](https://docs.x.ai/developers/models/grok-4.3.md).

#### Verbosity from Artificial Analysis
AA totals are output tokens used across its full Intelligence Index run, which is made of long, multi-step tasks. AA's comparison median is 70M — [AA Gemini 3.8 Flash](https://artificialanalysis.ai/models/gemini-3-8-flash).

| Model and variant | Output total | Reasoning | Answer | Output per task (AA) | Source |
|---|---|---|---|---|---|
| Grok 4.7 xhigh | 142.6M | 114.0M | 28.6M | 92,970 | [AA](https://artificialanalysis.ai/models/grok-4-7) |
| Grok 4.7 high | 123.2M | 99.4M | 23.8M | 89,127 | [AA](https://artificialanalysis.ai/models/grok-4-7-high) |
| Grok 4.7 low | 51.3M | 34.2M | 17.0M | 42,670 | [AA](https://artificialanalysis.ai/models/grok-4-7-low) |
| DeepSeek V4.1 Flash 1017 max | 174.4M | 134.5M | 39.9M | 138,962 | [AA](https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017) |
| DeepSeek V4.1 Flash 1017 non-reasoning | 51.2M | 0 | 51.2M | 65,358 | [AA](https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017-non-reasoning) |
| Qwen3.8 27B xhigh | 127.7M | 96.7M | 31.0M | 109,802 | [AA](https://artificialanalysis.ai/models/qwen3-8-27b) |
| Qwen3.8 27B non-reasoning | 37.5M | 0 | 37.5M | 44,867 | [AA](https://artificialanalysis.ai/models/qwen3-8-27b-non-reasoning) |
| Gemini 3.8 Flash high | 125.7M | 97.8M | 27.8M | 98,940 | [AA](https://artificialanalysis.ai/models/gemini-3-8-flash) |
| Gemini 3.8 Flash medium | 83.9M | 58.7M | 25.2M | 82,068 | [AA](https://artificialanalysis.ai/models/gemini-3-8-flash-medium) |
| Gemini 3.5 Flash-Lite | 43.8M | 32.4M | 11.4M | 30,301 | [AA](https://artificialanalysis.ai/models/gemini-3-5-flash-lite) |
| Gemini 4 Argon high | 113.3M | 79.6M | 33.7M | 116,368 | [AA](https://artificialanalysis.ai/models/gemini-4-argon) |
| Gemini 4 Carbon high | 204.8M | 167.9M | 36.9M | 122,768 | [AA](https://artificialanalysis.ai/models/gemini-4-carbon) |

#### Small documented examples
- xAI's sample Vercel AI SDK response for a two-sentence answer shows `outputTokens: 126` and `reasoningTokens: 167` — [xAI Chat Completions (Legacy)](https://docs.x.ai/developers/model-capabilities/legacy/chat-completions.md).
- Google's thinking example shows `total_output_tokens: 171` and `total_thought_tokens: 297` — [Gemini Thinking](https://ai.google.dev/gemini-api/docs/thinking).

### Inferences
- Reasoning share of output in AA's totals: Grok 4.7 low 67%, high 81%, xhigh 80%; DeepSeek max 77%; Qwen xhigh 76%; Gemini 3.8 high 78%, medium 70%; 3.5 Flash-Lite 74%; Argon 70%; Carbon 82%.
- AA's per-task numbers are tens of thousands of tokens because the tasks are agentic. They rank verbosity but must not be read as tokens per multiple-choice answer.
- The two documented samples above show reasoning of about 1.3 to 1.7 times the visible answer on very short prompts. They are single examples, not measurements.

**Illustrative cost per call.** The assumptions are mine: 300 text prompt tokens, a 150-token JSON answer, and three reasoning levels (R). Formula: ((image tokens + 300) × input price + (150 + R) × output price) / 1,000,000. Multiply by 1,000 for cost per 1,000 calls. One call every 10 seconds is 360 calls per hour.

| Model | R = 0 | R = 500 | R = 2,000 |
|---|---|---|---|
| `grok-4.7` (image tokens excluded) | Not available | $0.00450 | $0.01350 |
| `grok-4.3` (image tokens excluded) | $0.00075 with `none` | $0.00200 | $0.00575 |
| `grok-4.20-0309-non-reasoning` (image tokens excluded) | $0.00075 | n/a | n/a |
| `grok-build-0.1` (image tokens excluded) | Not available | $0.00160 | $0.00460 |
| `qwen/qwen3.8-27b` | $0.00248 | $0.00448 | $0.01048 |
| `deepseek-flash`, peak | $0.00058 | $0.00118 | $0.00298 |
| `deepseek-flash`, off-peak | $0.00029 | $0.00059 | $0.00149 |
| `gemini-3.8-flash` or `3.6-flash`, now | Not available | $0.00350 | $0.00913 |
| `gemini-3.8-flash` or `3.6-flash`, from 1 Jan 2027 | Not available | $0.00701 | $0.01826 |
| `gemini-3.5-flash-lite` | $0.00080 (minimal may still think) | $0.00205 | $0.00580 |
| `gemini-3.1-flash-lite` | $0.00058 (minimal may still think) | $0.00133 | $0.00358 |
| `gemini-3-flash-preview` | $0.00116 (minimal may still think) | $0.00266 | $0.00716 |
| `gemini-2.5-flash` | $0.00093 | $0.00218 | $0.00593 |
| `gemini-2.5-flash-lite` | $0.00024 | $0.00044 | $0.00104 |
| `gemini-4-argon`, now | Not available | $0.00934 | $0.02434 |
| `gemini-4-argon`, from 1 Dec 2026 | Not available | $0.01868 | $0.04868 |

### Gaps
- No provider publishes output tokens for a one-screenshot, one-answer call. The real R value has to be measured from `usage` on real prompts.
- Neither Groq nor DeepSeek has a sentence saying reasoning tokens are billed at the output rate. Their usage fields and pricing wording point that way, but this is my reading, not a quoted statement.

## 4. Does each model accept base64 images on an OpenAI-compatible Chat Completions endpoint, and is JSON schema or only JSON object mode documented, including with image input?

### Takeaway
All options except `deepseek-v4-pro` accept base64 images on an OpenAI-compatible Chat Completions endpoint. xAI labels that endpoint legacy, and Google says its OpenAI layer is still in beta. Only Groq documents JSON output with an image on Chat Completions, and that is JSON object mode. DeepSeek's Chat Completions API offers no JSON schema mode.

### Cited Findings

| Option | Endpoint | Base64 image | JSON object | JSON schema | Image with JSON documented together? |
|---|---|---|---|---|---|
| xAI `grok-4.7` and cheaper models | `https://api.x.ai/v1/chat/completions` | Yes, `image_url.url` data URL with optional `detail` | Yes | Yes | Not documented |
| Groq `qwen/qwen3.8-27b` | `https://api.groq.com/openai/v1/chat/completions` | Yes | Yes | Yes, `strict: true` and `false` | Yes for JSON object; not for schema |
| DeepSeek `deepseek-flash` | `https://api.deepseek.com/chat/completions` | Yes | Yes | Not offered: only `text` and `json_object` | Not documented |
| DeepSeek `deepseek-v4-pro` | Same | No: Vision "Not supported" | Yes | Not offered | n/a |
| Gemini | `https://generativelanguage.googleapis.com/v1beta/openai/chat/completions` | Yes, `data:image/jpeg;base64,` | Not separately described | Yes, through `response_format` | Yes on the native Interactions API; not on the OpenAI page |

- **xAI endpoint status:** "Chat Completions is offered as a legacy endpoint." — [xAI Chat Completions (Legacy)](https://docs.x.ai/developers/model-capabilities/legacy/chat-completions.md). The comparison table heads the column "Chat Completions API (Deprecated)" — [xAI comparison](https://docs.x.ai/developers/model-capabilities/text/comparison.md). "New integrations should use Responses" — [xAI Chat Completions reference](https://docs.x.ai/developers/rest-api-reference/inference/chat-completions.md).
- **xAI page conflict:** the Grok 4.7 page lists only the Responses API under APIs — [Grok 4.7](https://docs.x.ai/developers/grok-4-7.md). Yet the legacy page, the rate-limits example and x.ai/api all show `grok-4.7` on Chat Completions — [xAI Chat Completions (Legacy)](https://docs.x.ai/developers/model-capabilities/legacy/chat-completions.md); [xAI Rate Limits](https://docs.x.ai/developers/rate-limits); [x.ai/api](https://x.ai/api).
- **xAI image samples:** the legacy page's base64 message format is general, and its basic samples use `grok-4.7`, but its image code samples still use `model="grok-4"` — [xAI Chat Completions (Legacy)](https://docs.x.ai/developers/model-capabilities/legacy/chat-completions.md).
- **xAI schema:** `response_format` accepts `json_schema` and `json_object`. Limits are guaranteed up to 2,048 for string lengths, 256 for array sizes and 64 for object properties — [xAI Structured Outputs](https://docs.x.ai/developers/model-capabilities/text/structured-outputs.md). The page does not mention images — [xAI Structured Outputs](https://docs.x.ai/developers/model-capabilities/text/structured-outputs.md).
- **xAI on the Responses API:** "When sending images, it is advised to not store request/response history on the server. Otherwise the request may fail." — [xAI Image Understanding](https://docs.x.ai/developers/model-capabilities/images/understanding).
- **Groq images and JSON:** the Vision page has a section titled "JSON Mode with Images" using `response_format = {"type": "json_object"}` — [Groq Vision](https://console.groq.com/docs/vision). Base64 is passed as a `data:image/jpeg;base64,` URL — [Groq Vision](https://console.groq.com/docs/vision).
- **Groq schema:** `qwen/qwen3.8-27b` appears in both the strict and best-effort lists. The page does not address images. "Streaming and tool use are not currently supported with Structured Outputs." — [Groq Structured Outputs](https://console.groq.com/docs/structured-outputs).
- **Groq with reasoning:** the format must be `parsed` or `hidden` with JSON mode; explicitly setting `raw` returns a 400 error — [Groq Reasoning](https://console.groq.com/docs/reasoning).
- **DeepSeek vision:** the `deepseek-flash` page shows base64 in "the standard OpenAI-compatible Chat Completions format". Images are allowed in `user` messages only; in `system` or `assistant` messages they return a 400. Request body limit is 48 MiB and single image limit 32 MiB — [DeepSeek Vision](https://api-docs.deepseek.com/guides/vision.md).
- **DeepSeek JSON:** `response_format.type` "Must be one of `text` or `json_object`" — [DeepSeek Chat Completions](https://api-docs.deepseek.com/api/create-chat-completion.md). The prompt must contain the word "json" — [DeepSeek JSON Output](https://api-docs.deepseek.com/guides/json_mode.md).
- **DeepSeek JSON failure mode:** "if the model's output cannot be recognized as JSON, the API replaces the non-JSON content with spaces... the returned `content` may contain only spaces (appearing empty, even when `finish_reason` is `stop`)" — [DeepSeek JSON Output](https://api-docs.deepseek.com/guides/json_mode.md).
- **DeepSeek Responses API:** `text` is "Partially supported. `format` fully supported" — [DeepSeek Responses API](https://api-docs.deepseek.com/guides/responses_api.md). The page does not say `json_schema` by name.
- **Gemini OpenAI layer:** "Support for the OpenAI libraries is still in beta while we extend feature support." The page shows base64 images and structured output through `client.beta.chat.completions.parse` — [Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai).
- **Gemini image with schema:** the object detection example passes an image and `response_format` with a JSON schema on `gemini-3.8-flash`, through the native Interactions API — [Gemini Image Understanding](https://ai.google.dev/gemini-api/docs/image-understanding).
- **Gemini schema limits:** a schema that is too complex can fail with `400 INVALID_ARGUMENT` — [Gemini Structured Output](https://ai.google.dev/gemini-api/docs/structured-output).
- **Gemini media resolution on the OpenAI layer:** the `extra_body` table lists `cached_content` and `thinking_config` for chat, and neither `media_resolution` nor `detail` appears on the page — [Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai).

### Inferences
- On xAI, `image_url` and `response_format` are both ordinary Chat Completions fields, so sending both should work, but no page says so. The same reasoning applies to DeepSeek and to Groq schema mode.
- On the Gemini OpenAI layer, an image probably stays at default resolution because no documented field changes it. That would hold it at the 1,120 default, or at 1,548 if the tile rule applies.
- For DeepSeek, code would need to handle a blank `content` and retry, because a `stop` finish does not prove valid JSON came back.

### Gaps
- None of the four providers has an official example of base64 image plus strict JSON schema on Chat Completions. Only a live test can confirm this for each model.
- I found no statement that `deepseek-flash` thinking mode is incompatible with JSON Output, or that it is fully compatible.

## 5. Is there a free tier for each, what are its real limits, and is free-tier content used for training or product improvement?

### Takeaway
Groq and Gemini have free API tiers. xAI and DeepSeek document none. Groq's free limits are published and its terms bar training. Gemini's free tier does use content for product improvement with possible human review, and Google no longer publishes per-model free limits outside a signed-in page.

### Cited Findings

| Provider | Free API tier? | Limits | Training or improvement |
|---|---|---|---|
| xAI | No | n/a | n/a |
| Groq | Yes, Free plan | Qwen: 30 RPM, 1K RPD, 8K TPM, 200K TPD | Not permitted without permission |
| DeepSeek | None documented | n/a | Same terms as paid; see section 8 |
| Gemini | Yes, except `gemini-4-argon` | Only shown in signed-in AI Studio | Yes, including human review |

- **xAI:** "API usage is billed per token rather than free, but the Playground comes with every Console account" — [x.ai/api](https://x.ai/api).
- **xAI credits:** "In some instances we may offer free credits in exchange for you agreeing to permit us to train on your business data." — [xAI Enterprise FAQ](https://x.ai/legal/faq-enterprise). Billing mentions a promo code field but no standing free amount — [xAI Billing](https://docs.x.ai/console/billing.md).
- **Groq limits:** the Free table shows `qwen/qwen3.8-27b` at 30 RPM, 1K RPD, 8K TPM, 200K TPD — [Groq Rate Limits](https://console.groq.com/docs/rate-limits).
- **Groq training:** "Groq is not permitted to use Inputs or Outputs for training or fine-tuning any AI Model Services or other models, unless explicitly granted permission or instructed by Customer." — [Groq Services Agreement](https://console.groq.com/docs/legal/services-agreement). The agreement governs "GroqChat, Groq Playground, GroqCloud, and any other service provided by Groq for developers" — [Groq Services Agreement](https://console.groq.com/docs/legal/services-agreement).
- **DeepSeek:** the pricing page mentions a "granted balance" used before topped-up balance, with no amount or eligibility — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing). The terms say "free quota" details follow the product pages — [DeepSeek Open Platform Terms](https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html). HTTP 402 means "You have run out of balance." — [DeepSeek Error Codes](https://api-docs.deepseek.com/quick_start/error_codes.md).
- **Gemini availability:** input and output are "Free of charge" for all listed models except `gemini-4-argon`, which is "Not available" on Free — [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing).
- **Gemini limits:** "Rate limits depend on a variety of factors (such as your usage tier) and can be viewed in Google AI Studio." — [Gemini Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits).
- **Gemini data use:** the pricing row "Used to improve our products" is "Yes" on Free and "No" on Paid — [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing).
- **Gemini free-tier terms:** "Google uses the content you submit to the Services and any generated responses to provide, improve, and develop Google products and services and machine learning technologies". "human reviewers may read, annotate, and process your API input and output". "Do not submit sensitive, confidential, or personal information to the Unpaid Services." — [Gemini API Terms](https://ai.google.dev/gemini-api/terms). These terms apply to the free tier.
- **Gemini regional exception:** in the EEA, Switzerland or the UK, the Paid data terms apply even to unpaid quota — [Gemini API Terms](https://ai.google.dev/gemini-api/terms).
- **Unverified third-party Gemini limits, conflicting:** one site gives 5 RPM, 250,000 TPM and 20 RPD for 3.8 and 3.6 Flash, and 10 RPM, 250,000 TPM and 500 RPD for 3.5 and 3.1 Flash-Lite, citing AI Studio — [ScriptByAI](https://www.scriptbyai.com/gemini-api-free-tier-limits/). Another gives about 10 RPM and 1,500 RPD for 3.x Flash, citing community tracking — [Klymentiev blog](https://klymentiev.com/blog/gemini-api-free-tier). I could not check either.

### Inferences
- On Groq's free plan, 8K TPM is the limit that matters, not 30 RPM. One screenshot call uses about 2,498 tokens (2,048 image, 300 prompt, 150 answer), or about 15,000 TPM at one call every 10 seconds. That is nearly twice 8K TPM, leaving room for about 3 calls per minute.
- On the same assumptions, 200K TPD allows about 80 calls per day, or about 13 minutes of steady use at one call per 10 seconds. 1K RPD alone would allow 2.8 hours. This assumes image tokens count toward TPM, which Groq does not state outright.
- If ScriptByAI's figures are right, one call every 10 seconds (6 RPM) would exceed 5 RPM on 3.8 and 3.6 Flash, and 20 RPD would run out in about 3.3 minutes. Treat this as a lead to check in AI Studio, not as a fact.
- The Groq agreement has no free-plan carve-out, so its no-training clause appears to apply to the Free plan as well.

### Gaps
- Actual Gemini free limits per model could not be verified. `aistudio.google.com/rate-limit` redirects to sign-in, and Google's public page and its localized versions have no per-model RPM, TPM or RPD table.
- Any current DeepSeek sign-up credit could not be checked because the platform site was unreachable.

## 6. What are the rate limits on the lowest paid tier for one user sending about one request every 10 seconds, and do pages conflict?

### Takeaway
At 6 requests per minute, the published limits on xAI's Tier 0, Groq's Developer plan and DeepSeek are nowhere near binding. Gemini's paid per-model limits are not public, so its case can't be confirmed, though the published spend limit is not a concern at this volume.

### Cited Findings

| Provider and lowest paid level | Requests | Tokens | Other | Source |
|---|---|---|---|---|
| xAI Tier 0, `grok-4.7`, `4.6`, `4.5` | 150 RPS | 50M TPM | Tier needs $0 spend | [xAI Rate Limits](https://docs.x.ai/developers/rate-limits) |
| xAI Tier 0, `grok-4.3`, `grok-4.20-*`, `grok-build-0.1` | 37 RPS | 10M TPM | | [xAI Rate Limits](https://docs.x.ai/developers/rate-limits) |
| Groq Developer, `qwen/qwen3.8-27b` | 1K RPM, 500K RPD | 250K TPM, no TPD shown | Needs a payment method | [Groq Rate Limits](https://console.groq.com/docs/rate-limits); [Groq Models](https://console.groq.com/docs/models) |
| DeepSeek `deepseek-flash` | Concurrency 2,500 per account | None published | `deepseek-v4-pro` concurrency 500 | [DeepSeek Rate Limit](https://api-docs.deepseek.com/quick_start/rate_limit.md) |
| Gemini Tier 1 | Not published | Not published | $10 per 10 minutes spend limit; $250 billing cap | [Gemini Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits) |

- **xAI counting:** prompt tokens including image, completion, reasoning and cached tokens all count toward TPM. "Your per-second limit is derived from your per-minute request budget (RPM / 48, with a minimum of 2)". Tier is based on cumulative spend since 1 Jan 2026 — [xAI Rate Limits](https://docs.x.ai/developers/rate-limits). That page is dated October 5, 2026.
- **xAI payment:** usage comes from prepaid credits or monthly invoicing, and "Monthly invoiced billing is disabled by default." The auto top-up minimum is $5 — [xAI Billing](https://docs.x.ai/console/billing.md).
- **Groq plan terms:** moving to Developer requires "a valid payment method", with no immediate charge. New users are invoiced as lifetime usage crosses $1, $10, $100, $500 and $1,000, with different thresholds for India — [Groq Billing FAQs](https://console.groq.com/docs/billing-faqs).
- **Groq notes:** limits apply at organization level, the table is "a high level summary and there may be exceptions", and some organizations have separate input and output token limits — [Groq Rate Limits](https://console.groq.com/docs/rate-limits).
- **DeepSeek behaviour:** a request counts as one concurrent connection until the response completes. Empty lines or keep-alive comments may be returned while waiting. "If the request has not started inference after 10 minutes, the server will close the connection." — [DeepSeek Rate Limit](https://api-docs.deepseek.com/quick_start/rate_limit.md).
- **Gemini rules:** limits are per project, not per API key, and RPD resets at midnight Pacific. "Rate limits are more restricted for experimental and preview models." "Specified rate limits are not guaranteed and actual capacity may vary." — [Gemini Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits).
- **Gemini payment:** moving to paid means linking billing and prepaying at least $5. Credits expire after 1 year and are generally not refundable — [Gemini Billing](https://ai.google.dev/gemini-api/docs/billing).

#### Conflicts between pages
- **Groq table label:** the page says "the limits shown below are the base limits for the Developer plan", but the default table shows the Free values (30 RPM, 1K RPD, 8K TPM, 200K TPD). The Developer values sit in a second tab — [Groq Rate Limits](https://console.groq.com/docs/rate-limits). Those Developer RPM and TPM values match the Models page — [Groq Models](https://console.groq.com/docs/models).
- **Groq "unlimited":** the billing FAQ mentions "unlimited requests" as a Developer benefit — [Groq Billing FAQs](https://console.groq.com/docs/billing-faqs). The limits table shows 500K RPD — [Groq Rate Limits](https://console.groq.com/docs/rate-limits).
- **DeepSeek QPS:** the error page says 429 can mean exceeding "a concurrency or QPS limit" — [DeepSeek Error Codes](https://api-docs.deepseek.com/quick_start/error_codes.md). The rate limit page publishes no QPS number — [DeepSeek Rate Limit](https://api-docs.deepseek.com/quick_start/rate_limit.md).
- **Groq preview caution:** Qwen's 250K TPM sits on a model labelled for evaluation only; see section 9 — [Groq Models](https://console.groq.com/docs/models).

### Inferences
- One request every 10 seconds is 0.1 requests per second, or 6 RPM. That is about 0.07% of xAI Tier 0's 150 RPS, about 0.3% of its 37 RPS, and 0.6% of Groq Developer's 1K RPM.
- Groq Developer at 15,000 TPM is about 6% of 250K TPM, using the assumptions in section 5.
- DeepSeek concurrency stays at 1 for a single sequential user.
- Gemini's $10 per 10 minutes covers 60 calls in that window, each of which costs far less than the roughly $0.17 needed to reach the limit, so spend is not the risk.

### Gaps
- Gemini Tier 1 RPM, TPM and RPD per model are not public. A signed-in AI Studio check is the only primary source.

## 7. What are typical latency and output speed for each, ideally with image input?

### Takeaway
No source measures latency with image input. AA's text benchmark shows thinking level matters more than the model: first-answer time ranges from under 1 second with reasoning off to 20 to 40+ seconds at high effort. AA has no measurement of Groq-hosted Qwen 3.8, so Groq's speed figure comes from Groq alone.

### Cited Findings
- AA's default benchmark uses 10k input tokens, not images — [AA Gemini 4 Carbon providers](https://artificialanalysis.ai/models/gemini-4-carbon/providers). No AA measurement dates are shown on these pages.
- Groq states "~450+ tps" for Qwen — [Qwen model page](https://console.groq.com/docs/model/qwen/qwen3.8-27b). Its AA provider page tracks six Groq models and Qwen is not one of them — [AA Groq](https://artificialanalysis.ai/providers/groq). Groq is not among the hosts AA lists for Qwen3.8 27B — [AA Qwen3.8 27B providers](https://artificialanalysis.ai/models/qwen3-8-27b/providers).

First-party API values, where AA separates them. First chunk can arrive before the answer on models that stream reasoning. E2E is AA's end-to-end response time.

| Model and effort | Host | Speed (t/s) | First chunk (s) | First answer token (s) | E2E (s) | Source |
|---|---|---|---|---|---|---|
| Grok 4.7 low | xAI | 88.1 | 5.74 | 5.74 | 11.42 | [AA](https://artificialanalysis.ai/models/grok-4-7-low/providers) |
| Grok 4.7 high | xAI | 106.1 | 21.25 | 21.25 | 25.97 | [AA](https://artificialanalysis.ai/models/grok-4-7-high/providers) |
| Grok 4.7 xhigh | xAI | 86.8 | 42.06 | 42.06 | 47.81 | [AA](https://artificialanalysis.ai/models/grok-4-7) |
| Grok 4.3 non-reasoning | xAI | 98.4 | 0.74 | 0.74 | 5.82 | [AA](https://artificialanalysis.ai/models/grok-4-3-non-reasoning/providers) |
| Grok Build 0.1 0616 | xAI | 118.4 | 1.25 | 18.14 | 22.37 | [AA](https://artificialanalysis.ai/models/grok-build-0-1-06-16) |
| DeepSeek V4.1 Flash 1017 max | DeepSeek | 178.3 | 1.20 | 12.41 | 15.22 | [AA](https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017/providers) |
| Qwen3.8 27B xhigh | Alibaba Cloud (not Groq) | 39.9 | 3.91 | 54.01 | 66.53 | [AA](https://artificialanalysis.ai/models/qwen3-8-27b/providers) |
| Qwen3.8 27B non-reasoning | Alibaba Cloud (not Groq) | 45.7 | 3.87 | 3.87 | 14.80 | [AA](https://artificialanalysis.ai/models/qwen3-8-27b-non-reasoning/providers) |
| Gemini 3.8 Flash high | Google | 140.1 | 27.53 | 27.53 | 31.10 | [AA](https://artificialanalysis.ai/models/gemini-3-8-flash/providers) |
| Gemini 3.6 Flash high | Google | 190.6 | 15.19 | 15.19 | 17.81 | [AA](https://artificialanalysis.ai/models/gemini-3-6-flash/providers) |
| Gemini 3.5 Flash-Lite | Google | 460.6 | 6.86 | 6.86 | 7.94 | [AA](https://artificialanalysis.ai/models/gemini-3-5-flash-lite/providers) |
| Gemini 3.1 Flash-Lite high | Google | 326.8 | 4.75 | 4.75 | 6.28 | [AA embedded record](https://artificialanalysis.ai/models/gemini-4-carbon) |
| Gemini 3 Flash Preview non-reasoning | Google | 187.0 | 0.90 | 0.90 | 3.58 | [AA](https://artificialanalysis.ai/models/gemini-3-flash) |
| Gemini 3 Flash Preview reasoning | Google | 183.0 | 6.04 | 6.04 | 8.77 | [AA](https://artificialanalysis.ai/models/gemini-3-flash-reasoning) |
| Gemini 2.5 Flash non-reasoning | Google | 202.6 | 0.36 | 0.36 | 2.83 | [AA](https://artificialanalysis.ai/models/gemini-2-5-flash) |
| Gemini 2.5 Flash reasoning | Google | 208.2 | 14.26 | 14.26 | 16.67 | [AA](https://artificialanalysis.ai/models/gemini-2-5-flash-reasoning) |
| Gemini 2.5 Flash-Lite non-reasoning | Google | 300.9 | 0.30 | 0.30 | 1.96 | [AA](https://artificialanalysis.ai/models/gemini-2-5-flash-lite/providers) |
| Gemini 2.5 Flash-Lite reasoning | Google | 339.6 | 12.67 | 12.67 | 14.15 | [AA](https://artificialanalysis.ai/models/gemini-2-5-flash-lite-reasoning) |
| Gemini 4 Argon high | Google AI Studio | 101.5 | 41.56 | 41.56 | 46.49 | [AA](https://artificialanalysis.ai/models/gemini-4-argon/providers) |
| Gemini 4 Carbon high (restricted access) | Google, ID `models/carbon-g` | 98.0 | 103.13 | 103.13 | 108.23 | [AA](https://artificialanalysis.ai/models/gemini-4-carbon/providers) |

- AA has no first-party speed for DeepSeek V4.1 Flash 1017 non-reasoning. The 1,486 t/s and 1.15 s figures shown there belong to the third-party host Inco (FAST), and the same page gives no DeepSeek-hosted speed — [AA DeepSeek non-reasoning providers](https://artificialanalysis.ai/models/deepseek-v4-1-flash-1017-non-reasoning/providers).
- **Spread:** Grok 4.7's first-chunk time at xhigh ranged from 7.5 s (p05) to 310.7 s (p95), median 42.06 s — [AA Grok 4.7](https://artificialanalysis.ai/models/grok-4-7).
- **AA internal inconsistency:** its model and provider pages differ for the same variant. Grok 4.7 high shows 78.5 t/s and 32.59 s on the model page against 106.1 t/s and 21.25 s on the provider page — [AA model page](https://artificialanalysis.ai/models/grok-4-7-high); [AA provider page](https://artificialanalysis.ai/models/grok-4-7-high/providers). Gemini 3.8 Flash high shows 120.3 t/s and 24.69 s against 140.1 t/s and 27.53 s — [AA model page](https://artificialanalysis.ai/models/gemini-3-8-flash); [AA provider page](https://artificialanalysis.ai/models/gemini-3-8-flash/providers).
- For another host's Qwen3.8 27B speed, AA shows Nebius (FP4) at 402.7 t/s and 6.36 s to first answer token — [AA Qwen3.8 27B providers](https://artificialanalysis.ai/models/qwen3-8-27b/providers).

### Inferences
- These numbers fit a standard AA test of 500 answer tokens, plus 2,000 reasoning tokens for models that stream reasoning. For example, DeepSeek's record works out to 11.43 s × 175 t/s ≈ 2,000 and 2.86 s × 175 t/s ≈ 500. A short JSON answer with a 1.5k-token prompt should differ, probably with faster times.
- AA's figures are for high or maximum effort on several models, which is well above what an MCQ call needs. The low and non-reasoning rows are closer to that use. DeepSeek's only first-party row is at max effort.
- Image preprocessing could add time on any provider, but no source quantifies it.

### Gaps
- No image-input latency measurement was found for any of these models.
- No independent measurement of Groq's Qwen 3.8 exists on AA. Groq's "~450+ tps" is vendor-stated.
- AA has no live page for `gemini-3.1-flash-lite`: the provider URL returns 404, so that row comes from a record embedded in another AA page. AA has no first-party low-effort speed data for Gemini 3.8 Flash.

## 8. Where is data processed and stored, and what do the terms say about training on API inputs?

### Takeaway
xAI, Groq and paid Gemini all say API content is not used for training by default. DeepSeek is the exception: its general terms allow de-identified use of inputs and outputs, and storage is in China. Free Gemini does use content for improvement. Only Groq says inference requests are not retained by default. xAI keeps data for 30 days and Google for 55.

### Cited Findings

#### xAI
- **Applies to API customers:** "Our Enterprise Terms of Service govern the use of our Services for developers and businesses, including SpaceXSI APIs and PromptIDE." — [xAI Terms](https://x.ai/legal/terms-of-service). The Privacy Policy "does not apply to data that we process on behalf of customers of our business offerings, such as the SpaceXSI API" — [xAI Privacy Policy](https://x.ai/legal/privacy-policy).
- **Training:** "SpaceXSI never trains on your API inputs or outputs without your explicit permission." — [xAI Security FAQ](https://docs.x.ai/developers/faq/security.md). This is about API customers. "No, we do not use your business data, including inputs (prompts) or outputs (answers), for training our models." — [xAI Enterprise FAQ](https://x.ai/legal/faq-enterprise).
- **Permitted use:** the license covers providing the Services, addressing fraud, security risks, abuse or non-compliance, and safety or compliance operations — [xAI Enterprise Terms](https://x.ai/legal/terms-of-service-enterprise). Except under ZDR, xAI "may create and use, for any lawful purpose, de-identified and/or aggregated data" that is "irreversibly anonymized" — [xAI Enterprise Terms](https://x.ai/legal/terms-of-service-enterprise).
- **Retention:** "By default, all API requests and responses are stored on our servers (encrypted at rest) for 30 days for auditing purposes in the event of suspected abuse or misuse." — [xAI Security FAQ](https://docs.x.ai/developers/faq/security.md). The terms allow longer retention where needed for law, safety or abuse investigation — [xAI Enterprise Terms](https://x.ai/legal/terms-of-service-enterprise). The Enterprise Terms and Privacy Policy are both dated October 27, 2026.
- **Location:** "The default endpoint, `https://api.x.ai`, does not guarantee a processing region." The US endpoint covers request handling, inference, moderation and retained data, but serves only `grok-4.7` and `grok-4.6` at 1.1x — [xAI Security FAQ](https://docs.x.ai/developers/faq/security.md); [xAI Regional Endpoints](https://docs.x.ai/developers/advanced-api-usage/regions.md).
- **Model regions:** `grok-4.7` lists us-east-1, us-west-2 and us-central-1; `grok-4.3` lists us-east-1, eu-west-1 and us-west-2 — [grok-4.7](https://docs.x.ai/developers/models/grok-4.7.md); [grok-4.3](https://docs.x.ai/developers/models/grok-4.3.md). The DPA allows processing "on a global basis" — [xAI DPA](https://x.ai/legal/data-processing-addendum).
- **Personal data clause:** "Customer represents and warrants that it will not intentionally submit... any Personal Data to the Services except through SpaceXSI's ZDR-Enabled API." — [xAI Enterprise Terms](https://x.ai/legal/terms-of-service-enterprise).
- **ZDR contrast:** the Security FAQ says "For most customers, we do not recommend enabling ZDR" — [xAI Security FAQ](https://docs.x.ai/developers/faq/security.md). The personal data clause above points personal data toward ZDR — [xAI Enterprise Terms](https://x.ai/legal/terms-of-service-enterprise).
- **Storage wording conflict:** the comparison table says Chat Completions has "No storage — manage history yourself" — [xAI comparison](https://docs.x.ai/developers/model-capabilities/text/comparison.md). The FAQ says all API requests and responses are stored for 30 days — [xAI Security FAQ](https://docs.x.ai/developers/faq/security.md).

#### Groq
- **Applies to API customers:** the Services Agreement governs GroqCloud — [Groq Services Agreement](https://console.groq.com/docs/legal/services-agreement).
- **Training:** "Groq does not access, use, store, or retain Inputs or Outputs except as necessary to provide the Cloud Services, in accordance with the Customer's permission or instruction, comply with applicable law, ensure the reliable operation of the Cloud Services, or confirm Customer's compliance with the AUP." and "Groq is not permitted to use Inputs or Outputs for training or fine-tuning any AI Model Services or other models, unless explicitly granted permission or instructed by Customer." — [Groq Services Agreement](https://console.groq.com/docs/legal/services-agreement).
- **Retention:** "By default, Groq does not retain customer data for inference requests." Inputs and outputs may be logged when troubleshooting errors or investigating suspected abuse, kept "for up to 30 days" unless the law requires longer — [Your Data in GroqCloud](https://console.groq.com/docs/your-data).
- **Location:** "All customer data is retained in Google Cloud Platform (GCP) buckets located in the United States." — [Your Data in GroqCloud](https://console.groq.com/docs/your-data). "Groq is located in the United States, and maintains processing operations in various global jurisdictions." — [Groq Privacy Policy](https://groq.com/privacy-policy). The `x-groq-region` response header shows which datacenter handled a request — [Groq Optimizing Latency](https://console.groq.com/docs/production-readiness/optimizing-latency).
- **Conflict:** "All customers may enable Zero Data Retention" — [Your Data in GroqCloud](https://console.groq.com/docs/your-data). The agreement says "Eligible Customers may enable" it — [Groq Services Agreement](https://console.groq.com/docs/legal/services-agreement).

#### DeepSeek
- **Which terms apply:** the Open Platform Terms (effective April 29, 2026) apply to the API and serve as a "Specific Agreement" to the general Terms of Use — [DeepSeek Open Platform Terms](https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html). Developers must comply with the Terms of Use "especially regarding user conduct norms" — [DeepSeek Open Platform Terms](https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html).
- **Training, general terms:** "Under the premise of secure encryption technology processing, strict de-identification rendering, and irreversibility to identify specific individuals, we may, to a minimal extent, use Inputs and Outputs to provide, maintain, operate, develop or improve the Services or the underlying technologies supporting the Services. If you refuse to allow us to process the data in the manner described above, you can opt out by turning off 'Improve the model for everyone'." — [DeepSeek Terms of Use](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html), section 4.3, last updated March 27, 2026.
- **Open Platform Terms on training:** they contain no clause on training on inputs. The only training mention is that you may use Inputs and Outputs for "training other models" — [DeepSeek Open Platform Terms](https://cdn.deepseek.com/policies/en-US/deepseek-open-platform-terms-of-service.html).
- **Training disclosure:** optimization training pairs are "produced by our research team, with a small portion potentially based on user input." "If user input is used to construct training data, we apply secure encryption, strict de-identification, and anonymization". "Users are also given the right to opt out." — [DeepSeek Model Mechanism and Training Methods](https://cdn.deepseek.com/policies/en-US/model-algorithm-disclosure.html).
- **Privacy policy:** it covers use "To improve and develop the Services and to train and improve our technology, such as our machine learning models and algorithms." It also references paid use "in our open platform". Data from end users of developers' applications is not covered — [DeepSeek Privacy Policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html), last updated Feb 10, 2026.
- **Storage:** "we directly collect, process and store your Personal Data in People's Republic of China." — [DeepSeek Privacy Policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html).
- **Retention:** "we keep this Personal Data for as long as you have an account. This Personal Data includes your account Personal Data, input and payment Personal Data." — [DeepSeek Privacy Policy](https://cdn.deepseek.com/policies/en-US/deepseek-privacy-policy.html).

#### Google Gemini API
- **Paid training, applies to API customers on a billing-enabled project:** "When you use Paid Services, including, for example, the paid quota of the Gemini API, Google doesn't use your prompts (including associated system instructions, cached content, and files such as images, videos, or documents) or responses to improve our products" — [Gemini API Terms](https://ai.google.dev/gemini-api/terms). "Your access to Gemini API is a 'Paid Service' only when accessing the API through a Cloud Project associated with an active billing account." — [Gemini API Terms](https://ai.google.dev/gemini-api/terms).
- **Free tier:** content is used for improvement and may get human review; see section 5 — [Gemini API Terms](https://ai.google.dev/gemini-api/terms).
- **Paid logging and location:** "Google logs prompts and responses for a limited period of time, solely for detecting and preventing violations of the Prohibited Use Policy... This data may be stored transiently or cached in any country in which Google or its agents maintain facilities." — [Gemini API Terms](https://ai.google.dev/gemini-api/terms). Abuse-monitoring retention is "fifty-five (55) days" — [Gemini Abuse Monitoring](https://ai.google.dev/gemini-api/docs/usage-policies). Flagged content may be reviewed by authorized Google employees — [Gemini Abuse Monitoring](https://ai.google.dev/gemini-api/docs/usage-policies).
- **New default logging:** "Logging is on by default for Interactions API calls, and for Generate Content API calls in projects created on or after October 26, 2026." Logs last up to 55 days by default, can be set to 7, 14, 28 or 55 days, are private to the project, and are "not used for product improvement or development" unless shared in a dataset — [Gemini Data Logging](https://ai.google.dev/gemini-api/docs/logs-policy); [Gemini Release Notes](https://ai.google.dev/gemini-api/docs/changelog).
- **ZDR:** "If your workload requires guaranteed zero data retention or enterprise data processing agreements, use Vertex AI." — [Gemini ZDR](https://ai.google.dev/gemini-api/docs/zdr).

### Inferences
- A screenshot may show names, email addresses or code from a user's screen. That matters for the xAI personal data clause, Gemini's free-tier warning, and DeepSeek's storage in China.
- xAI's "No storage" table row most likely means conversation state, since the FAQ's 30-day audit retention covers all API requests.
- The DeepSeek opt-out is described as a chat setting. The Open Platform and chat service "use the same account", but no document says that toggle covers API traffic. Read cautiously, DeepSeek has not promised that API inputs are excluded from improvement use.
- Keeping `store=false` on Gemini is relevant only for APIs where logging is on. The logging page does not mention the OpenAI-compatible endpoint.

### Gaps
- It is not documented whether DeepSeek's "Improve the model for everyone" switch applies to API calls, or whether a separate API setting exists. The platform site and FAQ could not be read.
- I found no region-selection option for the Gemini Developer API, and no statement of where Groq runs Qwen inference specifically.
- Whether the new Gemini log default covers `/v1beta/openai/chat/completions` calls is not stated.

## 9. Are any of these models marked preview, experimental, legacy or scheduled for retirement?

### Takeaway
Every image-capable model on Groq is preview, and Groq says preview models are not for production. Gemini 2.5 models are restricted to past users, and Gemini 4 Carbon is not available to ordinary developers. `gemini-3-flash-preview` is preview and `gemini-3.1-flash-lite` has an earliest shutdown date of 7 May 2027. On xAI the concern is the endpoint, not the models: Chat Completions is legacy.

### Cited Findings

| Model | Status | Source |
|---|---|---|
| `grok-4.7` | Current flagship; no retirement date found | [xAI Models](https://docs.x.ai/developers/models.md) |
| `grok-4.20-multi-agent-0309` | Titled "Multi-Agent Beta" | [Model page](https://docs.x.ai/developers/models/grok-4.20-multi-agent-0309.md) |
| xAI Chat Completions endpoint | "legacy endpoint"; also headed "(Deprecated)" | [Legacy page](https://docs.x.ai/developers/model-capabilities/legacy/chat-completions.md); [Comparison](https://docs.x.ai/developers/model-capabilities/text/comparison.md) |
| `qwen/qwen3.8-27b` | Preview | [Groq Models](https://console.groq.com/docs/models) |
| `meta-models/muse-spark-open` | Limited preview, Enterprise, Contact Sales | [Groq Vision](https://console.groq.com/docs/vision); [Groq Models](https://console.groq.com/docs/models) |
| `deepseek-flash` | Current, no preview label | [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing) |
| `deepseek-v4-flash`, `deepseek-v4-flash-vision-exp` | Retired; names still accepted and served by V4.1 Flash | [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing) |
| `deepseek-v4-pro` | Served, see conflict below | [DeepSeek Change Log](https://api-docs.deepseek.com/updates.md) |
| `gemini-4-argon` | Stable; GA 13 Oct 2026; not listed on the Deprecations page (last updated 2026-10-22) | [Gemini Models](https://ai.google.dev/gemini-api/docs/models); [Release Notes](https://ai.google.dev/gemini-api/docs/changelog); [Deprecations](https://ai.google.dev/gemini-api/docs/deprecations) |
| `gemini-3.8-flash` | Stable; no shutdown date announced | [Gemini Deprecations](https://ai.google.dev/gemini-api/docs/deprecations) |
| `gemini-3.6-flash` | Stable; "previous-generation"; no shutdown date | [Model page](https://ai.google.dev/gemini-api/docs/models/gemini-3.6-flash); [Deprecations](https://ai.google.dev/gemini-api/docs/deprecations) |
| `gemini-3.5-flash-lite` | Stable; no shutdown date | [Gemini Deprecations](https://ai.google.dev/gemini-api/docs/deprecations) |
| `gemini-3.1-flash-lite` | Stable; earliest shutdown 7 May 2027; replacement `gemini-3.5-flash-lite` | [Gemini Deprecations](https://ai.google.dev/gemini-api/docs/deprecations) |
| `gemini-3-flash-preview` | Preview; pricing calls it "Our legacy Flash model"; no shutdown date; replacement `gemini-3.6-flash` | [Deprecations](https://ai.google.dev/gemini-api/docs/deprecations); [Pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| `gemini-2.5-flash`, `gemini-2.5-flash-lite` | Not deprecated, but access limited to past users | [Gemini Deprecations](https://ai.google.dev/gemini-api/docs/deprecations) |

- **Groq preview wording:** "Preview models are intended for evaluation purposes only and should not be used in production environments as they may be discontinued at short notice." — [Groq Models](https://console.groq.com/docs/models).
- **Groq's production list has no vision model:** production entries are GPT-OSS, Whisper and Enterprise Llama models — [Groq Models](https://console.groq.com/docs/models). The vision page lists only Qwen and Muse Spark Open — [Groq Vision](https://console.groq.com/docs/vision).
- **Groq churn:** `qwen/qwen3.6-27b` was shut down on 14 Sept 2026 in favour of 3.8, although Groq's June 2026 notice had named it as a replacement for Llama 4 Scout. `llama-4-scout` went on 17 July 2026 and `llama-4-maverick` on 9 March 2026 — [Groq Deprecations](https://console.groq.com/docs/deprecations). Release notes also mention an Enterprise vision model, `qwen/qwen3-vl-32b-instruct`, which is not on the current Models page — [Groq Changelog](https://console.groq.com/docs/changelog); [Groq Models](https://console.groq.com/docs/models).
- **Gemini 2.5 restriction:** "we are limiting access to the 2.5 models to users who have actively used them in the past. These models are not deprecated and will continue to be served until further notice through the API. For any new projects, use our latest models: 3.5 Flash-Lite or 3.8 Flash." — [Gemini 2.5 Flash page](https://ai.google.dev/gemini-api/docs/models/gemini-2.5-flash).
- **Gemini 4 Carbon:** "Starting this week, we will make Carbon available to a subset of cyber defenders and will gradually phase access to additional trusted partners through our Fairwind Program. We're continuing to gather feedback and iterate on guardrails before making Carbon available to developers, businesses, and consumers via our product surfaces as soon as possible." — [Google blog, Oct 28, 2026](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/).
- **Carbon in Google's catalog:** it is absent from the Models page (updated 2026-10-28), the pricing page (2026-10-30) and the release notes through 30 Oct 2026, and the guessed model page URL returns 404 — [Gemini Models](https://ai.google.dev/gemini-api/docs/models); [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing); [Gemini Release Notes](https://ai.google.dev/gemini-api/docs/changelog).
- **Carbon conflict:** AA says it "is available through Google" and benchmarks an ID of `models/carbon-g` at $4 and $20 — [AA Gemini 4 Carbon providers](https://artificialanalysis.ai/models/gemini-4-carbon/providers). That disagrees with Google's restricted-access statement and with Google's $2 and $10 introductory price — [Google blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/). A reseller page checked on Oct 30 also says it is not in the public catalog — [EvoLink](https://evolink.ai/gemini-4-carbon).
- **DeepSeek V4 Pro conflict:** the release note says "We're phasing out V4-Pro" and that from 14 Sept 2026 requests "will route to V4.1-Flash at V4.1-Flash rates" — [DeepSeek release note](https://api-docs.deepseek.com/news/news260910.md). The change log says "we have decided to continue providing API services for DeepSeek V4 Pro after September 14, 2026" with notice of any later change — [DeepSeek Change Log](https://api-docs.deepseek.com/updates.md). The pricing page still lists it — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing).
- **AA's "deprecated" flag is not a provider notice:** AA marks Grok 4.3, Grok Build 0.1, Gemini 3.6 Flash and Gemini 2.5 models as deprecated, for example its [Grok 4.3 record](https://artificialanalysis.ai/models/grok-4-3). xAI still sells Grok 4.3 and Google says the 2.5 models are "not deprecated" — [xAI Pricing](https://docs.x.ai/developers/pricing.md); [Gemini Deprecations](https://ai.google.dev/gemini-api/docs/deprecations).

#### Model-name corrections
- All names supplied are valid. `gemini-3-flash-preview` is the real code: the guessed page for `gemini-3-flash` returns 404 — [Gemini 3 Flash preview page](https://ai.google.dev/gemini-api/docs/models/gemini-3-flash-preview).
- `deepseek-flash` is the correct name and currently resolves to DeepSeek-V4.1-Flash-1017 — [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing).
- `gemini-3.7-flash` and `gemini-3.5-flash` are deprecated and route to `gemini-3.8-flash` and `gemini-3.6-flash` — [Gemini Deprecations](https://ai.google.dev/gemini-api/docs/deprecations).
- Gemini 4 Carbon has no published public model code — [Gemini Models](https://ai.google.dev/gemini-api/docs/models).

### Inferences
- For a new project, `gemini-2.5-flash` and `gemini-2.5-flash-lite` may not be available even though they appear with the lowest prices in section 3, unless the account has past usage.
- Groq moved from recommending Qwen 3.6 to shutting it down within about three months, so a Qwen-based setup should expect model IDs to change.
- `models/carbon-g` looks like a pre-release identifier. It should not be treated as a usable public model code.

### Gaps
- I could not test whether a new API key can reach `gemini-2.5-*`, or what "actively used" means in practice.
- No xAI retirement date was found for Chat Completions, Grok 4.3 or Grok 4.20.

## 10. Do any providers apply safety filters or content refusals that could block ordinary questions about software, security, Git or exams?

### Takeaway
No provider lists software, Git or exam questions as blocked. Security is the one real risk area. Grok 4.7 and Gemini 4 Argon both describe new safeguards around cyber misuse, and all four providers ban malicious hacking in their policies. xAI can charge a $0.05 fee for a pre-generation block, and Google returns an HTTP 400. No source gives false-refusal rates for ordinary security study questions.

### Cited Findings

#### xAI
- **Fee:** "When your request is deemed to be in violation of our usage guideline by our system, we will still charge for the generation of the request. For violations that are caught before generation in the Responses API, we will charge a $0.05 usage guideline violation fee per request." — [xAI Pricing](https://docs.x.ai/developers/pricing.md).
- **Safeguards:** "Grok 4.7 was built with an entirely new safeguard stack." It describes "allowing only 3.3% of risky dual-use prompts through while rarely blocking legitimate security work." These are xAI's own claims — [xAI Grok 4.7 announcement](https://x.ai/news/grok-4-7).
- **Policy:** the AUP bans "Engaging in espionage, hacking, defrauding, defaming, scamming, or spamming" and "Jailbreaking, adversarial prompting, or prompt injection" — [xAI AUP](https://x.ai/legal/acceptable-use-policy).
- **Controls:** `guidelines` can only add stricter handling for `nsfw`, `violence` and `profanity`; today the only behaviour is `decline` — [xAI Custom Moderation](https://docs.x.ai/developers/advanced-api-usage/custom-moderation-controls.md).

#### Groq
- **Moderation:** the docs describe content moderation as something you build with separate safeguard models, such as GPT-OSS-Safeguard 20B — [Groq Content Moderation](https://console.groq.com/docs/content-moderation).
- **Policy:** the AUP bars use "to gain unauthorized access to, attack, abuse, interfere with, intercept, disrupt, or exploit any users, systems, or services, including any offensive cyber operations or automated vulnerability discovery and exploitation" and "for phishing, generating, or distributing malware" — [Groq AUP](https://console.groq.com/docs/legal/ai-policy).
- **Exceptions:** customers with adequate safeguards may ask Groq for an exception for "lawful business or research purposes" — [Groq AUP](https://console.groq.com/docs/legal/ai-policy).

#### DeepSeek
- **Filter exists:** `finish_reason` can be "`content_filter` if content was omitted due to a flag from our content filters" — [DeepSeek Chat Completions](https://api-docs.deepseek.com/api/create-chat-completion.md).
- **Review:** DeepSeek may use "technical means to review the behavior of users", including "establishing risk filtering mechanisms, and creating databases for illegal content features" — [DeepSeek Terms of Use](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html).
- **Policy:** the terms forbid content that "constitute, encourage or provide instructions for a criminal offence", and "attempting to probe, scan, or test vulnerabilities in the software system or network without permission" — [DeepSeek Terms of Use](https://cdn.deepseek.com/policies/en-US/deepseek-terms-of-use.html).
- `user_id` is used "to distinguish user identities on your business side for content safety handling" — [DeepSeek Rate Limit](https://api-docs.deepseek.com/quick_start/rate_limit.md).

#### Google
- **Defaults:** adjustable filters default to "Off for Gemini 2.5 and later models". Core harms such as child safety are "always blocked and cannot be adjusted" — [Gemini Safety Settings](https://ai.google.dev/gemini-api/docs/safety-settings).
- **When blocked:** "If a safety filter blocks the input or the model's response, the interaction fails with an HTTP 400 error." Error codes include `safety`, `jailbreak`, `prohibited_content` and `blocklist` — [Gemini Safety Settings](https://ai.google.dev/gemini-api/docs/safety-settings).
- **Argon:** "the model is designed to refuse harmful requests while preserving legitimate, dual-use scientific research". "For trusted defenders and our own internal teams at Google, we'll be releasing Argon without cyber guardrails" — [Google blog, Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/).
- **Policy:** do not generate content that facilitates "Spam, phishing, or malware", or "Circumvention of abuse protections or safety filters" — [Google Generative AI Prohibited Use Policy](https://policies.google.com/terms/generative-ai/use-policy), last modified Dec 17, 2024.
- **Enforcement:** automated systems scan usage. Measures can include "adjusting rate limits or changing which model answers a specific request" — [Gemini Abuse Monitoring](https://ai.google.dev/gemini-api/docs/usage-policies).
- **On the OpenAI layer:** `safety_settings` in `extra_body` is listed for the Images endpoint only, not Chat — [Gemini OpenAI compatibility](https://ai.google.dev/gemini-api/docs/openai).

#### Conditions of use
- **Google:** "Use of Google AI Studio and Gemini API is for developers building with Google AI models for professional or business purposes, not for consumer use." You must be 18 or older, access must be from an available region, and only Paid Services may be offered to users in the EEA, Switzerland or the UK — [Gemini API Terms](https://ai.google.dev/gemini-api/terms); [Available Regions](https://ai.google.dev/gemini-api/docs/available-regions).
- **xAI:** "You must be 18 years old or older to use the SpaceXSI API." — [xAI Enterprise FAQ](https://x.ai/legal/faq-enterprise). "Your model access might vary depending on various factors such as geographical location, account limitations, etc." — [xAI Pricing](https://docs.x.ai/developers/pricing.md).

### Inferences
- None of the policies mention Git, ordinary programming or exam preparation as blocked topics. They should pass, and the realistic risk is limited to security content such as exploit-focused questions.
- The cyber language in Grok 4.7 and Argon suggests that a security question framed around attacking a system is more likely to be refused than a defensive or conceptual one. This is inference, not a documented rule.
- On Groq, the docs describe moderation as opt-in, and no platform filter on Qwen is documented. The model itself may still refuse.
- At xAI, a $0.05 fee is about 10 times the $0.0045 illustrative `grok-4.7` call in section 3, so false positives would have a visible cost if the Responses API is used. The fee sentence names only the Responses API, so its application to Chat Completions is unclear.
- A refusal does not arrive the same way everywhere: an HTTP 400 on Gemini, `content_filter` on DeepSeek, and possibly a billed response on xAI. Code asking for JSON has to handle each.

### Gaps
- I found no independent data on how often any of these models wrongly refuse ordinary security, Git or exam questions. xAI's 3.3% figure covers risky prompts allowed through and is self-reported.
- DeepSeek publishes no list of what its content filter blocks.
- Whether Gemini 3.8 Flash and the Flash-Lite models carry the same cyber guardrails as Argon is not stated in the docs I read. A short test set of real questions is the only way to measure this.
