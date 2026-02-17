---
name: fetching-langsmith-traces
description: Fetches LangSmith traces for debugging agent behavior. Use when troubleshooting agent issues, reviewing conversation history, or investigating tool calls.
---

# Fetching LangSmith Traces

Requires `langsmith-fetch` in project dependencies and `LANGSMITH_API_KEY` in `.env`.

## Commands

```bash
# Fetch recent traces to directory (recommended)
uv run --env-file .env langsmith-fetch traces ./traces --limit 10

# Fetch to stdout
uv run --env-file .env langsmith-fetch traces --limit 5 --format json

# Fetch single trace by ID
uv run --env-file .env langsmith-fetch trace <trace-id>

# Include metadata (timing, tokens, costs)
uv run --env-file .env langsmith-fetch trace <trace-id> --include-metadata
```

## Output Formats

- `--format pretty` - Human-readable (default)
- `--format json` - Pretty-printed JSON
- `--format raw` - Compact JSON for piping

## Troubleshooting Workflow

1. Fetch recent traces: `uv run --env-file .env langsmith-fetch traces ./debug --limit 10`
2. Find relevant trace in saved JSON files
3. Check: What tools were called? What did they return? Was it correct/expected?
