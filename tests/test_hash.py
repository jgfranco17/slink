import pytest
from slink.hash import HashMap, HashTable
from .conftest import base_hashmap, simple_hashtable


def test_hashmap_dunders(base_hashmap):
    # Add values to hashmap
    for i in range(1, 3):
        base_hashmap[i] = f'value{i}'
    
    # Test __len__
    assert len(base_hashmap) == 2

    # Test __delitem__
    del base_hashmap[1]
    assert len(base_hashmap) == 1
    assert 1 not in base_hashmap
    assert 2 in base_hashmap

    # Test __iter__
    assert set(base_hashmap) == {2}


def test_hashmap_value_setting(base_hashmap):
    base_hashmap[1] = 'value1'
    assert base_hashmap[1] == 'value1'
    base_hashmap[1] = 'value2'
    assert base_hashmap[1] == 'value2'
    base_hashmap[2] = 'value3'
    assert base_hashmap[2] == 'value3'
