# Session 0001: Adam And AdamW From Scratch

Topic: Adam and AdamW optimizers
Milestone: 1
Date: 2026-05-19

## Goal

Implement Adam and AdamW from scratch in `src/lab/optim/adam.py`.

You should be able to explain:

- the first moment update;
- the second moment update;
- bias correction;
- the difference between coupled L2 regularization and decoupled weight decay;
- why optimizer state must be per-parameter.

## Minimal Setup

Files to edit:

- `src/lab/optim/adam.py`
- `tests/test_adam_optimizers.py`
- `experiments/exp_0001_adamw_from_scratch/README.md`

Allowed references:

- Materials packet: [materials.md](materials.md)
- Adam paper: https://arxiv.org/abs/1412.6980
- AdamW paper: https://arxiv.org/abs/1711.05101
- PyTorch optimizer docs for API comparison, not for copying internals.

Not allowed yet:

- Copying PyTorch optimizer source.
- Using `torch.optim.Adam` or `torch.optim.AdamW` inside your implementation.
- Marking the milestone checkbox complete before tests, tiny run, and explanation pass.

## Pass Standard

- [ ] `Adam` update matches `torch.optim.Adam` on controlled tensors within tolerance.
- [ ] `AdamW` update matches `torch.optim.AdamW` on controlled tensors within tolerance.
- [ ] Optimizer state is separate for each parameter.
- [ ] Zero gradients are ignored safely.
- [ ] A tiny quadratic optimization task decreases loss.
- [ ] You can explain bias correction closed-book.
- [ ] You can explain decoupled weight decay closed-book.

## Prediction Before Coding

Before touching code, answer these:

1. Why are `m` and `v` initialized to zero?
2. Why do we divide by `1 - beta1**t` and `1 - beta2**t`?
3. If AdamW has `weight_decay=0.1`, does that decay get added to the gradient?
4. What should happen if a parameter has `grad is None`?
5. What bug would happen if all parameters shared the same `m` and `v` tensors?

## Implementation Notes

Key equations:

```text
m_t = beta1 * m_{t-1} + (1 - beta1) * grad
v_t = beta2 * v_{t-1} + (1 - beta2) * grad^2
m_hat = m_t / (1 - beta1^t)
v_hat = v_t / (1 - beta2^t)
param = param - lr * m_hat / (sqrt(v_hat) + eps)
```

Adam with coupled weight decay adds the decay term to the gradient before moment updates.

AdamW applies weight decay directly to the parameter update separately from the gradient moments.

## Test Notes

Start by removing `@pytest.mark.skip` from one test at a time in `tests/test_adam_optimizers.py`.

Command:

```bash
python3 -m pytest tests/test_adam_optimizers.py
```

## Exam

Recall questions:

1. Derive the Adam update for one scalar parameter.
2. Explain why the first few Adam steps are biased without correction.
3. Explain why AdamW is not just Adam plus `grad += wd * param`.

Debug questions:

1. The loss decreases for one parameter but not two. What optimizer-state bug should you suspect?
2. Your implementation matches PyTorch when `weight_decay=0` but diverges when it is nonzero. Where
   should you inspect first?

Transfer question:

1. In a tiny transformer run, what optimizer metrics would you log to catch silent training failure?

## Decision

Integrate / archive / revise:

Next action: implement `Adam` first, then `AdamW`.
