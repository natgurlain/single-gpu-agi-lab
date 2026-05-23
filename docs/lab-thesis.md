# Lab Thesis

Status: v0 draft for Milestone 0.

This lab exists to build practical research skill under a hard constraint: one local GPU, public
artifacts, and no hand-wavy claims. The goal is not to train a frontier model. The goal is to
become the kind of builder who can read a paper, isolate the mechanism, implement the useful core,
measure it honestly, and decide whether it belongs in a coherent agent stack.

## Thesis

The best one-GPU path toward AGI-relevant competence is to study skill-acquisition efficiency:
how quickly a system can adapt to a novel problem using limited experience, reusable priors,
search, memory, abstraction, world models, and self-evaluation.

ARC-AGI-3 is the north-star environment because it turns that idea into an interactive test. Static
benchmarks often reward memorized patterns, broad pretraining, or final-answer accuracy. ARC-AGI-3
asks a harder question: can an agent enter a new environment, discover what matters, infer the
goal, plan actions, remember what it learned, and improve before wasting too many moves?

That makes it a useful forcing function for this lab. Every mechanism should eventually answer at
least one practical question:

- Does it help the agent explore more productively?
- Does it help represent state, objects, dynamics, or goals?
- Does it reduce actions needed to solve a new environment?
- Does it improve reproducible model training or evaluation discipline?
- Does it fail in an instructive way that narrows the search space?

## Why One GPU

The one-GPU constraint is not a weakness to hide. It is a pressure that forces good taste.

Large-scale training can hide confusion behind scale. A small lab has to be sharper. It needs small
experiments, clear baselines, tight eval loops, and enough instrumentation to know why a run failed.
This means the lab should value mechanisms that can be inspected:

- optimizer updates that can be compared against known references;
- transformer components with shape, mask, gradient, and determinism tests;
- toy models that overfit tiny batches before larger runs are trusted;
- ARC agents that save replays, action logs, state hashes, and failure examples;
- benchmarks that record config, seed, hardware, commit, and raw outputs.

The constraint also separates learning from performance theater. The lab should not chase a
leaderboard number without a reusable lesson, and it should not implement papers as isolated
notebooks that never connect back to the system.

## What Counts As Progress

Progress is not "read a paper" or "ran a model." Progress is a completed loop:

```text
paper -> minimal implementation -> controlled validation -> integration or rejection -> artifact
```

A result counts when it has a falsifiable hypothesis, a baseline, a metric, logs or raw outputs,
failure analysis, and a decision. "This did not work" is progress if it teaches something and is
recorded clearly enough to avoid repeating the mistake.

## Research Compass

This lab should bias toward mechanisms that compound:

- Neural fundamentals, so training failures are debuggable from first principles.
- Transformer mechanics, so small language models are not black boxes.
- Evaluation infrastructure, so every claim has a fixed config and baseline.
- Search and planning, so agents can reason over actions rather than react greedily.
- Exploration and memory, so agents can use experience gathered inside an environment.
- Object-centric abstraction and DSLs, so ARC-like structure can be represented compactly.
- World models, so action choices can be tested against predicted consequences.

The long-term target is an ARC-AGI-3 agent stack that can run offline, save replays, report metrics,
and support ablations. The public artifact should be a trail of code, reports, model cards, dataset
cards, logs, and honest writeups.

## Personal Operating Rules

1. Prefer measured mechanisms over vibes.
2. Prefer small reproducible experiments over dramatic demos.
3. Treat failures as data, but only if they are written down.
4. Use libraries for infrastructure after implementing the core mechanism once.
5. Do not optimize public games in a way that cannot survive custom holdouts.
6. Advance milestones only when the repo contains evidence.

## Current Milestone 0 Decision

Milestone 0 defines the lab direction: build a reproducible single-GPU research workspace aimed at
skill-acquisition efficiency under novelty. The immediate next technical work should be Milestone 1
fundamentals and Project 001 infrastructure, starting with Adam/AdamW, causal attention, RMSNorm,
RoPE, and the first tiny training/eval loop.

