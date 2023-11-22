import pytest

from slink.stacks import Stack
from slink.structexceptions import StackOverflowError, StackUnderflowError

from .conftest import base_stack


def test_stack_init(base_stack):
    assert isinstance(base_stack, Stack)
    assert base_stack.limit == 10


def test_stack_init_with_limit():
    base_stack = Stack(limit=5)
    assert base_stack.limit == 5


def test_stack_push(base_stack):
    base_stack.push(1)
    assert base_stack.size == 1
    assert base_stack.peek() == 1
    base_stack.push(2)
    assert base_stack.size == 2
    assert base_stack.peek() == 2


def test_stack_underflow(base_stack):
    with pytest.raises(StackUnderflowError):
        _ = base_stack.pop()


def test_stack_overflow(base_stack):
    with pytest.raises(StackOverflowError):
        for value in range(base_stack.limit + 1):
            base_stack.push(value)


def test_stack_pop(base_stack):
    base_stack.push(1)
    base_stack.push(2)
    assert base_stack.pop() == 2
    assert base_stack.size == 1
    assert base_stack.pop() == 1
    assert base_stack.size == 0


def test_stack_pop_empty(base_stack):
    with pytest.raises(StackUnderflowError):
        base_stack.pop()


def test_stack_peek(base_stack):
    base_stack.push(1)
    assert base_stack.peek() == 1
    base_stack.push(2)
    assert base_stack.peek() == 2


def test_stack_peek_empty(base_stack):
    with pytest.raises(StackUnderflowError):
        base_stack.peek()


def test_stack_len(base_stack):
    assert len(base_stack) == 0
    base_stack.push(1)
    assert len(base_stack) == 1


def test_stack_str(base_stack):
    base_stack.push(1)
    base_stack.push(2)
    assert str(base_stack) == "[1|2]"
