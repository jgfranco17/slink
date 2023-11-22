import pytest

from slink.arrays import Array

from .conftest import empty_array, simple_array


def test_array_str(simple_array):
    simple_array[0] = 1
    simple_array[1] = 2
    simple_array[2] = 3
    simple_array[3] = 4
    simple_array[4] = 5
    assert str(simple_array) == "[1 2 3 4 5]"


def test_array_get_item(simple_array):
    simple_array[0] = 1
    simple_array[1] = 2
    simple_array[2] = 3
    simple_array[3] = 4
    simple_array[4] = 5
    assert simple_array[0] == 1
    assert simple_array[1] == 2
    assert simple_array[2] == 3
    assert simple_array[3] == 4
    assert simple_array[4] == 5


def test_array_resize(simple_array):
    simple_array.resize(10)
    assert len(simple_array) == 10
    simple_array.resize(3)
    assert len(simple_array) == 3


def test_array_insert():
    array = Array(3)
    array[0] = 1
    array[1] = 2
    array.insert(1, 3)
    assert str(array) == "[1 3 2 None]"


def test_array_remove(simple_array):
    simple_array[0] = 1
    simple_array[1] = 2
    simple_array[2] = 3
    simple_array.remove(2)
    assert str(simple_array) == "[1 3 None None]"
    with pytest.raises(ValueError):
        simple_array.remove(4)


def test_array_iteration():
    array = Array(3)
    array[0] = 1
    array[1] = 2
    array[2] = 3
    items = []
    for value in array:
        items.append(value)
    assert items == [1, 2, 3]


def test_array_invalid_resize(empty_array):
    with pytest.raises(TypeError):
        empty_array.resize("invalid_input")


def test_array_invalid_insert(simple_array):
    with pytest.raises(TypeError):
        simple_array.insert("invalid_index", 5)
    with pytest.raises(IndexError):
        simple_array.insert(-1, 5)
    with pytest.raises(IndexError):
        simple_array.insert(6, 5)


def test_array_invalid_remove(simple_array):
    with pytest.raises(ValueError):
        simple_array.remove(4)
