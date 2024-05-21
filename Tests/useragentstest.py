import pytest
from ..Main.useragents import *


class TestAgentHandler:
    def test_returns_different_ua(self):
        handler = AgentHandler()
        count = 0
        while count <= 10:
            agent1 = handler.get_agent()
            agent2 = handler.get_agent()
            assert agent1 != agent2
            count += 1
