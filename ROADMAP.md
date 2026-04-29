# Roadmap

This file is the working Markdown index for the PDF roadmap hierarchy:

- Primary roadmap: `single_gpu_agi_arc_milestone_ladder.pdf`
- Companion paper workflow: `agi_paper_implementation_ladder_2026.pdf`

If this file conflicts with the primary roadmap, follow the primary roadmap. Use the companion PDF for paper-selection and implementation-card workflow details.

## Strategy

Build a public, reproducible, single-GPU AGI systems lab by implementing a curated sequence of AGI-relevant papers from scratch, validating useful mechanisms in toy or synthetic environments, integrating the best ones into ARC-AGI-3 / skill-acquisition agents, and publishing every meaningful result.

Avoid two traps:

- leaderboard-only hacking that improves scores but teaches little;
- paper tourism that creates disconnected notebooks without a coherent system.

The winning loop is:

```text
paper -> implementation -> toy validation -> ARC/synthetic integration -> ablation -> public artifact
```

## Milestone Ladder

Advance by capability gates, not by calendar.

| Milestone | Name | Gate |
| --- | --- | --- |
| 0 | Lab OS and AGI compass | Reproducible repo, toolchain, ARC runner, and personal research thesis. |
| 1 | Neural network fundamentals | Autograd, optimizers, and training loops can be debugged from first principles. |
| 2 | Transformer mechanics | Decoder-only transformer implemented and tested from scratch. |
| 3 | Small LMs from scratch | Small language model trained, evaluated, and documented. |
| 4 | Evaluation spine | Local model and ARC baselines measured with fixed configs. |
| 5 | Single-GPU post-training | LoRA, QLoRA, and SFT run with before/after evals. |
| 6 | Preference optimization | DPO/preference pipeline implemented and measured. |
| 7 | Inference and serving | Local serving and quantization benchmark published. |
| 8 | Training systems and dynamics | VRAM model, checkpointing, scaling, and optimizer experiments. |
| 9 | Search, planning, and agents | Search/tool-use agents evaluated beyond demos. |
| 10 | World models and exploration | Novelty, transition modeling, and goal inference tested in environments. |
| 11 | ARC abstraction and DSLs | Object/state abstraction and program search integrated. |
| 12 | ARC-AGI-3 competitive system | Self-contained agent stack with replays, metrics, and packaging. |
| 13 | Public research lab | Reproduction suite, model cards, benchmarks, and public proof-of-work. |

## Project 001

**Tiny LLaMA-style LM plus eval harness plus ARC smoke test**

Goal: create the reusable backbone of the lab: transformer implementation, training loop, logging, evaluation, and ARC environment runner.

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

Minimum language-model metrics:

- train loss;
- validation loss;
- perplexity;
- tokens/sec;
- peak VRAM;
- sample generations;
- overfit-tiny-batch result.

Minimum ARC metrics:

- games attempted;
- score;
- steps;
- unique states;
- action histogram;
- replay saved.

Done means:

- all core modules have tests;
- tiny model overfits a tiny batch;
- full training run completes without NaNs;
- eval script runs on a checkpoint;
- generation script works;
- ARC baseline runs and saves replay/logs;
- README has one-command reproduction;
- one technical writeup and one public thread are published.

## Priority Order

Tier 1 must be implemented first:

1. Adam and AdamW from scratch.
2. Causal attention from scratch.
3. RMSNorm and RoPE.
4. BPE tokenizer from scratch.
5. nanoGPT-style tiny LM training.
6. FlashAttention/PyTorch SDPA benchmark.
7. Tiny scaling-law sweep.
8. Eval harness v0.
9. ARC-AGI-3 SDK/environment baseline.
10. ARC replay and state abstraction.
11. LoRA from scratch.
12. QLoRA SFT.
13. DPO loss from scratch.
14. DPO local model run.
15. CoT and self-consistency harness.
16. ReAct agent loop.
17. Tree of Thoughts or explicit planner.
18. ARC world model and planner.
19. vLLM/SGLang inference benchmark.
20. Quantization benchmark.

Tier 2 is strongly recommended after the spine exists:

- STaR-style rationale self-training;
- Reflexion-style memory loop;
- SWE-agent-style interface design;
- activation checkpointing and VRAM budget calculator;
- muP-style hyperparameter transfer;
- RND exploration;
- tiny world model;
- DSL/program search on ARC-mini tasks;
- TransformerLens analysis of the tiny model;
- RAG and retrieval evals for tool-use systems.

Tier 3 is optional or later:

- full ZeRO/Megatron implementation;
- CUDA kernel writing;
- full Dreamer reproduction;
- full DeepSeek-R1 reproduction;
- full large-scale multimodal training;
- production-grade inference server implementation.

## Paper Implementation Card

Use this for every serious paper. A reusable copy lives at [templates/paper-implementation-card.md](templates/paper-implementation-card.md).

```markdown
# Paper implementation card

Paper:
URL:
Category:
Core mechanism:
Why it matters for model building:
Why it matters for ARC / skill acquisition:
Implementation level: L1 / L2 / L3 / L4
Minimal implementation:
Dataset / environment:
Baseline:
Metric:
Expected failure:
Kill criterion:
Integration target:
Public artifact:
Decision: integrate / archive / reject
```

The most important fields are `Metric`, `Kill criterion`, and `Integration target`.

## Kill Criteria

Stop or downgrade a paper if:

- it requires compute far beyond one GPU;
- the core mechanism cannot be isolated in a toy setting;
- it depends on private data or impossible replication details;
- it has no testable metric;
- it does not connect to the lab after the educational implementation;
- it keeps expanding in scope without producing a result.

Do not keep an ARC module if:

- it improves only public games and fails custom holdout;
- it increases no-op or invalid action rate without increasing solved levels;
- it is too slow for evaluation;
- it cannot be debugged from traces;
- it requires hosted APIs or internet access;
- it branches on public environment IDs.
