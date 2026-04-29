# Notebooks

This directory is the notebook execution layer for the lab. The primary roadmap PDF controls roadmap order and acceptance criteria; the companion paper-workflow PDF controls paper implementation workflow details.

Use notebooks for exploration, notes, quick experiments, visual checks, and public artifact drafts. Move reusable code into `src/lab/` once the project structure exists.

## Current Role

Notebooks should be organized by milestone, project, paper, or experiment. Do not create time-boxed notebooks unless a PDF roadmap explicitly adds that structure.

The canonical first real project is Project 001 from the PDFs:

**Tiny LLaMA-style LM plus eval harness plus ARC smoke test**

## Notebook Rules

Every serious notebook should include:

1. Hypothesis.
2. Baseline.
3. Metric.
4. Config and seed.
5. Hardware notes.
6. Result table or logs.
7. Failure analysis.
8. Decision: integrate, archive, or reject.
9. Public artifact draft.

## Structure

- `templates/`
  - reusable notebook templates

Project notebooks should mirror the experiment IDs from the roadmap, for example:

- `experiments/exp_0001_adamw_from_scratch/`
- `experiments/exp_0002_tiny_gpt/`
- `experiments/exp_0003_arc_baseline/`
