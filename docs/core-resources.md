# Core Resources

This is the curated resource map for the lab.

The rule is simple: do not collect endless bookmarks. Use one primary resource per concept, then one optional deeper source if needed.

## How To Use This Page

- Start with the `Best First Resource`.
- Use `Then Read` only if the first resource leaves important gaps.
- Do not read everything in one sitting.
- For each resource, write 3 to 5 sentences in your own words before moving on.

## 1. Base Models, Instruct Models, And Chat Formatting

### Best First Resource

- Hugging Face `Chat basics`
  - https://huggingface.co/docs/transformers/main/conversations
  - Why: this is the cleanest practical explanation of what an instruct or chat model is, and how it differs from a base or pretrained model.

### Then Read

- Hugging Face `Chat templates`
  - https://huggingface.co/docs/transformers/chat_templating
  - Why: this explains the formatting layer that many beginners miss. It matters because a lot of "model quality" problems are actually formatting problems.

## 2. Pretraining Basics

### Best First Resource

- Hugging Face `Causal language modeling`
  - https://huggingface.co/docs/transformers/en/tasks/language_modeling
  - Why: this is the most direct introduction to next-token prediction, which is the core of modern autoregressive language models.

### Then Read

- Hugging Face blog `Illustrating RLHF`
  - https://huggingface.co/blog/rlhf
  - Why: the pretraining section gives a useful larger picture of how pretraining fits into the full post-training pipeline.

## 3. Supervised Fine-Tuning

### Best First Resource

- Hugging Face LLM Course `Supervised Fine-Tuning`
  - https://huggingface.co/docs/course/chapter11/1
  - Why: this is a more learner-friendly overview than jumping straight into trainer API docs.

### Then Read

- TRL `SFT Trainer`
  - https://huggingface.co/docs/trl/sft_trainer
  - Why: once the concept is clear, this is the practical reference for dataset format, tokenization, and loss behavior.

## 4. LoRA And QLoRA

### Best First Resource

- PEFT `LoRA`
  - https://huggingface.co/docs/peft/main/conceptual_guides/lora
  - Why: this explains parameter-efficient fine-tuning in the most practical way for single-GPU work.

### Then Read

- QLoRA paper
  - https://arxiv.org/abs/2305.14314
  - Why: this is the key paper for understanding why 4-bit adapter tuning became the default practical path for constrained hardware.

## 5. Preference Tuning And RLHF

### Best First Resource

- Hugging Face blog `Illustrating RLHF`
  - https://huggingface.co/blog/rlhf
  - Why: this is still one of the best conceptual overviews of pretraining, reward modeling, and RL-style post-training.

### Then Read

- TRL `DPO Trainer`
  - https://huggingface.co/docs/trl/dpo_trainer
  - Why: DPO is more realistic than full PPO-style RLHF for your setup, so the implementation reference matters more than abstract RL theory.

## 6. Tokenization

### Best First Resource

- Hugging Face Course `Tokenizers Introduction`
  - https://huggingface.co/docs/course/chapter6/1
  - Why: this is the cleanest introduction to why tokenizers matter and when you would train or adapt one.

### Then Read

- Hugging Face Course `Building a tokenizer, block by block`
  - https://huggingface.co/docs/course/main/en/chapter6/8
  - Why: read this when you want to understand the tokenizer pipeline more concretely.

## 7. Reasoning-Model Reproductions

### Best First Resource

- Hugging Face blog `Open-R1`
  - https://huggingface.co/blog/open-r1
  - Why: this is a strong practical bridge from theory to open reproductions of reasoning-model work.

### Then Read

- Open-R1 hub page
  - https://huggingface.co/open-r1
  - Why: this is where the initiative’s models, datasets, and updates are gathered.

## 8. Local Inference And Single-GPU Usage

### Best First Resource

- vLLM quickstart
  - https://docs.vllm.ai/en/latest/getting_started/quickstart.html
  - Why: fast route to getting real local inference running.

### Then Read

- Hugging Face `Chat basics`, especially performance and memory usage
  - https://huggingface.co/docs/transformers/main/conversations
  - Why: it explains why memory bandwidth, quantization, and model size matter on local hardware.

## Recommended Reading Order For Week 1

Use this order unless you have a strong reason not to:

1. Chat basics
2. Chat templates
3. Causal language modeling
4. Supervised Fine-Tuning
5. LoRA guide
6. QLoRA paper
7. Tokenizers introduction
8. RLHF overview

## Rule For The Lab

For every concept you study:

1. Read the best first resource.
2. Write your own explanation in the notebook.
3. Only then open the deeper resource.
