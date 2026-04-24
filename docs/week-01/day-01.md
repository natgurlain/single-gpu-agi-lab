# Day 1: Map The Territory And Set Up The Lab

## Goal

Understand the modern open-model stack at a high level and set up the project habits you will use for the rest of the lab.

## Why This Day Matters

If you skip this foundation, the rest of the week becomes cargo-culting tools and paper names. Today is about building a map so later details have somewhere to attach.

## Time Budget

- Reading: 45 to 60 minutes
- Notebook work: 45 to 60 minutes
- Notes and X post: 20 to 30 minutes

Total: 2 to 2.5 hours

## Learn Before Starting

Do not treat this section as a vocabulary list. Use the resources below in order.

### 1. Base Model Vs Instruct Model

- Best first resource:
  - Hugging Face `Chat basics`
  - https://huggingface.co/docs/transformers/main/conversations
- Then read:
  - Hugging Face `Chat templates`
  - https://huggingface.co/docs/transformers/chat_templating
- What to learn:
  - what a base or pretrained model is
  - what an instruct or chat model is
  - why formatting matters

### 2. Pretraining Vs Fine-Tuning

- Best first resource:
  - Hugging Face `Causal language modeling`
  - https://huggingface.co/docs/transformers/en/tasks/language_modeling
- Then read:
  - Hugging Face `Fine-tuning`
  - https://huggingface.co/docs/transformers/main/training
- What to learn:
  - what next-token prediction means
  - how pretraining differs from fine-tuning
  - why fine-tuning is far more realistic on one GPU

### 3. Supervised Fine-Tuning

- Best first resource:
  - Hugging Face LLM Course `Supervised Fine-Tuning`
  - https://huggingface.co/docs/course/chapter11/1
- Then read:
  - TRL `SFT Trainer`
  - https://huggingface.co/docs/trl/sft_trainer
- What to learn:
  - what SFT is actually doing
  - what input and output pairs look like
  - how datasets are formatted in practice

### 4. Preference Tuning And RL-Style Post-Training

- Best first resource:
  - Hugging Face blog `Illustrating RLHF`
  - https://huggingface.co/blog/rlhf
- Then read:
  - TRL `DPO Trainer`
  - https://huggingface.co/docs/trl/dpo_trainer
- What to learn:
  - where preference tuning fits in the stack
  - why DPO is usually more realistic than full RLHF for you
  - why reward design and evals matter

### 5. LoRA, QLoRA, And Single-GPU Training

- Best first resource:
  - PEFT `LoRA`
  - https://huggingface.co/docs/peft/main/conceptual_guides/lora
- Then read:
  - QLoRA paper
  - https://arxiv.org/abs/2305.14314
- What to learn:
  - why LoRA reduces trainable parameters
  - why QLoRA matters for limited VRAM
  - why adapter tuning is the default practical path for this lab

### 6. Tokenization

- Best first resource:
  - Hugging Face Course `Tokenizers Introduction`
  - https://huggingface.co/docs/course/chapter6/1
- Then read:
  - Hugging Face Course `Building a tokenizer, block by block`
  - https://huggingface.co/docs/course/main/en/chapter6/8
- What to learn:
  - what tokenizers do
  - why tokens matter for cost, context, and training
  - why a tokenizer mismatch can hurt performance

### 7. Notebook-First Learning

- Best first resource:
  - Project notebook template
  - [notebooks/templates/daily-lab-template.ipynb](/home/pawel/repos/single-gpu-agi-lab/notebooks/templates/daily-lab-template.ipynb)
- What to learn:
  - why the notebook is your lab bench
  - why you should capture explanations, experiments, and results in one place
  - why your X posts should come from notebook artifacts rather than memory

### Minimum Reading For Today

If you only have enough energy for the minimum:

1. Chat basics
2. Supervised Fine-Tuning
3. PEFT LoRA
4. QLoRA paper abstract and introduction

## Read Before Starting

Follow this order instead of opening things randomly:

1. `Chat basics`
   - https://huggingface.co/docs/transformers/main/conversations
2. `Supervised Fine-Tuning`
   - https://huggingface.co/docs/course/chapter11/1
3. `PEFT LoRA`
   - https://huggingface.co/docs/peft/main/conceptual_guides/lora
4. `QLoRA paper`
   - https://arxiv.org/abs/2305.14314

Optional after that:

5. `Chat templates`
   - https://huggingface.co/docs/transformers/chat_templating
6. `TRL SFT Trainer`
   - https://huggingface.co/docs/trl/sft_trainer

Do not try to master every detail today. Your job is to build a map, not to finish a literature review.

## What You Should Understand By The End

By the end of today, you should be able to explain:

- what part of the model lifecycle happens before users ever see a model
- what part of the lifecycle you can realistically work on with one GPU
- why instruction tuning and evaluation are more realistic than frontier pretraining
- what tools you are most likely to use during the next 2 weeks

## Step-By-Step Agenda

1. Spend 10 minutes writing what you currently think the training stack looks like.
   Do this before reading deeply. This gives you a baseline for what you do and do not understand.
2. Read the QLoRA abstract, intro, and conclusion first.
   Ignore heavy details for now. Your question is simple: why did this paper matter for resource-constrained training?
3. Skim the TRL landing page and vLLM quickstart.
   Do not read every option. Just identify what each tool is for.
4. Open `day-01-lab-map.ipynb`.
5. Create a glossary in the notebook.
   Define these in your own words:
   - base model
   - instruct model
   - tokenizer
   - pretraining
   - SFT
   - DPO
   - GRPO
   - quantization
   - checkpoint
6. Write a short stack map in the notebook.
   Use this sequence:
   - data collection
   - pretraining
   - instruction tuning
   - preference tuning
   - inference
   - evaluation
7. Record your hardware profile.
   Do not skip this. Your future decisions should refer back to it.
8. Choose your initial tool path.
   Keep it simple:
   - inference: vLLM
   - training: TRL + PEFT
   - fast experimentation: Jupyter
   - notes: Markdown
9. Write one sentence defining your lab niche.
10. Draft a short X post explaining the lab and its constraint.

Suggested niche:

`I reproduce practical single-GPU training and evaluation workflows for open models.`

## Recommended Decisions

- Inference: start with vLLM and one backup path like llama.cpp or Ollama.
- Training: start with TRL + PEFT, then test Unsloth once the basics are clear.
- Logging: use Markdown notes before adding heavier tooling.

## Checkpoints

Before ending the day, answer these without looking things up:

- What is the difference between a base model and an instruct model?
- Why is QLoRA important for someone with one GPU?
- What is the difference between SFT and DPO?
- Why are evals part of training work rather than an optional extra?

If you cannot answer these cleanly, stay on Day 1 and simplify your explanations further.

## Common Mistakes

- Trying to fully understand an entire paper on Day 1.
- Copying definitions instead of writing your own.
- Thinking "AGI" is one training stage.
- Choosing too many tools before you have run anything.
- Treating hardware constraints as a side note instead of a core design input.

## Artifact To Produce

Create:

- a notebook: `day-01-lab-map.ipynb`
- a short note file with:
  - glossary
  - stack map
  - hardware profile
  - niche statement
  - open questions
- one X post draft

## Done Means

- you can explain the difference between SFT, DPO, and RL in plain language
- you know which tools you intend to use first
- you are no longer thinking of "AGI" as one single training recipe
- you have one realistic public post ready to publish

## If You Finish Early

- Add one more section to your notebook: "What I thought before today vs what I think now."
- Write a 5-sentence summary of QLoRA aimed at a friend who knows Python but not ML.

## Reflection Prompts

- Which part of the stack feels most concrete?
- Which part still sounds magical?
- What would be a realistic first public post from this lab?
