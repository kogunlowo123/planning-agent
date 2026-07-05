"""Planning Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_decompose_goal():
    """Test Decompose a high-level goal into atomic sub-tasks with dependencies."""
    tools = AgentTools()
    result = await tools.decompose_goal(goal="test", constraints="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_build_execution_plan():
    """Test Build an optimized execution plan from sub-tasks."""
    tools = AgentTools()
    result = await tools.build_execution_plan(tasks="test", strategy="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_evaluate_plan():
    """Test Evaluate a plan for feasibility, risk, and estimated cost."""
    tools = AgentTools()
    result = await tools.evaluate_plan(plan="test", success_criteria="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_adapt_plan():
    """Test Adapt a running plan when conditions change or tasks fail."""
    tools = AgentTools()
    result = await tools.adapt_plan(plan_id="test", changed_conditions="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.planning_agent_agent import PlanningAgentAgent
    agent = PlanningAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
