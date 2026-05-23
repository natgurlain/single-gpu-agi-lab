# Materials: Adam And AdamW From Scratch

Use this before editing `src/lab/optim/adam.py`.

## Required Reading

Read only the parts needed for implementation.

1. Adam paper: https://arxiv.org/abs/1412.6980
   - Read: Algorithm 1.
   - Skim: introduction and the explanation of bias correction.
   - Ignore for now: convergence proof.

2. AdamW paper: https://arxiv.org/abs/1711.05101
   - Read: the distinction between L2 regularization and decoupled weight decay.
   - Focus on why adaptive optimizers make coupled weight decay behave differently from plain SGD.
   - Ignore for now: large experiment tables.

3. PyTorch optimizer docs:
   - Adam: https://docs.pytorch.org/docs/stable/generated/torch.optim.Adam.html
   - AdamW: https://docs.pytorch.org/docs/stable/generated/torch.optim.AdamW.html
   - Use these for expected API behavior, not implementation copying.

## Mental Model

Adam keeps two moving averages per parameter:

- `m`: average gradient direction.
- `v`: average squared gradient magnitude.

The first tells the optimizer where gradients usually point. The second rescales updates so large,
noisy coordinates move more cautiously and small coordinates can still move.

Because `m` and `v` start at zero, early estimates are biased toward zero. Bias correction divides
by `1 - beta**t` so the first few steps are not artificially tiny.

AdamW changes weight decay. In regular Adam with coupled L2 decay, the decay term is added to the
gradient before the moving averages are updated. In AdamW, decay is applied directly to the
parameter separately from the gradient moments.

## Core Equations

For Adam without weight decay:

```text
g_t = grad(theta)
m_t = beta1 * m_{t-1} + (1 - beta1) * g_t
v_t = beta2 * v_{t-1} + (1 - beta2) * g_t^2
m_hat_t = m_t / (1 - beta1^t)
v_hat_t = v_t / (1 - beta2^t)
theta_t = theta_{t-1} - lr * m_hat_t / (sqrt(v_hat_t) + eps)
```

For Adam with coupled weight decay:

```text
g_t = grad(theta) + weight_decay * theta
```

Then use `g_t` in the moment updates.

For AdamW with decoupled weight decay:

```text
theta = theta * (1 - lr * weight_decay)
```

Then apply the Adam gradient update separately.

## Things You Must Get Right

- Optimizer state is per parameter, not global.
- `m` and `v` should have the same shape, device, and dtype as the parameter.
- Skip parameters with `grad is None`.
- Update parameters under `torch.no_grad()`.
- Do not accidentally track optimizer math in autograd.
- Bias correction uses the step number starting at 1.
- Adam and AdamW differ only when `weight_decay != 0`.

## Pre-Code Drill

Answer these without notes:

1. In one sentence, what does `m` estimate?
2. In one sentence, what does `v` estimate?
3. Why is `v` squared gradient instead of absolute gradient?
4. What happens to the first Adam update if you remove bias correction?
5. Why can coupled L2 decay be strange under adaptive optimizers?

## Tiny Hand Calculation

Use one scalar parameter:

```text
theta = 1.0
grad = 0.5
lr = 0.1
beta1 = 0.9
beta2 = 0.999
eps = 1e-8
m_0 = 0
v_0 = 0
t = 1
```

Compute:

```text
m_1
v_1
m_hat_1
v_hat_1
theta_1
```

You should notice something interesting about the first update after bias correction.

## Implementation Order

1. Implement Adam with `weight_decay=0`.
2. Pass `test_adam_matches_torch_on_controlled_tensor`.
3. Add coupled weight decay to Adam.
4. Pass `test_adam_matches_torch_with_coupled_weight_decay`.
5. Implement AdamW decoupled weight decay.
6. Pass `test_adamw_matches_torch_with_decoupled_weight_decay`.
7. Pass per-parameter state and tiny quadratic tests.

## High-Bar Check

Before asking for review, be ready to explain:

- why the first update magnitude often looks close to `lr * sign(grad)`;
- why AdamW decay is applied outside the moment estimates;
- why `eps` is outside the square root here;
- what would break if two parameters shared one state dict.

