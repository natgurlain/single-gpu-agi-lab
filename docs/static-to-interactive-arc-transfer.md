# Static ARC To Interactive ARC-AGI-3 Transfer

Status: v0 transfer table for Milestone 0.

Static ARC work remains useful, but ARC-AGI-3 changes the shape of the problem. Static ARC asks for
an output grid after seeing examples. ARC-AGI-3 asks the agent to discover the rules and goal
through interaction.

The transfer question for this lab is: which static ARC mechanisms become useful agent components?

| Static ARC method | What it solves in static ARC | Interactive ARC-AGI-3 analogue | Lab implementation target | Main risk |
| --- | --- | --- | --- | --- |
| Connected components | Finds objects and regions in grids | State object extraction from observations | `src/lab/arc_agi3/abstractions.py` object parser | Object definitions may change across games |
| Color histograms | Summarizes grid-level transformations | Compact state features and change detection | State summaries in replay logs | Counts can miss causal structure |
| Bounding boxes | Localizes objects | Track entities across time | Entity tracker over observations | Moving/hidden objects break simple matching |
| Difference masks | Finds input-output changes | Detects action effects between states | Transition-difference analyzer | Delayed rewards may obscure cause |
| DSL/program search | Generates candidate grid transformations | Generates candidate action programs/macros | Tiny action DSL and macro search | Search can explode without good pruning |
| Test-time adaptation | Learns from task-specific examples | Learns from within-environment experience | Episode memory and online hypothesis updates | Can overfit one episode and forget generality |
| Verifier loops | Rejects wrong candidate outputs | Scores candidate action plans using traces | Replay-based plan evaluator | Weak verifier may reward shortcuts |
| Synthetic data | Creates more transformation examples | Creates custom games and perturbations | Holdout environment suite | Synthetic tasks may miss real game difficulty |
| Ensembling | Combines different solvers | Meta-controller chooses explorer/planner/policy | Policy ensemble with action-budget accounting | Ensemble cost may increase action waste |
| Recursive refinement | Improves candidate answers | Improves action plans after feedback | Plan-reflect-replan loop | Reflection without metrics becomes narration |

## What Changes In ARC-AGI-3

Static ARC allows the solver to inspect examples before producing one answer. ARC-AGI-3 withholds
the goal and makes the agent spend actions to learn. This shifts the main bottlenecks:

- From final answer generation to exploration.
- From grid transformation to state transition modeling.
- From checking one output to evaluating action sequences.
- From example-based inference to experience-based belief updates.
- From solve rate alone to solve rate plus action efficiency.

## First Transfer Targets

For Project 001 and early ARC work, transfer should stay modest:

1. Save every observation-action-next-observation transition.
2. Hash states and count unique states.
3. Build simple action histograms and no-op detectors.
4. Add connected-component summaries for grid-like observations when available.
5. Compare random, action-cycling, and novelty-seeking explorers.

These are not enough for competitive performance, but they create the replay/debugging substrate the
later roadmap needs.

## Acceptance Rule

A static ARC idea counts as transferred only when it becomes an interactive component with:

- a clear metric;
- replay evidence;
- at least one baseline comparison;
- a failure note;
- a decision to integrate, archive, or reject.

