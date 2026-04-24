# High-Level Plan

## Goal

Build real capability in modern AI systems on a single GPU by moving from usage to measurement, then to training, then to reproduction, then to original experiments.

## North Star

Over time, this lab should become a place where you can:

- run strong open models locally
- fine-tune and evaluate them reliably
- reproduce selected research papers at small scale
- publish useful artifacts and practical writeups
- develop your own taste in data, evals, and training recipes
- post consistently on X in a way that attracts serious builders

## What Not To Do

- Do not aim to pretrain a frontier base model from scratch.
- Do not chase every new paper.
- Do not confuse "using AI tools" with understanding model behavior.
- Do not spend weeks on infrastructure before running simple baselines.

## Phases

## Phase 1: Foundations And Local Model Literacy

Duration: 2 to 4 weeks

Main outcomes:

- understand model families, tokenizer basics, checkpoints, quantization, context length, and inference tradeoffs
- run several open models locally and compare them
- learn how VRAM, latency, and quality interact

Focus areas:

- vLLM
- transformers
- quantization
- prompting and structured evaluation

## Phase 2: Data And Post-Training

Duration: 4 to 6 weeks

Main outcomes:

- prepare instruction datasets
- run LoRA / QLoRA fine-tunes
- compare base versus tuned behavior
- understand overfitting, formatting, and task mismatch

Focus areas:

- PEFT
- TRL
- Unsloth or Axolotl
- dataset curation

## Phase 3: Preference Optimization And Small RL

Duration: 3 to 6 weeks

Main outcomes:

- understand SFT versus DPO versus RL-style tuning
- run small DPO experiments
- inspect GRPO style workflows conceptually and then experimentally
- build reward or rule-based evaluation loops

Focus areas:

- DPO
- GRPO
- reward design
- evals and failure analysis

## Phase 4: Tiny Pretraining And Mechanistic Intuition

Duration: 2 to 6 weeks

Main outcomes:

- train a small transformer from scratch
- understand tokenization, curriculum, scaling, and optimization basics
- inspect loss curves and common failure modes

Focus areas:

- tiny transformer training
- small corpora
- optimizer and scheduler choices
- ablations

## Phase 5: Research Reproductions

Duration: ongoing

Main outcomes:

- reproduce a focused set of practical papers
- publish notes, code, charts, and takeaways
- learn to separate important ideas from hype

Priority papers and lines of work:

- QLoRA
- DoRA
- DPO
- DeepSeekMath / GRPO lineage
- Open-R1 style reproductions

## Phase 6: Build In Public

Duration: ongoing

Main outcomes:

- develop a recognizable niche
- accumulate trust through practical outputs
- attract the right technical audience

Default content style:

- daily short post with one concrete takeaway
- weekly thread with a benchmark, notebook result, or reproduction summary
- always include specifics: model, tool, constraint, failure, or metric

Good niches for this lab:

- single-GPU reproductions
- local inference and quantization benchmarks
- practical post-training notes
- small-model reasoning experiments

## Cadence

Use this weekly rhythm:

1. Read 1 core source at a realistic depth.
2. Run 1 small notebook-based experiment or benchmark.
3. Record metrics and failures.
4. Post 1 concrete update on X.
5. Decide the next experiment from evidence, not hype.

## Success Criteria

You are on track if, after a few months, you can do these without guessing:

- choose a model that fits your hardware and task
- explain when to use LoRA, QLoRA, DPO, or small RL
- build a dataset for a narrow task
- run an eval and interpret the result
- reproduce at least one paper at reduced scale
- write a clear technical thread or post with numbers and lessons
