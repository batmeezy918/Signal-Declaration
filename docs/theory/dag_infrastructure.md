# DAG Infrastructure

## Purpose

The DAG layer organizes computation into explicit dependencies.

```text
install dependencies
  -> build kernels
  -> run benchmarks
  -> validate outputs
  -> summarize results
  -> publish/report
```

## Current DAG level

The current framework is best described as a deterministic static DAG workflow: each node is explicit, replayable, and auditable. The next level is adaptive DAG execution where the graph can change based on measured collapse, curvature, or error signals.

## Node families

- `baseline` — reference nonlinear flow
- `spectral` — low-rank projection flow
- `dag` — cached operator reuse
- `fold` — temporal memory flow
- `dacv` — fused spectral/DAG/fold kernel

## Repo rule

Every runnable node should live in `src/` and every orchestration command should live in `scripts/`.
