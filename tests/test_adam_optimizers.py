import pytest

torch = pytest.importorskip("torch")

from lab.optim.adam import Adam, AdamW


def _run_reference_pair(optimizer_cls, reference_cls, *, weight_decay: float = 0.0) -> tuple[torch.Tensor, torch.Tensor]:
    torch.manual_seed(0)
    ours_param = torch.nn.Parameter(torch.tensor([1.0, -2.0, 3.0]))
    ref_param = torch.nn.Parameter(ours_param.detach().clone())

    ours = optimizer_cls([ours_param], lr=1e-2, betas=(0.8, 0.9), eps=1e-8, weight_decay=weight_decay)
    ref = reference_cls([ref_param], lr=1e-2, betas=(0.8, 0.9), eps=1e-8, weight_decay=weight_decay)

    for _ in range(5):
        grad = torch.tensor([0.1, -0.2, 0.3])
        ours_param.grad = grad.clone()
        ref_param.grad = grad.clone()
        ours.step()
        ref.step()

    return ours_param.detach(), ref_param.detach()


@pytest.mark.skip(reason="Exercise: implement Adam.step, then remove this skip.")
def test_adam_matches_torch_on_controlled_tensor() -> None:
    ours, ref = _run_reference_pair(Adam, torch.optim.Adam, weight_decay=0.0)
    torch.testing.assert_close(ours, ref, rtol=1e-6, atol=1e-8)


@pytest.mark.skip(reason="Exercise: implement coupled Adam weight decay, then remove this skip.")
def test_adam_matches_torch_with_coupled_weight_decay() -> None:
    ours, ref = _run_reference_pair(Adam, torch.optim.Adam, weight_decay=0.1)
    torch.testing.assert_close(ours, ref, rtol=1e-6, atol=1e-8)


@pytest.mark.skip(reason="Exercise: implement AdamW.step, then remove this skip.")
def test_adamw_matches_torch_with_decoupled_weight_decay() -> None:
    ours, ref = _run_reference_pair(AdamW, torch.optim.AdamW, weight_decay=0.1)
    torch.testing.assert_close(ours, ref, rtol=1e-6, atol=1e-8)


@pytest.mark.skip(reason="Exercise: implement per-parameter optimizer state, then remove this skip.")
def test_optimizer_state_is_per_parameter() -> None:
    p1 = torch.nn.Parameter(torch.tensor([1.0]))
    p2 = torch.nn.Parameter(torch.tensor([10.0]))
    optim = Adam([p1, p2], lr=0.1)

    p1.grad = torch.tensor([1.0])
    p2.grad = torch.tensor([2.0])
    optim.step()

    assert id(p1) in optim.state
    assert id(p2) in optim.state
    assert optim.state[id(p1)]["m"] is not optim.state[id(p2)]["m"]
    assert optim.state[id(p1)]["v"] is not optim.state[id(p2)]["v"]


@pytest.mark.skip(reason="Exercise: implement optimizer update, then remove this skip.")
def test_adam_decreases_tiny_quadratic_loss() -> None:
    x = torch.nn.Parameter(torch.tensor([5.0]))
    optim = Adam([x], lr=0.1)

    losses = []
    for _ in range(30):
        loss = (x - 1.5).pow(2).sum()
        losses.append(loss.item())
        loss.backward()
        optim.step()
        optim.zero_grad()

    assert losses[-1] < losses[0] * 0.1
