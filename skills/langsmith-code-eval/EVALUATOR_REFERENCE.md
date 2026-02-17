# Evaluator Reference

## Evaluator Function Signature

```python
from langsmith.schemas import Run, Example

def evaluator_name(run: Run, example: Example) -> dict:
    """
    Args:
        run: Contains actual agent execution data
            - run.inputs: dict - inputs passed to agent
            - run.outputs: dict - agent outputs (structure varies by agent)
        example: Contains dataset example data
            - example.inputs: dict - inputs from dataset
            - example.outputs: dict - reference outputs (if any)
            - example.metadata: dict - metadata fields (if any)

    Returns:
        dict with:
            - key: str - metric name
            - score: float | int | bool | None - the score (None = not applicable)
            - comment: str (optional) - explanation
    """
    # Implementation depends on YOUR trace and dataset structure
    # Use inspect_trace.py and inspect_dataset.py output to determine
    # what fields are available in run.outputs and example.metadata

    return {
        "key": "metric_name",
        "score": 1,  # or 0, or 0.5, or None if not applicable
        "comment": "Optional explanation"
    }
```

## Return Format Options

Single metric:
```python
return {"key": "accuracy", "score": 1, "comment": "Correct"}
```

Multiple metrics (return a list):
```python
return [
    {"key": "metric_a", "score": 1},
    {"key": "metric_b", "score": 0},
]
```

Not applicable (use None):
```python
return {"key": "metric_name", "score": None, "comment": "N/A - condition not met"}
```

## Summary Evaluator Signature

For experiment-level metrics (precision, recall, etc.):

```python
def summary_evaluator(runs: list[Run], examples: list[Example]) -> dict:
    """Receives all runs and examples from the experiment."""
    return {"key": "aggregate_metric", "score": 0.85}
```

## Running Evaluations

```python
from langsmith import evaluate  # or aevaluate for async

def target(inputs: dict) -> dict:
    """Wrapper that calls your agent. Input keys must match dataset."""
    return your_agent(inputs["your_input_key"])

results = evaluate(
    target,
    data="dataset-name",
    evaluators=[evaluator_a, evaluator_b],
    experiment_prefix="experiment-name",
)
```

Async version:
```python
from langsmith import aevaluate

results = await aevaluate(
    async_target,
    data="dataset-name",
    evaluators=[evaluator_a],
    max_concurrency=2,
)
```

## Important

The actual structure of `run.outputs` and `example.metadata` varies by agent and dataset. Always use `inspect_trace.py` and `inspect_dataset.py` to discover the real structure before writing evaluator logic.
