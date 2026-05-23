# Learning Loop

Status: v0 operating contract.

This lab is optimized for fast durable learning, not passive content consumption. The standard loop
is:

```text
read -> predict -> implement -> test -> explain -> exam -> revise -> publish
```

The teacher's job is to keep the bar high. The learner's job is to do the implementation,
retrieval, design, debugging, and explanation work rather than only watching the agent produce
artifacts. By default, Codex creates minimal setup, templates, review prompts, and tests; the user
implements the core mechanism.

## Core Principles

1. Retrieval beats rereading.
   After learning a concept, you will be asked to recall it without notes, derive it, debug it, or
   explain it. Exams are not just assessment; they are part of learning.

2. Deliberate practice beats vague effort.
   Each session needs a target skill, a task just beyond comfort, immediate feedback, and a clear
   standard for passing.

3. Spacing beats cramming.
   Important concepts return after delays. A milestone is not done just because it worked once.

4. Interleaving beats isolated drills.
   Once basics are introduced, tasks should mix concepts: optimizer math plus tests, attention masks
   plus shapes, ARC replay logs plus failure analysis.

5. Projects beat lectures, but only with exams.
   We learn by building, then we prove learning by answering questions and fixing unseen failures.

6. Public artifacts force clarity.
   Every serious unit should leave a short note, test, result, or writeup that future-you can trust.

## Session Format

Each serious session should follow this structure:

1. Objective.
   Name the exact skill or milestone checkbox.

2. Primer.
   I give a short explanation, key formulas, source links, and what to ignore for now.

3. Prediction.
   Before implementation, you answer: what should happen, what can fail, and how we will know?

4. Build.
   You implement the smallest useful artifact. I may create the scaffold, define the tests, review,
   and give hints, but I should not take over the core implementation unless you explicitly ask.

5. Test.
   We run unit tests, smoke tests, or a tiny experiment.

6. Oral exam.
   I ask questions. You answer from memory. I grade hard.

7. Debug exam.
   I introduce or describe a failure. You diagnose it.

8. Artifact.
   We update notes, results, checklist items, and next actions.

## Exam Types

- Recall: define a concept without notes.
- Derivation: derive an update rule, shape transformation, or metric.
- Trace: step through code or tensor shapes by hand.
- Debug: explain why a test failed or why a run produced nonsense.
- Design: choose the minimal experiment and justify the metric.
- Transfer: apply the idea to ARC-AGI-3 or another unseen setting.
- Falsification: name what result would make us reject the approach.

## Grading Standard

Answers are graded as:

- Pass: correct, precise, and transferable.
- Borderline: mostly right but missing a key condition, edge case, or failure mode.
- Fail: vague, memorized, or unable to guide implementation/debugging.

Passing means you can use the idea under pressure. It does not mean you saw the code run once.

## Milestone Advancement Rule

A checkbox is complete only when three things exist:

1. Evidence in the repo.
2. A passing test, run, note, or result appropriate to the item.
3. The learner can explain the concept and its failure modes.

## Implementation Ownership

For learning milestones, the default ownership split is:

- User: core implementation, first debugging attempt, closed-book explanation.
- Codex: minimal file scaffold, templates, test skeletons, source curation, review, hints, grading,
  and adversarial debugging prompts.

If the user says "implement it for me," Codex may write code. Otherwise, preserve the learning
benefit by scaffolding instead of solving.

Use `templates/implementation-session-template.md` for each new mechanism.

## Agent Roles We Can Use

When useful, we can spin up parallel agents:

- Research scout: gather primary sources and summarize only what affects the current milestone.
- Examiner: generate hard questions and grade answers against a rubric.
- Code reviewer: attack the implementation for bugs, missing tests, and false claims.
- Experiment auditor: check whether metrics, seeds, configs, and logs support the conclusion.

Agents are assistants, not substitutes. They widen feedback and catch blind spots; they do not
replace your retrieval practice.

## Default Weekly Rhythm

For each substantial topic:

1. Day 1: learn and implement the smallest version.
2. Day 2: recall exam and debugging drill.
3. Day 3-4: apply to a slightly different task.
4. Day 7: spaced review and mini oral exam.
5. Day 14+: revisit through a harder milestone.

## Current First Loop

Next topic: Adam and AdamW from scratch.

Pass standard:

- You can derive Adam's first and second moment updates.
- You can explain bias correction.
- You can explain why AdamW decouples weight decay.
- The implementation matches PyTorch on controlled tensors within tolerance.
- A tiny optimization task shows a sensible loss curve.
- The experiment note records config, seed, metric, failure notes, and decision.

## Learning Science Sources

- Retrieval practice/testing effect: https://pmc.ncbi.nlm.nih.gov/articles/PMC3983480/
- Applied retrieval-practice review: https://link.springer.com/article/10.1007/s10648-021-09595-9
- Spacing and learning strategies overview: https://pmc.ncbi.nlm.nih.gov/articles/PMC5780548/
- Spacing over longer timescales review: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00962/full
- Interleaving review: https://link.springer.com/article/10.1007/s10648-021-09613-w
- Deliberate practice evidence discussion: https://pmc.ncbi.nlm.nih.gov/articles/PMC7461852/
