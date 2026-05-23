"""Verify that PyTorch and JAX can see and use the local NVIDIA GPU."""

from __future__ import annotations

import json
import os
import subprocess
import sys


def _run_nvidia_smi() -> str:
    try:
        return subprocess.check_output(
            [
                "nvidia-smi",
                "--query-gpu=name,driver_version,memory.total",
                "--format=csv,noheader",
            ],
            text=True,
        ).strip()
    except Exception as exc:  # pragma: no cover - diagnostic path
        return f"nvidia-smi unavailable: {exc}"


def verify_torch() -> dict[str, object]:
    import torch

    if not torch.cuda.is_available():
        raise RuntimeError("PyTorch CUDA is not available")

    device = torch.device("cuda")
    x = torch.randn((1024, 1024), device=device)
    y = x @ x.T
    torch.cuda.synchronize()

    return {
        "version": torch.__version__,
        "cuda_build": torch.version.cuda,
        "device_count": torch.cuda.device_count(),
        "device_name": torch.cuda.get_device_name(0),
        "matmul_mean": float(y.mean().detach().cpu()),
    }


def verify_jax() -> dict[str, object]:
    import jax
    import jax.numpy as jnp

    gpu_devices = jax.devices("gpu")
    if not gpu_devices:
        raise RuntimeError(f"JAX GPU is not available; devices={jax.devices()}")

    x = jnp.ones((1024, 1024), dtype=jnp.float32)
    y = (x @ x.T).block_until_ready()

    return {
        "version": jax.__version__,
        "backend": jax.default_backend(),
        "devices": [str(device) for device in gpu_devices],
        "matmul_mean": float(jnp.mean(y)),
    }


def main() -> int:
    report = {
        "nvidia_smi": _run_nvidia_smi(),
        "python": sys.version.split()[0],
        "python_no_user_site": os.environ.get("PYTHONNOUSERSITE", ""),
        "torch": verify_torch(),
        "jax": verify_jax(),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
