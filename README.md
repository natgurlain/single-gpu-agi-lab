# Single-GPU AGI Lab

This repository is a practical learning plan for building strong intuition around modern AI systems on a single consumer GPU.

The focus is not on pretending a single machine can reproduce frontier pretraining. The focus is on learning the parts of the stack that are both technically serious and feasible:

- local inference and benchmarking
- tokenization, datasets, and data quality
- supervised fine-tuning with LoRA / QLoRA
- preference tuning and small-scale reinforcement learning
- evaluation, ablations, and reproducible experiments
- building in public with concrete artifacts

The workflow is intentionally:

- realistic for one person learning part-time
- notebook-first using Jupyter
- daily build-in-public on X
- tutor-style rather than vague or motivational

## Start Here

- [High-Level Plan](docs/high-level-plan.md)
- [Core Resources](docs/core-resources.md)
- [Notebooks Overview](notebooks/README.md)
- [X Post Template](templates/x-post-template.md)
- Week 1
  - [Day 1](docs/week-01/day-01.md)
  - [Day 2](docs/week-01/day-02.md)
  - [Day 3](docs/week-01/day-03.md)
  - [Day 4](docs/week-01/day-04.md)
  - [Day 5](docs/week-01/day-05.md)
  - [Day 6](docs/week-01/day-06.md)
  - [Day 7](docs/week-01/day-07.md)

## How To Use This Repo

Each day file follows the same pattern:

1. What the day is trying to teach.
2. What to learn before doing anything.
3. What to read before starting the day.
4. A step-by-step agenda with time boxes.
5. Checkpoints to verify understanding.
6. Common mistakes to avoid.
7. What artifact to produce.
8. What "done" means.

Do not rush through the week. The point is to build working mental models and a repeatable research loop.

Default execution format:

- use a Jupyter notebook for the day's hands-on work
- keep short notes in Markdown
- end the day with one X post or thread draft

Default study rule:

- if a day looks too large, finish the understanding and notes first, then scale down the hands-on work
- do not pretend to have understood a paper you only skimmed
- do not move on without writing your own explanation
- do not leave a concept at the level of a label; attach it to a concrete resource

Starter notebooks:

- [Day 1 Notebook](notebooks/week-01/day-01-lab-map.ipynb)
- [Day 2 Notebook](notebooks/week-01/day-02-local-model-benchmarks.ipynb)
- [Day 3 Notebook](notebooks/week-01/day-03-data-and-tokenization.ipynb)
- [Day 4 Notebook](notebooks/week-01/day-04-first-qlora-plan.ipynb)
- [Day 5 Notebook](notebooks/week-01/day-05-eval-baseline.ipynb)
- [Day 6 Notebook](notebooks/week-01/day-06-preference-tuning-notes.ipynb)
- [Day 7 Notebook](notebooks/week-01/day-07-week-review.ipynb)

## Principles

- Stay close to open tools and open papers.
- Prefer reproductions over vague theory.
- Prefer 1 clean experiment over 10 half-finished ones.
- Track results, failures, timings, and memory use.
- Publish artifacts when possible: notes, configs, charts, benchmarks, adapters, eval tables.
- Post daily, even if the post is small. Consistency beats occasional giant threads.
- Use notebooks as the main working surface for experiments and exploration.
- Learn actively: define, compare, test, summarize, then publish.
- Write in your own words before copying other people's framing.

## Recommended Stack

- Model hub and training ecosystem: Hugging Face
- Inference: vLLM, llama.cpp, Ollama
- Fine-tuning: TRL, PEFT, Unsloth, Axolotl
- Evaluation: lm-eval-harness, custom task evals
- Experiment tracking: plain Markdown first, W&B later if needed
- Notebook environment: JupyterLab or VS Code notebooks

## Constraint

This plan assumes one NVIDIA GPU in the rough class of an RTX 3090 Ti with 24 GB VRAM. That is enough for serious learning and useful outputs, but it changes the strategy:

- do not start by training base models from scratch at useful scale
- do start with post-training and small-model experiments
- do treat data quality and eval quality as first-class work

## Output Expectation

By the end of the first week, you should have:

- a working local model stack
- a reading and notes habit
- baseline inference measurements
- a first tiny dataset pipeline
- a clear understanding of LoRA / QLoRA / DPO / GRPO roles
- at least one public-quality writeup idea for X
- a habit of daily technical posting with concrete artifacts
