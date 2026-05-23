"""Adam-family optimizers for Milestone 1.

Exercise rule: the user implements the core update logic.
"""

from __future__ import annotations

from collections.abc import Iterable

import torch


class Adam:
    """Minimal Adam optimizer scaffold.

    Implement this class without calling ``torch.optim.Adam``.
    """

    def __init__(
        self,
        params: Iterable[torch.nn.Parameter],
        lr: float = 1e-3,
        betas: tuple[float, float] = (0.9, 0.999),
        eps: float = 1e-8,
        weight_decay: float = 0.0,
    ) -> None:
        self.params = list(params)
        self.lr = lr
        self.betas = betas
        self.eps = eps
        self.weight_decay = weight_decay
        self.step_count = 0
        self.state: dict[int, dict[str, torch.Tensor]] = {}

    def zero_grad(self) -> None:
        """Clear gradients in-place."""
        for param in self.params:
            param.grad = None

    @torch.no_grad()
    def step(self) -> None:
        """Apply one Adam update.

        Your implementation goes here.
        """
        raise NotImplementedError("Implement Adam.step as the exercise.")


class AdamW(Adam):
    """Minimal AdamW optimizer scaffold.

    Implement decoupled weight decay without calling ``torch.optim.AdamW``.
    """

    @torch.no_grad()
    def step(self) -> None:
        """Apply one AdamW update.

        Your implementation goes here.
        """
        raise NotImplementedError("Implement AdamW.step as the exercise.")

