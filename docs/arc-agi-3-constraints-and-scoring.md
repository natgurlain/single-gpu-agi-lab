# ARC-AGI-3 Constraints And Scoring

Status: v0 summary for Milestone 0.
Last checked: 2026-05-19.

Primary sources:

- [ARC-AGI-3 official page](https://arcprize.org/arc-agi/3)
- [ARC-AGI-3 scoring methodology](https://docs.arcprize.org/methodology)
- [ARC-AGI Toolkit quickstart](https://docs.arcprize.org/toolkit/overview)
- [ARC-AGI-3 technical paper](https://arxiv.org/abs/2603.24621)

## What ARC-AGI-3 Measures

ARC-AGI-3 is an interactive reasoning benchmark. Unlike static ARC tasks, an agent must act inside
a novel turn-based environment. It has to explore, infer the goal, build an internal model of state
transitions, plan, and adapt from experience.

For this lab, the important target is not "solve final puzzle from examples." It is:

```text
observe -> act -> receive feedback -> update beliefs -> plan better actions
```

The benchmark is designed around:

- novel environments;
- no natural-language task instructions;
- no reliance on external knowledge;
- human-solvable games;
- sparse or delayed feedback;
- efficiency over a sequence of actions.

## Agent Constraints

Practical constraints for our lab:

- The agent should work through the official ARC-AGI toolkit or documented API.
- Local/offline development should be preferred for iteration.
- Online/scorecard mode should be used when official scorecards or shareable replays matter.
- Every run should record the game id, seed, available actions, chosen actions, observations,
  terminal state, scorecard fields where available, and replay path.
- Any agent improvement must be tested against at least one custom or held-out environment before
  being trusted.

Failure modes to watch:

- exploring randomly without extracting reusable state information;
- overfitting to public game ids or game versions;
- inflating action count through retries, loops, or no-ops;
- reporting score without replays or action traces;
- solving early/tutorial levels but failing later levels;
- using hidden assumptions that a first-time human would not need.

## What Counts As An Action

An action is an external interaction that changes or attempts to change the environment state. The
agent's private computation, planning, tool calls, and internal reasoning are not counted as actions
unless they are submitted to the game environment.

This makes action efficiency the scarce resource. Compute can be used for planning, but the plan
must reduce bad moves.

## Scoring Summary

ARC-AGI-3 uses Relative Human Action Efficiency, or RHAE. The score combines:

- completion: how many levels the agent completes;
- efficiency: how many actions it takes compared with first-time human baselines.

For a completed level:

```text
level_score = (human_baseline_actions / ai_actions) ^ 2
```

The human baseline is based on first-time human players. The current methodology uses the upper
median human action count per level, rather than a theoretical best run.

Each level score is capped at 1.15, so an agent can receive limited credit for outperforming the
human baseline but cannot let one shortcut dominate the whole game score.

Game scores use a weighted average across levels, where later levels carry more weight. If an agent
does not complete later levels, the maximum possible game score is capped by that missing progress.

The total score is the average across games.

## Lab Metrics To Record

Even before official scoring integration, every ARC run should save:

- games attempted;
- levels completed;
- total actions;
- score or local proxy score;
- unique state hashes;
- action histogram;
- invalid/no-op action count;
- terminal state;
- replay or recording path;
- failure notes.

## Milestone 0 Decision

ARC-AGI-3 is the lab's agent benchmark because it forces interaction, exploration, goal inference,
world modeling, planning, and efficient adaptation. Milestone 0 does not require a strong agent;
it requires knowing what evidence a future agent must produce.

