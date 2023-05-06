import pytest
from slink.structexceptions import StackOverflowError, StackUnderflowError
from .conftest import sample_stack


def test_stack_underflow(sample_stack):
    """
    Test that popping an empty stack raises StackUnderflowError.
    """
    with pytest.raises(StackUnderflowError):
        _ = sample_stack.pop()


def test_stack_overflow(sample_stack):
    """
    Test that exceeding the stack limit raises StackOverflowError.
    """
    with pytest.raises(StackOverflowError):
        for value in range(sample_stack.limit + 1):
            sample_stack.push(value)