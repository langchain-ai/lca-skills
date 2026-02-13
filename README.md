# LCA Skills

A collection of agent skills for LangChain Academy and LangSmith workflows.

## Available Skills

### 🔍 langsmith-code-eval

Create code-based evaluators for LangSmith-traced agents with step-by-step collaborative guidance.

**Use when:** Building custom evaluators to test agent behavior, tool usage, and response quality in LangSmith.

**Features:**
- 9-step collaborative workflow
- Automatic trace structure inspection
- Category-based evaluation patterns
- Complete code generation for evaluators and experiment runners

## Installation

Install all skills:
```bash
npx skills add langchain-ai/lca-skills
```

Install specific skill:
```bash
npx skills add langchain-ai/lca-skills/tree/main/skills/langsmith-code-eval
```

For Claude Code:
```bash
npx skills add langchain-ai/lca-skills -a claude-code
```

## Skills Included

| Skill | Description | Documentation |
|-------|-------------|---------------|
| `langsmith-code-eval` | Create LangSmith code evaluators | [SKILL.md](skills/langsmith-code-eval/SKILL.md) |

## Contributing

Have a skill to add? Open a pull request with your skill in the `skills/` directory.

## License

Apache 2.0

---

Built for [LangChain Academy](https://academy.langchain.com)
