#!/usr/bin/env bash
set -euo pipefail

ENV_NAME="${ENV_NAME:-single-gpu-agi-lab}"
MAMBA_ROOT="${MAMBA_ROOT:-/home/pawel/mambaforge}"
PYTHON_VERSION="${PYTHON_VERSION:-3.11}"
PYTORCH_CUDA_INDEX="${PYTORCH_CUDA_INDEX:-cu130}"
JAX_CUDA_EXTRA="${JAX_CUDA_EXTRA:-cuda13}"
RECREATE_ENV="${RECREATE_ENV:-0}"

usage() {
  cat <<'USAGE'
Set up the single-gpu-agi-lab mamba environment with GPU PyTorch and JAX.

Defaults:
  ENV_NAME=single-gpu-agi-lab
  MAMBA_ROOT=/home/pawel/mambaforge
  PYTHON_VERSION=3.11
  PYTORCH_CUDA_INDEX=cu130
  JAX_CUDA_EXTRA=cuda13

Common overrides:
  ENV_NAME=sgal RECREATE_ENV=1 scripts/setup_gpu_env.sh
  PYTORCH_CUDA_INDEX=cu128 JAX_CUDA_EXTRA=cuda12 scripts/setup_gpu_env.sh

The script installs:
  - this repo in editable dev mode
  - torch, torchvision, torchaudio from the selected PyTorch CUDA wheel index
  - jax with the selected CUDA extra

It then runs scripts/verify_gpu_stack.py.
USAGE
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MAMBA_SH="${MAMBA_ROOT}/etc/profile.d/mamba.sh"

if [[ ! -f "${MAMBA_SH}" ]]; then
  echo "Could not find mamba activation script at ${MAMBA_SH}" >&2
  echo "Set MAMBA_ROOT to your mambaforge root and retry." >&2
  exit 1
fi

source "${MAMBA_SH}"

if command -v nvidia-smi >/dev/null 2>&1; then
  echo "Detected NVIDIA GPU/driver:"
  nvidia-smi
else
  echo "nvidia-smi not found. Continuing, but GPU verification will likely fail." >&2
fi

if mamba env list | awk '{print $1}' | grep -Fxq "${ENV_NAME}"; then
  if [[ "${RECREATE_ENV}" == "1" ]]; then
    echo "Removing existing environment: ${ENV_NAME}"
    mamba env remove -n "${ENV_NAME}" -y
  else
    echo "Using existing environment: ${ENV_NAME}"
  fi
fi

if ! mamba env list | awk '{print $1}' | grep -Fxq "${ENV_NAME}"; then
  echo "Creating environment: ${ENV_NAME}"
  mamba create -n "${ENV_NAME}" -y -c conda-forge "python=${PYTHON_VERSION}" pip
fi

mamba activate "${ENV_NAME}"
export PYTHONNOUSERSITE=1

cd "${REPO_ROOT}"

python -m pip install --upgrade pip setuptools wheel
python -m pip install -e ".[dev]"

python -m pip install \
  torch torchvision torchaudio \
  --index-url "https://download.pytorch.org/whl/${PYTORCH_CUDA_INDEX}"

python -m pip install --upgrade "jax[${JAX_CUDA_EXTRA}]"

python scripts/verify_gpu_stack.py

echo
echo "Environment ready."
echo "Activate with:"
echo "  source ${MAMBA_SH}"
echo "  mamba activate ${ENV_NAME}"
