# Planning Agent Architecture

AI planning and reasoning agent that decomposes complex goals into executable sub-tasks, builds dependency graphs, selects optimal execution strategies, monitors progress, and handles plan adaptation when conditions change.

## Domain Tools

- **decompose_goal**: Decompose a high-level goal into atomic sub-tasks with dependencies
- **build_execution_plan**: Build an optimized execution plan from sub-tasks
- **evaluate_plan**: Evaluate a plan for feasibility, risk, and estimated cost
- **adapt_plan**: Adapt a running plan when conditions change or tasks fail
- **track_progress**: Track execution progress and estimated completion