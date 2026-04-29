# High-Level Plan

The root PDFs have a hierarchy:

- Primary roadmap: `single_gpu_agi_arc_milestone_ladder.pdf`
- Companion paper workflow: `agi_paper_implementation_ladder_2026.pdf`

This file is a working summary. If it conflicts with the primary roadmap, follow the primary roadmap. Use the companion PDF for paper-selection and implementation workflow details.

## Goal

Become a strong single-GPU AI builder by implementing paper mechanisms, validating them with measured experiments, integrating useful pieces into ARC-AGI-3 / synthetic skill-acquisition systems, and publishing clear proof-of-work.

The goal is not to claim that one GPU can train frontier AGI. The goal is to build the taste and engineering skill to turn papers into code, measurements, ablations, failure analyses, and coherent systems.

## North Star

This repo should become a public, reproducible lab with:

- a tiny language model stack implemented from scratch;
- eval harnesses for local models and ARC-like environments;
- LoRA, QLoRA, and DPO implementations and runs;
- inference and quantization benchmarks;
- ARC-AGI-3 environment runners, replay analysis, state abstraction, planners, and world-model experiments;
- paper implementation reports with metrics and decisions;
- model cards, dataset cards, raw logs, plots, and public writeups.

## Strategy

The lab loop is:

```text
paper -> implementation -> toy validation -> ARC/synthetic integration -> ablation -> public artifact
```

Do not implement a paper because it is trendy. Implement it because it advances one of the lab capabilities:

- neural fundamentals;
- efficient training;
- evaluation;
- inference;
- search and planning;
- exploration;
- world modeling;
- object-centric reasoning;
- program synthesis;
- test-time adaptation;
- agent memory and tool use.

## What From Scratch Means

Implement from scratch:

- model modules;
- losses;
- optimizers where useful;
- search algorithms;
- transition models;
- replay buffers;
- action ranking;
- evaluation loops;
- toy environments;
- ablation scripts.

Do not waste time implementing from scratch:

- CUDA kernels;
- production tokenizer infrastructure;
- distributed training frameworks;
- logging frameworks;
- production inference servers.

Use PyTorch. Use Hugging Face, PEFT, TRL, vLLM, SGLang, and related tools after the core mechanism has been manually implemented once.

## Current First Project

**Project 001: Tiny LLaMA-style LM plus eval harness plus ARC smoke test**

This is the first real project because it creates reusable infrastructure for the rest of the roadmap.

Build:

1. RMSNorm.
2. RoPE.
3. Causal attention.
4. LLaMA-style transformer block.
5. Tiny GPT model.
6. BPE or SentencePiece wrapper.
7. Training loop.
8. Checkpointing.
9. Eval script.
10. ARC-AGI-3 random/systematic baseline runner.

Minimum acceptance criteria:

- core modules have tests;
- tiny model overfits a tiny batch;
- full training run completes without NaNs;
- eval script runs on a checkpoint;
- generation script works;
- ARC baseline saves replay/logs;
- one-command reproduction is documented;
- one technical writeup and one public thread are published.

## Milestone Gates

Use capability gates, not calendar promises.

1. Lab OS and AGI compass.
2. Neural network fundamentals.
3. Transformer mechanics.
4. Small LMs from scratch.
5. Evaluation spine.
6. Single-GPU post-training.
7. Preference optimization.
8. Inference and serving.
9. Training systems and dynamics.
10. Search, planning, and agents.
11. World models and exploration.
12. ARC abstraction and DSLs.
13. ARC-AGI-3 competitive system.
14. Public research lab and capstone.

## Project Acceptance Standard

A project is accepted only if it has:

- a falsifiable hypothesis;
- a baseline;
- a metric;
- config, seed, commit, and hardware details;
- logs and raw outputs where practical;
- failure analysis with examples;
- a public artifact;
- a stop condition or kill criterion.

## Public Proof-Of-Work

Every serious milestone should produce at least one artifact:

- GitHub code;
- short README;
- chart;
- failure analysis;
- X thread;
- demo video;
- notebook;
- technical blog post.

The voice should be useful, reproducible, technical, and honest. Avoid grand predictions, cherry-picked generations, benchmark screenshots without configs, and fine-tune announcements without before/after evals.
