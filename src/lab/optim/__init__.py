"""Optimizer implementations and optimizer experiments."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from lab.optim.adam import Adam, AdamW

__all__ = ["Adam", "AdamW"]


def __getattr__(name: str) -> object:
    if name in __all__:
        from lab.optim.adam import Adam, AdamW

        return {"Adam": Adam, "AdamW": AdamW}[name]
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
