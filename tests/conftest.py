import pytest
from slink.stacks import Stack


# each test runs on cwd to its temp dir
@pytest.fixture(scope="module")
def sample_stack():
    stack = Stack(limit=3)
    return stack
