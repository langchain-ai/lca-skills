---
name: langsmith-code-eval
description: Creates code-based evaluators for LangSmith-traced agents. Use when building custom evaluation logic, testing tool usage patterns, or scoring agent outputs programmatically. Triggers on requests to evaluate agents, create evaluators, or run experiments against LangSmith datasets.
---

# LangSmith Code Evaluator Creation

Creates evaluators for LangSmith experiments through structured inspection and implementation.

## Prerequisites

- `langsmith` Python package installed
- `LANGSMITH_API_KEY` environment variable set (check project's `.env` file)

## Workflow

Copy this checklist and track progress:

```
Evaluator Creation Progress:
- [ ] Step 1: Discover environment
- [ ] Step 2: Read agent code
- [ ] Step 3: Inspect trace structure
- [ ] Step 4: Inspect dataset structure
- [ ] Step 5: Clarify evaluation goals
- [ ] Step 6: Write evaluator
- [ ] Step 7: Write experiment runner
- [ ] Step 8: Run and iterate
```

### Step 1: Discover Environment

Ask the user how to run Python in their project. Common patterns:
- `python` or `python3`
- `uv run python`
- `poetry run python`
- `pdm run python`

### Step 2: Read Agent Code

Ask for the agent file path. Read it to identify:
- Entry point function (look for `@traceable` decorator)
- Available tools
- Output format (what the function returns)

### Step 3: Inspect Trace Structure

Ask for the LangSmith project name. Run the inspection script located in this skill's directory:

```bash
{python_cmd} {skill_dir}/scripts/inspect_trace.py PROJECT_NAME [RUN_ID]
```

Replace `{python_cmd}` with the command from Step 1, and `{skill_dir}` with this skill's directory path.

**Verify the trace matches the agent:**
- Does the trace type match? (e.g., OpenAI trace for OpenAI agent)
- Does it contain the data needed for evaluation?
- If mismatched, clarify before proceeding.

### Step 4: Inspect Dataset Structure

Ask for the LangSmith dataset name. Run:

```bash
{python_cmd} {skill_dir}/scripts/inspect_dataset.py DATASET_NAME
```

This reveals:
- Input schema (what gets passed to the agent)
- Output schema (reference/expected outputs)
- Metadata fields (e.g., `expected_tool`, `difficulty`, labels)

**The dataset metadata often contains ground truth for evaluation** (e.g., which tool should be called, expected classification).

### Step 5: Clarify Evaluation Goals

Ask: "What behavior should pass vs fail?"

Common evaluation types:
- **Tool usage**: Did the agent call the correct tool?
- **Output correctness**: Does output match expected format/content?
- **Policy compliance**: Did it follow specific rules?
- **Classification**: Did it categorize correctly?

### Step 6: Write the Evaluator

Create evaluator functions based on trace and dataset structure. See [EVALUATOR_REFERENCE.md](EVALUATOR_REFERENCE.md) for function signatures and return formats.

### Step 7: Write Experiment Runner

Create a script that:
1. Imports the agent's entry function
2. Wraps it as a target function
3. Runs `evaluate()` or `aevaluate()` against the dataset

See [EVALUATOR_REFERENCE.md](EVALUATOR_REFERENCE.md) for `evaluate()` usage.

### Step 8: Run and Iterate

Execute the experiment, review results in LangSmith, refine evaluators as needed.
