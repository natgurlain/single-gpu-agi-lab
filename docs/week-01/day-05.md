# Day 5: Learn Evaluation Before You Trust Training

## Goal

Build the habit of evaluating changes instead of judging them from one or two anecdotes.

## Why This Day Matters

Without evaluation, model improvement is mostly storytelling. Today is where you stop relying on "it felt better" as your only signal.

## Time Budget

- Reading: 20 to 30 minutes
- Eval design: 45 to 60 minutes
- Baseline scoring: 45 to 60 minutes
- Notes and X post: 20 minutes

Total: 2 to 2.5 hours

## Learn Before Starting

- Why training without evaluation is mostly guesswork.
- The difference between benchmark scores and task-specific usefulness.
- Why qualitative and quantitative evaluation should both exist.

## Read Before Starting

- Hugging Face evaluation-related docs in the ecosystem
- lm-evaluation-harness repository:
  - https://github.com/EleutherAI/lm-evaluation-harness
- Hamel Husain's general eval-oriented materials and posts if available

Do not go deep into benchmark culture today. Focus on building one eval you can actually reuse.

## What You Should Understand By The End

- why a tiny imperfect eval is better than no eval
- what your chosen metric captures and what it misses
- what the baseline model currently does poorly

## Step-By-Step Agenda

1. Open `day-05-eval-baseline.ipynb`.
2. Define a tiny eval set for your chosen task.

Target size:

- 20 to 50 examples

3. Decide what you will score.

Possible metrics:

- exact match
- format validity
- pass/fail rubric
- human preference
- task-specific accuracy

4. Write a simple rubric.

Even if you score manually at first, make the rubric explicit.

5. Score 5 examples manually first.
   This helps you see whether your rubric is actually usable.
6. Test your baseline model against the eval set.

Record:

- total score
- common errors
- examples of strong outputs

7. Decide whether the eval is good enough to guide tuning.

8. Draft an X post with:
   - the task
   - the eval rubric
   - one baseline failure example

## Checkpoints

- Can you explain why your metric matters?
- Did your rubric help you score consistently?
- Can you name the baseline model's top 2 failure modes?
- Would this eval detect the improvement you care about?

## Common Mistakes

- Using a metric that is easy to compute but not useful.
- Creating an eval that is too vague to score consistently.
- Only recording good examples.
- Treating benchmark scores as a substitute for task-specific testing.

## Artifact To Produce

Create:

- a notebook: `day-05-eval-baseline.ipynb`
- an eval spec note with:
  - task definition
  - eval set description
  - scoring rubric
  - baseline results
  - limitations of the eval
- one X post draft

## Done Means

- you have an eval you can reuse after fine-tuning
- you can describe model behavior with evidence
- you have a baseline score to beat

## If You Finish Early

- Separate your eval into easy, medium, and hard items.
- Add one "must not fail" case that matters for real usage.

## Reflection Prompts

- Which failures matter most for the task?
- Which good-looking answers still fail the rubric?
- What should not be counted as success?
