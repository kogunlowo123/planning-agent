"""Test configuration for Planning Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "planning-agent", "category": "AI Engineering"}
