# Planning Agent

[![CI](https://github.com/kogunlowo123/planning-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/planning-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: AI Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

AI planning and reasoning agent that decomposes complex goals into executable sub-tasks, builds dependency graphs, selects optimal execution strategies, monitors progress, and handles plan adaptation when conditions change.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `decompose_goal` | Decompose a high-level goal into atomic sub-tasks with dependencies |
| `build_execution_plan` | Build an optimized execution plan from sub-tasks |
| `evaluate_plan` | Evaluate a plan for feasibility, risk, and estimated cost |
| `adapt_plan` | Adapt a running plan when conditions change or tasks fail |
| `track_progress` | Track execution progress and estimated completion |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/plans/decompose` | Decompose a goal |
| `POST` | `/api/v1/plans/build` | Build execution plan |
| `POST` | `/api/v1/plans/evaluate` | Evaluate plan feasibility |
| `POST` | `/api/v1/plans/{plan_id}/adapt` | Adapt a running plan |
| `GET` | `/api/v1/plans/{plan_id}/progress` | Track plan progress |

## Features

- Goal Decomposition
- Dependency Graphs
- Strategy Selection
- Progress Monitoring
- Plan Adaptation

## Integrations

- Langgraph
- Temporal
- Airflow
- Celery
- Graphdb

## Architecture

```
planning-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── planning_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**LLM + Task Orchestration + Graph Engine**

---

Built as part of the Enterprise AI Agent Platform.
