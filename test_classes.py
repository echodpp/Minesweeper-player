import pytest
from Agent import Agent
from Environment import Environment
from BroadVisualzation import Mines


def test_Environment():
    oir_env = Environment(1, 1)
    assert oir_env.dim == 1


def test_Agent():
    oir_env = Environment(10, 10)
    ag = Agent(oir_env, 10)
    assert ag.num_of_mine == 10


def test_Mines():
    oir_env = Environment(10, 10)
    ag = Agent(oir_env, 10)
    m = Mines(oir_env, ag)
    assert m.agent == ag


if __name__ == "__main__":
    test_Environment()
    test_Agent()
    test_Mines()
