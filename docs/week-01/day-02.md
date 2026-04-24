# Day 2: Run Open Models Locally And Measure Them

## Goal

Get out of theory mode. Run several open models locally and compare them on the same prompts.

## Why This Day Matters

A lot of beginners form opinions about models from screenshots and hype. Today forces you to measure real behavior on your own hardware.

## Time Budget

- Reading: 20 to 30 minutes
- Setup and runs: 60 to 90 minutes
- Comparison notes and X post: 30 minutes

Total: 2 to 2.5 hours

## Learn Before Starting

- Why inference quality is not just about parameter count.
- How quantization changes memory use and sometimes quality.
- Why benchmarking on your own tasks matters more than generic hype.

## Read Before Starting

- vLLM quickstart: https://docs.vllm.ai/en/latest/getting_started/quickstart.html
- Bitsandbytes quantization docs: https://huggingface.co/docs/transformers/quantization/bitsandbytes
- One practical model card:
  - https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
  - or https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct

Read only enough to run the models and understand the key tradeoffs.

## What You Should Understand By The End

- why "best model" depends on task and hardware
- how quantization and model size affect local usability
- which model is your best candidate for later fine-tuning

## Step-By-Step Agenda

1. Open `day-02-local-model-benchmarks.ipynb`.
2. Choose 3 models you can realistically run.

Suggested mix:

- one small instruct model
- one code-capable model
- one slightly larger reasoning-capable model

3. Write down why you chose each model before testing.
4. Build a 10-prompt benchmark set.

Use 10 prompts total:

- 3 reasoning prompts
- 3 coding prompts
- 2 summarization prompts
- 2 tool-usage or structured-output prompts

5. Run the same prompt set on all 3 models.
6. Record for each model:

- memory usage
- latency
- tokens per second if available
- response quality on your prompts
- obvious failure modes

7. Score them roughly.
   You do not need a perfect metric. A simple 1 to 5 rating per prompt category is enough for today.
8. Write a short comparison:

- which model feels strongest overall
- which model is best value for your hardware
- which model you would fine-tune first

9. Draft an X post with:
   - the 3 models tested
   - one surprise
   - one simple table or screenshot from the notebook

## Checkpoints

- Can you explain why one model felt stronger even if it was slower?
- Can you explain why the fastest model may not be the best future tuning target?
- Did you compare them on the same prompts rather than changing prompts mid-way?

## Common Mistakes

- Comparing models on different prompts.
- Trusting one lucky response too much.
- Ignoring latency and VRAM because the answer looked good.
- Choosing only hype-driven models instead of models that fit your machine.

## Artifact To Produce

Create:

- a notebook: `day-02-local-model-benchmarks.ipynb`
- a benchmark note with:
  - prompt set
  - model names and quantization format
  - hardware notes
  - performance table
  - subjective quality notes
- one X post draft

## Done Means

- you have run at least 3 models locally
- you have a baseline table, not just impressions
- you have picked one candidate model for future tuning

## If You Finish Early

- Add one more model as a stretch comparison.
- Turn one qualitative judgment into a measurable rubric.

## Reflection Prompts

- Did the best-feeling model also have the best latency?
- What quality differences mattered most in practice?
- What surprised you about small models?
