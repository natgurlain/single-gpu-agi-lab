# Day 6: Understand Preference Tuning And Small RL

## Goal

Build a correct mental model of where SFT ends and preference optimization begins.

## Why This Day Matters

This is where many people become confused by alignment language and RL hype. Today is about simplifying the conceptual picture so you know when extra complexity is justified.

## Time Budget

- Reading: 40 to 50 minutes
- Notebook explanation work: 45 to 60 minutes
- Notes and X post: 20 to 30 minutes

Total: about 2 hours

## Learn Before Starting

- Why SFT teaches imitation, while preference methods try to rank or optimize behavior.
- Why DPO is often a practical first step before heavier RL workflows.
- Why GRPO-style work is interesting but easy to misunderstand if the reward design is weak.

## Read Before Starting

- Read one paper only:
  - DPO paper: https://arxiv.org/abs/2305.18290
- Skim these implementation-oriented references:
- TRL DPO trainer docs: https://huggingface.co/docs/trl/dpo_trainer
- TRL GRPO trainer docs: https://huggingface.co/docs/trl/grpo_trainer
- Open-R1 blog: https://huggingface.co/blog/open-r1

## What You Should Understand By The End

- what SFT can already solve well
- when DPO is useful
- why jumping straight into RL-style work is often premature on one GPU

## Step-By-Step Agenda

1. Open `day-06-preference-tuning-notes.ipynb`.
2. Write your own explanation of:

- SFT
- DPO
- GRPO

Use plain language, not paper language.

3. Write one example where SFT is probably enough.
4. Define one task where preference data would help more than pure SFT.

Examples:

- answer style preference
- concise versus verbose output preference
- choosing better code repair among candidates

5. Sketch a tiny preference dataset design.

Include:

- prompt
- chosen response
- rejected response
- selection rule

6. Decide whether your first real training work should be:

- SFT only
- SFT then DPO
- SFT plus a later small RL experiment

7. Write down what would make an RL-flavored project fake or misleading.

Examples:

- weak reward function
- no held-out eval
- cherry-picked examples
- no comparison to SFT baseline

8. Draft an X post with:
   - the simplest explanation of DPO you can give
   - why you are not jumping straight into heavy RL
   - one practical next step

## Checkpoints

- Can you explain SFT, DPO, and GRPO without using paper jargon?
- Can you give one example where DPO is a better fit than plain SFT?
- Can you explain why an RL-looking project can still be methodologically weak?

## Common Mistakes

- Thinking RL is automatically more advanced and therefore better.
- Discussing alignment methods without a concrete task in mind.
- Ignoring the need for a baseline SFT comparison.
- Treating preference data as magical rather than task-specific.

## Artifact To Produce

Create:

- a notebook: `day-06-preference-tuning-notes.ipynb`
- a note called `alignment-stack-notes.md` with:
  - plain-English definitions
  - a preference dataset sketch
  - your decision for next-step training
  - risks and anti-patterns
- one X post draft

## Done Means

- you know why DPO is often more realistic than jumping straight to RLHF
- you can describe a preference dataset structure
- you have a grounded view of small-scale RL work

## If You Finish Early

- Write a one-paragraph argument for "SFT first, DPO second."
- Sketch how you would collect preference pairs for your own task.

## Reflection Prompts

- What can SFT solve well enough on its own?
- When is preference tuning worth the added complexity?
- What reward would you trust least?
