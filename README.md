# four-from-zero-resnet

**AlphaZero on Connect Four.** AlphaZero-style self-play on Connect Four, probing the value network for concepts like threats and centre control.

**Status:** not started.

## Question

Does self-play alone discover Connect Four strategy, and does the value network represent concepts like threats?

## Plan

- **Architecture:** a small ResNet (about 5 residual blocks, 64 channels) with a policy head over 7 columns and a value head, plus Monte Carlo tree search with PUCT. Reuse the Connect Four engine from blindfold-tfm.
- **Data:** self-play only.

## Experiments

- Win rate against random play and a simple heuristic agent.
- Move accuracy against a perfect Connect Four solver (the game is solved).
- Probes for concepts such as open three-in-a-rows and centre control, tracked over training to see when each appears.

## Done when

- It reliably beats the heuristic agent, and at least one concept probe clearly beats its control.

Plus the general checklist:

Apply this checklist with the project-specific requirements and exceptions in
[CLAUDE.md](CLAUDE.md#project-specific-scope).

- `just quick` runs end to end on CPU in under 5 minutes, as a smoke test.
- The full run fits on one consumer GPU (8–12 GB VRAM) and auto-detects cuda, mps or cpu.
- Each run saves weights, `metrics.json` and its plots to `runs/<run-name>/`.
- This README shows the headline result with plots, compares against baselines, and states negative results plainly.
- Tests cover data generators, tensor shapes and one tiny overfit check.

## Quickstart

Needs [uv](https://docs.astral.sh/uv/) and [just](https://just.systems/). Everything else, Python 3.12 included, comes from uv.

```sh
just setup              # uv sync, then install the pre-commit hooks
just quick              # CPU smoke test, under 5 minutes
just train              # full run; flags pass through, e.g. --run-name wd1.0-seed0
just analyze <run>      # baselines, probes, interventions and plots
just test               # pytest
just check              # ruff and basedpyright, as in CI
```

Copy `.env.example` to `.env` (gitignored) for `HF_TOKEN` and `HF_USER`.

## Layout

```
four-from-zero-resnet/
├── README.md                goal, plan, results with plots
├── CLAUDE.md                instructions for coding agents; AGENTS.md points here
├── .agents/                 instructions/ (Python formatting, commits) and plans/
├── pyproject.toml           metadata, dependencies, tool settings
├── uv.lock                  committed lockfile
├── .python-version          pinned by uv
├── justfile                 every routine command
├── .pre-commit-config.yaml
├── .github/workflows/ci.yml
├── src/four_from_zero_resnet/
│   └── model.py, data.py, analysis.py, utils.py
├── train.py                 CLI; --quick runs the CPU smoke test
├── predict.py               load weights and run inference
├── analyze.py               baselines, probes, interventions, plots
├── notebooks/               marimo notebooks for exploration
├── tests/
└── runs/                    outputs, gitignored
```

## Results

_No results yet._ The headline result with plots, the comparison against baselines, and any negative results go here.

## Sources

- Silver et al. 2017, AlphaZero
- Pascal Pons's Connect Four solver

## License

MIT
