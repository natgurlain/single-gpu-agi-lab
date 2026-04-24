# Day 4: Understand And Plan Your First LoRA / QLoRA Run

## Goal

Translate the earlier theory into a concrete fine-tuning plan that fits your hardware.

## Why This Day Matters

Most failed training runs are badly planned before they are badly executed. Today is about deciding what you are trying to improve and how you will tell if it worked.

## Time Budget

- Reading: 30 to 45 minutes
- Planning notebook: 60 to 75 minutes
- Notes and X post: 20 to 30 minutes

Total: about 2 hours

## Learn Before Starting

- What LoRA changes versus full fine-tuning.
- Why QLoRA is a strong default for single-GPU adaptation.
- Which training hyperparameters matter most at small scale:
  - learning rate
  - batch size
  - gradient accumulation
  - sequence length
  - number of steps

## Read Before Starting

- QLoRA paper: https://arxiv.org/abs/2305.14314
- PEFT docs: https://huggingface.co/docs/peft
- TRL docs: https://huggingface.co/docs/trl
- Unsloth docs or Axolotl docs:
  - https://docs.unsloth.ai/
  - https://docs.axolotl.ai/

Do not read both deeply. Pick one path and move on.

## What You Should Understand By The End

- why QLoRA is the default practical choice for your setup
- which hyperparameters matter most for a first run
- what your first experiment is actually testing

## Step-By-Step Agenda

1. Open `day-04-first-qlora-plan.ipynb`.
2. Choose your first training target:

- model
- dataset
- task

3. Write one sentence describing the exact behavior you want to improve.
   Example: "I want the model to return valid structured JSON for my extraction task."
4. Decide your training setup:

- LoRA or QLoRA
- max sequence length
- target modules if needed
- expected batch strategy
- eval split

5. Define a minimal experiment matrix.

Good first matrix:

- baseline untuned model
- run A with conservative settings
- run B with one changed variable

6. Define what success means.

Example success criteria:

- better structured output adherence
- lower error rate on your validation prompts
- better performance on a small custom eval set

7. Write down expected failure modes.

Examples:

- overfitting
- output style collapse
- training instability
- no measurable improvement

8. Draft an X post with:
   - which model you plan to tune
   - why QLoRA fits a single GPU
   - the narrow task you picked

## Checkpoints

- Can you describe the exact target behavior in one sentence?
- Do you know what variable changes between Run A and Run B?
- Do you have a baseline to compare against?
- Would a stranger understand what counts as success?

## Common Mistakes

- Starting training before defining the eval.
- Changing too many variables at once.
- Copying hyperparameters with no idea why they exist.
- Picking a task too broad for a first run.

## Artifact To Produce

Create:

- a notebook: `day-04-first-qlora-plan.ipynb`
- a training plan note with:
  - exact model
  - exact task
  - dataset summary
  - planned hyperparameters
  - success criteria
  - failure checklist
- one X post draft

## Done Means

- you could explain your run before launching it
- you know what you are trying to improve
- you are not using random hyperparameters copied without understanding

## If You Finish Early

- Add a "reasons this plan could fail" section.
- Write down your top 3 uncertainties before the actual run.

## Reflection Prompts

- Why is QLoRA a better fit than full fine-tuning here?
- What would count as a misleading "improvement"?
- Which variable would you change second, and why?
