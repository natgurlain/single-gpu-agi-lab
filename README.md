# Single-GPU AGI Lab

This repository is a practical, single-GPU research lab for learning modern AI systems by turning papers into working code, measured experiments, failure analyses, and public artifacts.

The root PDFs have a hierarchy:

- Primary roadmap: [single_gpu_agi_arc_milestone_ladder.pdf](single_gpu_agi_arc_milestone_ladder.pdf)
- Companion paper workflow: [agi_paper_implementation_ladder_2026.pdf](agi_paper_implementation_ladder_2026.pdf)

All Markdown files are working notes derived from those PDFs. If a Markdown file conflicts with the primary roadmap, follow the primary roadmap. Use the companion PDF for paper selection and implementation workflow details.

## Operating Thesis

The goal is not to train a frontier foundation model on one GPU. The goal is to become a builder-researcher who can:

- implement core mechanisms from papers;
- validate them on toy or synthetic environments;
- integrate useful mechanisms into a coherent ARC-AGI-3 / skill-acquisition agent stack;
- measure results with baselines, metrics, configs, logs, and failure analysis;
- publish useful proof-of-work.

On one 24 GB GPU, the advantage is tight feedback loops, honest evaluation, and coherent compounding work.

## Start Here

- [Roadmap](ROADMAP.md)
- [High-Level Plan](docs/high-level-plan.md)
- [Core Resources](docs/core-resources.md)
- [Notebooks Overview](notebooks/README.md)
- [X Post Template](templates/x-post-template.md)
- [Paper Implementation Card](templates/paper-implementation-card.md)

The current first real project is:

**Project 001: Tiny LLaMA-style LM plus eval harness plus ARC smoke test**

It builds the reusable spine of the lab:

- RMSNorm;
- RoPE;
- causal attention;
- LLaMA-style transformer block;
- tiny GPT model;
- tokenizer wrapper;
- training loop;
- checkpointing;
- eval script;
- ARC-AGI-3 random/systematic baseline runner.

## Repository Status

This repo is milestone-driven, not time-driven. Older time-boxed onboarding files have been removed so the project follows the PDF roadmap directly.

The canonical priority order starts with the implementation spine:

1. Adam and AdamW from scratch.
2. Causal attention from scratch.
3. RMSNorm and RoPE.
4. BPE tokenizer from scratch.
5. nanoGPT-style tiny LM training.
6. Eval harness v0.
7. ARC-AGI-3 SDK/environment baseline.
8. ARC replay and state abstraction.
9. LoRA from scratch.
10. QLoRA SFT.

Use the primary roadmap PDF for the full priority list.

## Implementation Loop

Every serious paper or mechanism should follow this loop:

1. Choose it because it advances a capability.
2. Define the minimal implementation.
3. Validate on a toy environment.
4. Integrate, archive, or reject.
5. Publish a public artifact.

A paper implementation only counts when it produces working code, a measured result, a short explanation, and a clear decision.

## Acceptance Standard

A project is accepted only if it has:

- a falsifiable hypothesis;
- a baseline;
- a metric;
- config, seed, commit, and hardware details;
- logs and raw outputs where practical;
- failure analysis with examples;
- a public artifact;
- a stop condition or kill criterion.

## Recommended Future Structure

The PDFs recommend growing this repo into a single monorepo with:

- `pyproject.toml`
- `configs/`
- `src/lab/`
- `papers/`
- `experiments/`
- `results/`
- `datasets/`
- `model_cards/`
- `docs/blog/`
- `docs/x_drafts/`
- `scripts/`
- `tests/`

Do not split the repo early. The lab should compound in one place until the boundaries are obvious.
