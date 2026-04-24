# Day 3: Learn Data, Formats, And Tokenization

## Goal

Understand that data quality and formatting usually matter more than people expect.

## Why This Day Matters

People like talking about architectures and training tricks, but small projects usually win or lose on task definition and example quality. Today is about becoming more precise.

## Time Budget

- Reading: 20 to 30 minutes
- Dataset drafting: 60 to 90 minutes
- Notes and X post: 20 to 30 minutes

Total: 2 to 2.5 hours

## Learn Before Starting

- Why model quality is shaped by data, not just architecture.
- Why prompt formatting and chat templates affect results.
- What tokenization does and why it matters for cost and behavior.

## Read Before Starting

- A tokenizer primer from Hugging Face docs:
  - https://huggingface.co/docs/transformers/tokenizer_summary
- TRL docs for dataset expectations:
  - https://huggingface.co/docs/trl
- Browse one instruction dataset on Hugging Face and inspect format carefully.

Keep the reading short. Today is mainly about touching the data directly.

## What You Should Understand By The End

- why a narrow task is easier to train and evaluate
- why formatting consistency matters
- what makes an example usable or unusable for tuning

## Step-By-Step Agenda

1. Open `day-03-data-and-tokenization.ipynb`.
2. Pick one narrow task you care about.

Examples:

- structured extraction
- code repair
- concise research summarization
- agent tool selection

3. Write the task in one sentence.
   If the task takes more than one sentence to explain, it is probably still too broad.
4. Write 5 gold examples manually.
   Do not start with 100. Start with 5 high-quality examples.
5. Inspect those 5 examples for consistency.
   Check tone, formatting, output length, and clarity.
6. Expand to a tiny dataset of 25 to 100 examples.

The dataset can be hand-written or lightly adapted from public sources, but keep it narrow and consistent.

7. Define the schema clearly.

Possible formats:

- plain instruction / response
- chat messages
- preference pairs

8. Inspect token lengths.

Measure:

- average prompt length
- average completion length
- longest example

9. Write down likely data problems:

- inconsistent style
- leakage
- mixed task definitions
- too-long outputs
- weak targets

10. Draft an X post with:
   - the task you chose
   - one lesson about dataset quality
   - one thing that was harder than expected

## Checkpoints

- Can you explain the task in one sentence?
- Can you point to one example and explain why it is good?
- Do your examples all imply the same behavior, or are they mixed?
- Would you know how to score success on this task later?

## Common Mistakes

- Starting with a broad, fuzzy task.
- Collecting many examples before defining the format.
- Mixing examples from different tasks into one dataset.
- Ignoring output length and style consistency.

## Artifact To Produce

Create:

- a notebook: `day-03-data-and-tokenization.ipynb`
- a dataset note with:
  - task definition
  - schema
  - 3 example records
  - token length stats
  - quality risks
- one X post draft

## Done Means

- you have a real dataset idea, not a vague domain interest
- you understand your example format
- you see why data cleaning is part of modeling, not an afterthought

## If You Finish Early

- Label your examples by difficulty.
- Add a section called "examples I rejected and why."

## Reflection Prompts

- Was it harder to define the task or to write examples?
- What makes an example high quality?
- What would make this dataset fail in training?
