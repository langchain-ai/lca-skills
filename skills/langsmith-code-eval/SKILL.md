---
name: langsmith-code-eval
description: Create code-based evaluators for LangSmith-traced agents. Use when building custom evaluation logic for agent experiments, testing tool usage patterns, or scoring agent outputs programmatically.
---

# LangSmith Code Evaluator Creation

Create evaluators for LangSmith experiments through collaborative inspection and implementation.

## Workflow

### Step 1: Locate and Understand the Agent
Ask for the agent file. Read it to identify entry point, tools, and output format.

### Step 2: Inspect Trace Structure
Ask for LangSmith project name. Run:
```bash
python scripts/inspect_trace.py PROJECT_NAME [RUN_ID]
```

**Think critically about the trace:**
- Does it match the agent? (e.g., a LangGraph trace for an OpenAI agent won't work)
- Does it contain the data needed for the evaluation goals?
- If not, clarify what's missing before proceeding.

### Step 3: Clarify Evaluation Goals
Ask: "What behavior should pass vs fail?"

### Step 4: Create the Evaluator
Write the evaluator based on trace structure from Step 2. Consult the [Code Evaluator SDK docs](https://docs.langchain.com/langsmith/code-evaluator-sdk) for:
- Available function signatures and parameters
- Return type options
- Row-level vs summary evaluators

### Step 5: Create Experiment Runner
Create a script that runs the evaluator against a dataset. See [Evaluate LLM Applications](https://docs.langchain.com/langsmith/evaluate-llm-application) for `evaluate()` / `aevaluate()` usage.

### Step 6: Run and Iterate
Execute the experiment, review results in LangSmith, refine as needed.

## Reference

- [Code Evaluator SDK](https://docs.langchain.com/langsmith/code-evaluator-sdk) - Signatures, parameters, return types
- [Evaluate LLM Applications](https://docs.langchain.com/langsmith/evaluate-llm-application) - `evaluate()` / `aevaluate()` usage
- [Summary Evaluators](https://docs.langchain.com/langsmith/summary) - Experiment-level metrics (precision, recall, f1)
- [Evaluation Concepts](https://docs.langchain.com/langsmith/evaluation-concepts) - Overview of evaluator types (code, LLM-as-judge, pairwise)
