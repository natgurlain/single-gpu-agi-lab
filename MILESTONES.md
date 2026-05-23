# Milestone Checklist

This checklist merges the primary roadmap PDF and the companion paper-workflow PDF.

- Primary roadmap: `single_gpu_agi_arc_milestone_ladder.pdf`
- Companion paper workflow: `agi_paper_implementation_ladder_2026.pdf`

Use this file as the operational progress tracker. Check a milestone only when its acceptance
evidence exists in the repo: code, configs, metrics, logs, notes, and a clear decision.

## Global Acceptance Rules

Every serious project or paper implementation needs:

- [ ] Falsifiable hypothesis.
- [ ] Baseline.
- [ ] Metric.
- [ ] Config, seed, commit, and hardware details.
- [ ] Logs or raw outputs where practical.
- [ ] Failure analysis with examples.
- [ ] Public artifact draft or published artifact.
- [ ] Stop condition or kill criterion.
- [ ] Decision: integrate, archive, or reject.

## Paper Implementation Workflow

Apply this loop inside every milestone that includes a paper or mechanism:

- [ ] Choose the paper because it advances a capability.
- [ ] Define the minimal implementation.
- [ ] Validate on a toy environment or controlled baseline.
- [ ] Integrate into the lab, archive as educational, or reject with a written reason.
- [ ] Publish or draft a public artifact.

## Milestone 0: Lab OS And AGI Compass

Gate: reproducible repo, toolchain, ARC runner direction, and personal research thesis.

- [x] Primary roadmap and companion paper workflow are committed.
- [x] Monorepo structure exists.
- [x] `pyproject.toml` exists.
- [x] Basic package import works.
- [x] Smoke test script exists.
- [x] Lab thesis is drafted.
- [x] ARC-AGI-3 constraints and scoring are summarized.
- [x] Static ARC to interactive ARC-AGI-3 transfer table exists.
- [x] Paper card for `On the Measure of Intelligence` exists.
- [x] Milestone 0 accepted.

## Milestone 1: Neural Network Fundamentals From Scratch

Gate: autograd, optimizers, initialization, and training loops can be debugged from first principles.

- [ ] Adam implemented from scratch.
- [ ] AdamW implemented from scratch.
- [ ] Xavier/Kaiming initialization notes or tests exist.
- [ ] Tiny MLP or controlled optimization task exists.
- [ ] Residual block sanity test exists.
- [ ] Tiny training loop exists.
- [ ] Overfit-tiny-batch test passes.
- [ ] Loss curves and failure notes are recorded.
- [ ] `exp_0001_adamw_from_scratch` has results.
- [ ] Milestone 1 accepted.

## Milestone 2: Transformer Mechanics

Gate: decoder-only transformer components are implemented and tested from scratch.

- [ ] Causal attention implemented from scratch.
- [ ] Attention mask correctness tests pass.
- [ ] RMSNorm implemented and tested.
- [ ] RoPE implemented and tested.
- [ ] LLaMA-style transformer block implemented.
- [ ] Naive attention compared against PyTorch SDPA.
- [ ] Shape, dtype, gradient, and determinism tests exist.
- [ ] Paper card for `Attention Is All You Need` exists.
- [ ] Milestone 2 accepted.

## Milestone 3: Small Language Models From Scratch

Gate: small language model is trained, evaluated, and documented.

- [ ] BPE or SentencePiece wrapper exists.
- [ ] Tiny GPT model exists.
- [ ] Training loop supports checkpointing.
- [ ] Full tiny training run completes without NaNs.
- [ ] Eval script runs on a checkpoint.
- [ ] Generation script works.
- [ ] Train loss, validation loss, and perplexity are logged.
- [ ] Tokens/sec and peak VRAM are logged.
- [ ] Sample generations and failure examples are saved.
- [ ] `exp_0002_tiny_gpt` has results.
- [ ] Milestone 3 accepted.

## Milestone 4: Evaluation Spine

Gate: local model and ARC baselines are measured with fixed configs.

- [ ] Eval harness v0 exists.
- [ ] Fixed eval configs exist.
- [ ] Seeds are recorded.
- [ ] Baseline model scores are recorded.
- [ ] Failure taxonomy exists.
- [ ] Raw outputs or representative examples are saved.
- [ ] ARC smoke-test metric plan exists.
- [ ] Project 001 language-model metrics are reproducible.
- [ ] Milestone 4 accepted.

## Milestone 5: Single-GPU Post-Training

Gate: LoRA, QLoRA, and SFT are run with before/after evals.

- [ ] LoRA implemented manually on a tiny transformer.
- [ ] LoRA tests verify frozen base weights and trainable adapters.
- [ ] SFT dataset card exists.
- [ ] Baseline eval before tuning exists.
- [ ] QLoRA SFT run completes on local GPU.
- [ ] After-tuning eval exists.
- [ ] Before/after comparison is written.
- [ ] Failure analysis covers overfitting, formatting, and task mismatch.
- [ ] Paper cards for LoRA and QLoRA exist.
- [ ] Milestone 5 accepted.

## Milestone 6: Preference Optimization And Alignment

Gate: DPO or preference pipeline is implemented and measured against SFT.

- [ ] DPO loss implemented from scratch.
- [ ] Tiny preference dataset exists.
- [ ] Preference dataset card exists.
- [ ] SFT baseline exists.
- [ ] DPO local run completes.
- [ ] SFT-vs-DPO comparison exists.
- [ ] Reward/rubric weaknesses are documented.
- [ ] GRPO is explained and scoped before implementation.
- [ ] Paper card for DPO exists.
- [ ] Milestone 6 accepted.

## Milestone 7: Inference, Quantization, And Serving

Gate: local serving and quantization benchmark is published or ready to publish.

- [ ] vLLM benchmark plan exists.
- [ ] SGLang benchmark plan exists.
- [ ] Transformers baseline exists.
- [ ] Quantization benchmark includes at least one quantized format.
- [ ] Latency is logged.
- [ ] Tokens/sec is logged.
- [ ] Peak VRAM is logged.
- [ ] Context length and batch assumptions are recorded.
- [ ] Quality notes or task eval deltas are recorded.
- [ ] Milestone 7 accepted.

## Milestone 8: Training Systems And Dynamics

Gate: VRAM modeling, checkpointing, scaling, and optimizer experiments are understood empirically.

- [ ] VRAM budget calculator exists.
- [ ] Activation checkpointing experiment exists.
- [ ] Resume-from-checkpoint is tested.
- [ ] Tiny scaling-law sweep exists.
- [ ] Optimizer comparison or ablation exists.
- [ ] Tokens/sec, samples/sec, LR, grad norm, and parameter norm are logged.
- [ ] Checkpoint health is validated.
- [ ] Run checklist is documented.
- [ ] Milestone 8 accepted.

## Milestone 9: Search, Planning, And Agent Loops

Gate: search/tool-use agents are evaluated beyond demos.

- [ ] CoT prompting harness exists.
- [ ] Self-consistency harness exists.
- [ ] ReAct-style loop exists on a toy environment.
- [ ] Tree of Thoughts or explicit planner exists.
- [ ] Baseline planner comparison exists.
- [ ] Metrics include score, solve rate, cost, or action count.
- [ ] Reflection or memory loop is tested with an ablation.
- [ ] Failure cases are categorized.
- [ ] Milestone 9 accepted.

## Milestone 10: World Models, Exploration, And Intrinsic Motivation

Gate: novelty, transition modeling, and goal inference are tested in environments.

- [ ] Random explorer exists.
- [ ] Action-cycling explorer exists.
- [ ] Novelty-search explorer exists.
- [ ] RND or equivalent curiosity metric exists.
- [ ] State hashes and transition tables exist.
- [ ] Tiny transition model exists.
- [ ] Goal-hypothesis ranking from score/state changes exists.
- [ ] Metrics include state coverage, reward discovery, and action count.
- [ ] Milestone 10 accepted.

## Milestone 11: ARC Abstraction, Object-Centric Reasoning, And DSLs

Gate: object/state abstraction and program search are integrated into ARC-like work.

- [ ] Connected components implemented.
- [ ] Bounding boxes, color histograms, and topology features exist.
- [ ] Object graph representation exists.
- [ ] Transition-difference analysis exists.
- [ ] Tiny DSL exists.
- [ ] Enumerative search exists on toy ARC-like tasks.
- [ ] Neural-guided search or object-model comparison exists.
- [ ] Abstraction improves a baseline on at least one environment or task family.
- [ ] Milestone 11 accepted.

## Milestone 12: ARC-AGI-3 Competitive System

Gate: self-contained ARC-AGI-3 agent stack has replays, metrics, and packaging.

- [ ] ARC-0 environment harness runs public environments.
- [ ] ARC-0 saves replays, logs, scores, actions, terminal states, and state hashes.
- [ ] ARC-1 random, action-cycling, systematic, novelty, and macro-action explorers exist.
- [ ] ARC-2 state abstraction summarizes what changed after actions.
- [ ] ARC-3 goal inference ranks plausible objectives.
- [ ] ARC-4 planner/search improves score or action count versus exploration alone.
- [ ] ARC-5 world model or transition model improves action selection on held-out episodes.
- [ ] ARC-6 ensemble or meta-controller combines policies.
- [ ] Custom holdout suite exists to reduce public-set overfitting.
- [ ] Final package runs offline with documented hardware budget.
- [ ] Milestone 12 accepted.

## Milestone 13: Public Research Lab And Capstone

Gate: experiments become a coherent public proof-of-work portfolio.

- [ ] At least 10 serious paper implementation reports exist.
- [ ] Tiny LM stack is documented.
- [ ] Fine-tuning pipeline is documented.
- [ ] Eval harness is documented.
- [ ] Inference benchmark is documented.
- [ ] ARC agent lab is documented.
- [ ] Model cards exist for trained models or adapters.
- [ ] Dataset cards exist for curated datasets.
- [ ] Benchmark configs, commands, raw logs, and caveats are included.
- [ ] Public writeups or drafts exist for major milestones.
- [ ] Milestone 13 accepted.

## Project 001: Tiny LLaMA-Style LM Plus Eval Harness Plus ARC Smoke Test

This is the first integrated project across milestones 1-4 and 12.

- [ ] RMSNorm.
- [ ] RoPE.
- [ ] Causal attention.
- [ ] LLaMA-style transformer block.
- [ ] Tiny GPT model.
- [ ] BPE or SentencePiece wrapper.
- [ ] Training loop.
- [ ] Checkpointing.
- [ ] Eval script.
- [ ] ARC-AGI-3 random/systematic baseline runner.
- [ ] All core modules have tests.
- [ ] Tiny model overfits a tiny batch.
- [ ] Full training run completes without NaNs.
- [ ] Eval script runs on a checkpoint.
- [ ] Generation script works.
- [ ] ARC baseline runs and saves replay/logs.
- [ ] One-command reproduction is documented.
- [ ] Technical writeup or public thread is drafted.
- [ ] Project 001 accepted.

## Tier 1 Priority Queue

Use this queue to select the next implementation task.

- [ ] Adam and AdamW from scratch.
- [ ] Causal attention from scratch.
- [ ] RMSNorm and RoPE.
- [ ] BPE tokenizer from scratch.
- [ ] nanoGPT-style tiny LM training.
- [ ] FlashAttention/PyTorch SDPA benchmark.
- [ ] Tiny scaling-law sweep.
- [ ] Eval harness v0.
- [ ] ARC-AGI-3 SDK/environment baseline.
- [ ] ARC replay and state abstraction.
- [ ] LoRA from scratch.
- [ ] QLoRA SFT.
- [ ] DPO loss from scratch.
- [ ] DPO local model run.
- [ ] CoT and self-consistency harness.
- [ ] ReAct agent loop.
- [ ] Tree of Thoughts or explicit planner.
- [ ] ARC world model and planner.
- [ ] vLLM/SGLang inference benchmark.
- [ ] Quantization benchmark.
