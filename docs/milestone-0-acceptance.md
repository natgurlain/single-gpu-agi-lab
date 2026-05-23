# Milestone 0 Acceptance

Status: accepted v0.
Date: 2026-05-19.

Milestone 0 gate: reproducible repo, toolchain direction, ARC runner direction, and personal
research thesis.

## Evidence

- Primary roadmap and companion paper workflow are present at the repo root.
- `MILESTONES.md` is the operational checklist.
- `pyproject.toml` defines the Python package.
- `src/lab/` exists as the monorepo package namespace.
- `tests/test_package_import.py` verifies package import.
- `scripts/smoke_test.sh` runs the test suite.
- `docs/lab-thesis.md` defines the lab thesis.
- `docs/arc-agi-3-constraints-and-scoring.md` summarizes ARC-AGI-3 constraints and scoring.
- `docs/static-to-interactive-arc-transfer.md` maps static ARC methods to interactive agent
  components.
- `papers/000_measure_of_intelligence/card.md` records the paper implementation card.

## Verification

Command:

```bash
python3 -m pytest
```

Latest observed result:

```text
1 passed
```

## Decision

Milestone 0 is accepted as a v0 lab operating system and research compass.

This does not mean the ARC runner is implemented. It means the repo now has enough structure and
direction to begin the implementation ladder. The ARC runner becomes concrete in Project 001 and
later Milestone 12 work.

## Next Milestone

Start Milestone 1 with:

1. Adam and AdamW from scratch.
2. Tiny controlled optimization task.
3. Tests against PyTorch optimizer behavior.
4. Loss curve and failure notes for `exp_0001_adamw_from_scratch`.

