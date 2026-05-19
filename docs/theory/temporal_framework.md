# Temporal Framework

## Purpose

The temporal framework treats computation as ordered state evolution rather than isolated execution. Each run is modeled as a sequence of transformations:

```text
psi_{k+1} = O_k psi_k
```

This supports deterministic replay, stepwise auditing, and comparison across operator families.

## Current role

The framework helps distinguish:

- persistent structure from transient artifacts
- actual operator behavior from environment noise
- collapse regimes from ordinary convergence
- DAG reuse effects from spectral projection effects

## Core observables

- flow energy
- curvature proxy
- propagation ratio
- entropy shift
- error versus baseline
- runtime

## Operational rule

Every temporal experiment should write a result row to `results/` with enough metadata to replay the run.
