# Core Resources

Last verified: 2026-04-28.

The primary roadmap is `single_gpu_agi_arc_milestone_ladder.pdf`. The companion paper workflow is `agi_paper_implementation_ladder_2026.pdf`. This file is a milestone-oriented resource index for implementation work. Prefer primary sources: papers, official docs, official repos, and competition docs.

Use each resource to produce code, a metric, or a decision. Do not collect links for comfort.

## Resource Policy

For each milestone:

1. Read the canonical paper or official spec.
2. Write the mechanism in your own words.
3. Implement the smallest useful version.
4. Test it on a toy case or baseline.
5. Decide: integrate, archive, or reject.

## Milestone 0: AGI Compass And ARC Grounding

Goal: understand the lab target: skill-acquisition efficiency under novelty, not generic benchmark score-chasing.

- On the Measure of Intelligence, Francois Chollet: https://arxiv.org/abs/1911.01547
- ARC-AGI-3 official page: https://arcprize.org/arc-agi/3
- ARC-AGI-3 technical paper: https://arxiv.org/abs/2603.24621
- ARC-AGI Toolkit quickstart: https://docs.arcprize.org/toolkit/overview
- ARC Prize 2026 ARC-AGI-3 competition: https://arcprize.org/competitions/2026/arc-agi-3
- ARC Prize docs: https://docs.arcprize.org/
- ARC Prize 2024 winners technical report: https://arcprize.org/media/arc-prize-2024-technical-report.pdf
- ARC Prize 2025 results analysis: https://arcprize.org/blog/arc-prize-2025-results-analysis
- The Bitter Lesson, Rich Sutton: https://www.incompleteideas.net/IncIdeas/BitterLesson.html
- Building Machines That Learn and Think Like People: https://arxiv.org/abs/1604.00289

Implementation output:

- 1-2 page lab thesis.
- ARC-AGI-3 constraint/spec summary.
- ARC transfer table: static ARC methods -> interactive ARC-AGI-3 agent components.

## Milestone 1: Neural Network Fundamentals

Goal: implement and debug neural machinery from first principles.

- Adam: A Method for Stochastic Optimization: https://arxiv.org/abs/1412.6980
- Decoupled Weight Decay Regularization: https://arxiv.org/abs/1711.05101
- Deep Residual Learning for Image Recognition: https://arxiv.org/abs/1512.03385
- Understanding the difficulty of training deep feedforward neural networks, Xavier initialization: https://proceedings.mlr.press/v9/glorot10a.html
- Delving Deep into Rectifiers, Kaiming initialization: https://arxiv.org/abs/1502.01852
- PyTorch autograd mechanics: https://docs.pytorch.org/docs/stable/notes/autograd.html

Implementation output:

- Adam and AdamW from scratch.
- MLP/residual block tests.
- Tiny training loop with overfit-tiny-batch test.
- Loss curves and failure notes.

## Milestone 2: Transformer Mechanics

Goal: build the core decoder-only transformer components needed for Project 001.

- Attention Is All You Need: https://arxiv.org/abs/1706.03762
- RMSNorm: https://arxiv.org/abs/1910.07467
- RoFormer / RoPE: https://arxiv.org/abs/2104.09864
- LLaMA: https://arxiv.org/abs/2302.13971
- PyTorch scaled dot product attention docs: https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html
- PyTorch SDPA tutorial: https://docs.pytorch.org/tutorials/intermediate/scaled_dot_product_attention_tutorial.html

Implementation output:

- RMSNorm tests.
- RoPE tests.
- Causal attention tests, including mask correctness.
- Tiny LLaMA-style block.
- Naive attention vs PyTorch SDPA comparison.

## Milestone 3: Small LMs From Scratch

Goal: train, evaluate, and document a small language model under the one-GPU constraint.

- GPT-2 paper: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- nanoGPT: https://github.com/karpathy/nanoGPT
- TinyStories: https://arxiv.org/abs/2305.07759
- FineWeb-Edu dataset: https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu
- Hugging Face tokenizers docs: https://huggingface.co/docs/tokenizers/index
- SentencePiece: https://github.com/google/sentencepiece

Implementation output:

- BPE or SentencePiece wrapper.
- Tiny GPT training run.
- Train loss, validation loss, perplexity, tokens/sec, peak VRAM.
- Sample generations and failure examples.

## Milestone 4: Evaluation Spine

Goal: make measurement a reusable subsystem before serious training claims.

- MMLU: https://arxiv.org/abs/2009.03300
- HELM: https://arxiv.org/abs/2211.09110
- HumanEval: https://arxiv.org/abs/2107.03374
- SWE-bench: https://arxiv.org/abs/2310.06770
- lm-evaluation-harness: https://github.com/EleutherAI/lm-evaluation-harness
- Inspecting and Understanding LLM Eval: https://hamel.dev/blog/posts/evals/

Implementation output:

- Eval harness v0.
- Fixed configs and seeds.
- Baseline tables.
- Failure taxonomy with examples.

## Milestone 5: Single-GPU Post-Training

Goal: implement adapter mechanics once, then use mature tools for practical runs.

- LoRA: https://arxiv.org/abs/2106.09685
- QLoRA: https://arxiv.org/abs/2305.14314
- DoRA: https://arxiv.org/abs/2402.09353
- Hugging Face PEFT LoRA guide: https://huggingface.co/docs/peft/main/en/developer_guides/lora
- Hugging Face PEFT quantization guide: https://huggingface.co/docs/peft/main/en/developer_guides/quantization
- TRL docs: https://huggingface.co/docs/trl
- TRL SFT trainer: https://huggingface.co/docs/trl/sft_trainer
- Unsloth docs: https://docs.unsloth.ai/
- Axolotl docs: https://docs.axolotl.ai/

Implementation output:

- LoRA from scratch on the tiny transformer.
- QLoRA SFT run using library tools.
- Before/after evals, not cherry-picked examples.

## Milestone 6: Preference Optimization

Goal: understand preference methods by implementing the loss and measuring against SFT.

- InstructGPT: https://arxiv.org/abs/2203.02155
- DPO: https://arxiv.org/abs/2305.18290
- DeepSeekMath / GRPO: https://arxiv.org/abs/2402.03300
- DeepSeek-R1: https://arxiv.org/abs/2501.12948
- Open-R1 blog: https://huggingface.co/blog/open-r1
- Open-R1 repo: https://github.com/huggingface/open-r1
- TRL DPO trainer: https://huggingface.co/docs/trl/dpo_trainer
- TRL GRPO trainer: https://huggingface.co/docs/trl/grpo_trainer

Implementation output:

- DPO loss from scratch.
- Small preference dataset.
- SFT baseline vs DPO run.
- Reward/rubric failure analysis.

## Milestone 7: Inference And Quantization

Goal: measure local serving and quantization tradeoffs on the actual GPU.

- vLLM / PagedAttention: https://arxiv.org/abs/2309.06180
- vLLM docs: https://docs.vllm.ai/
- SGLang docs: https://docs.sglang.io/
- llama.cpp: https://github.com/ggml-org/llama.cpp
- LLM.int8: https://arxiv.org/abs/2208.07339
- GPTQ: https://arxiv.org/abs/2210.17323
- AWQ: https://arxiv.org/abs/2306.00978
- SmoothQuant: https://arxiv.org/abs/2211.10438

Implementation output:

- vLLM/SGLang/Transformers benchmark.
- Quantization benchmark.
- Latency, tokens/sec, peak VRAM, context length, and quality notes.

## Milestone 8: Training Systems And Dynamics

Goal: understand why runs succeed or fail under memory and compute constraints.

- Scaling Laws for Neural Language Models: https://arxiv.org/abs/2001.08361
- Chinchilla: https://arxiv.org/abs/2203.15556
- Tensor Programs V / muP: https://arxiv.org/abs/2203.03466
- ZeRO: https://arxiv.org/abs/1910.02054
- Megatron-LM: https://arxiv.org/abs/1909.08053
- PyTorch activation checkpointing: https://docs.pytorch.org/docs/stable/checkpoint.html

Implementation output:

- VRAM budget calculator.
- Activation checkpointing experiment.
- Tiny scaling-law sweep.
- Run checklist with tokens/sec, grad norm, LR, and checkpoint health.

## Milestone 9: Search, Planning, And Agent Loops

Goal: evaluate search and agent mechanisms beyond demos.

- Chain-of-Thought: https://arxiv.org/abs/2201.11903
- Self-Consistency: https://arxiv.org/abs/2203.11171
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
- ReAct: https://arxiv.org/abs/2210.03629
- Reflexion: https://arxiv.org/abs/2303.11366
- SWE-agent: https://arxiv.org/abs/2405.15793

Implementation output:

- CoT/self-consistency harness.
- ReAct-style loop on a toy environment.
- Explicit planner with score/action-count metrics.
- Reflection or memory loop with ablation.

## Milestone 10: World Models And Exploration

Goal: learn from interaction, not just static examples.

- Go-Explore: https://arxiv.org/abs/1901.10995
- Random Network Distillation: https://arxiv.org/abs/1810.12894
- World Models: https://arxiv.org/abs/1803.10122
- Dreamer: https://arxiv.org/abs/1912.01603
- DreamerV3: https://arxiv.org/abs/2301.04104
- MuZero: https://arxiv.org/abs/1911.08265

Implementation output:

- Exploration baselines.
- State hashes and transition tables.
- Tiny transition model.
- State coverage, reward discovery, and action-count metrics.

## Milestone 11: Object-Centric Reasoning And DSLs

Goal: convert observations into objects, relations, transitions, and programs.

- Slot Attention: https://arxiv.org/abs/2006.15055
- Relational Inductive Biases / Graph Networks: https://arxiv.org/abs/1806.01261
- Human-level Concept Learning through Probabilistic Program Induction: https://www.science.org/doi/10.1126/science.aab3050
- DeepCoder: https://arxiv.org/abs/1611.01989
- DreamCoder: https://arxiv.org/abs/2006.08381
- Program-Aided Language Models: https://arxiv.org/abs/2211.10435
- Latent Program Network: https://arxiv.org/abs/2411.08706

Implementation output:

- Connected components and object graphs.
- Transition-difference analysis.
- Tiny DSL and enumerative search.
- Neural-guided program search toy benchmark.

## Milestone 12: ARC-AGI-3 Competitive System

Goal: build the self-contained ARC-AGI-3 agent stack.

- ARC-AGI-3 official page: https://arcprize.org/arc-agi/3
- ARC-AGI Toolkit quickstart: https://docs.arcprize.org/toolkit/overview
- ARC Prize 2026 ARC-AGI-3 competition: https://arcprize.org/competitions/2026/arc-agi-3
- ARC-AGI Toolkit / SDK repo: https://github.com/arcprize/arc-agi
- ARC-AGI-3 agents repo: https://github.com/arcprize/ARC-AGI-3-Agents
- StochasticGoose: https://github.com/DriesSmit/ARC3-solution
- Explore It Till You Solve It: https://github.com/dolphin-in-a-coma/arc-agi-3-just-explore
- Static ARC corpus: https://github.com/fchollet/ARC-AGI

Implementation output:

- Local runner.
- Trace logger.
- Replay viewer.
- Graph explorer.
- Action-change predictor.
- Custom holdout suite.
- Package-ready offline agent.

## Milestone 13: Public Research Lab

Goal: turn experiments into a coherent public portfolio.

- Model cards guide: https://huggingface.co/docs/hub/model-cards
- Dataset cards guide: https://huggingface.co/docs/hub/datasets-cards
- Papers with Code reproducibility checklist: https://paperswithcode.com/rc2020
- The Turing Way reproducible research guide: https://the-turing-way.netlify.app/reproducible-research/reproducible-research.html

Implementation output:

- Paper implementation reports.
- Model cards and dataset cards.
- Benchmark tables with raw logs.
- Failure reports.
- X threads and longer technical posts.
