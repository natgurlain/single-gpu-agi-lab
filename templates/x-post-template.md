# X Post Template

Use this for public proof-of-work. The primary roadmap and companion paper-workflow PDFs define the standard: posts should be concrete, measured, honest, and tied to artifacts.

## Short Implementation Post

I implemented `[paper/mechanism]` from scratch on one GPU.

What worked:
- `[specific result]`

What failed:
- `[specific failure]`

Metric:
- baseline: `[number or behavior]`
- new method: `[number or behavior]`

Next:
- `[next experiment]`

Code/report:
- `[link when public]`

## Failure Report

Failed experiment: `[name]`

Hypothesis:
`[what I expected]`

Result:
`[what happened]`

Likely cause:
`[diagnosis]`

What I will change:
`[next fix or kill decision]`

Why this matters:
`[what the failure teaches]`

## Longer Technical Post

Title: What I learned implementing `[paper/mechanism]` for ARC-style agents

1. Why I chose it.
2. Core mechanism.
3. Minimal implementation.
4. Toy result.
5. ARC/synthetic integration.
6. Metrics.
7. Failure modes.
8. What I will keep, archive, or reject.

## Rules

- Always include the exact mechanism, model, dataset, or environment.
- Always include baseline and metric when available.
- Mention the single-GPU constraint when it affects design.
- Include failures and caveats.
- Do not post benchmark screenshots without configs.
- Do not claim a toy run reproduces a frontier-scale result.
- Do not announce a fine-tune without before/after evals.
