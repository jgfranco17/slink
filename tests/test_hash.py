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


def test_hashtable():
    hashtable = HashTable(5)

    # Test insert_data and __getitem__
    hashtable.insert_data(2)
    assert hashtable[2] == 2
    hashtable.insert_data(7)
    assert hashtable[7] == 7
    hashtable.insert_data(12)
    assert hashtable[12] == 12

    # Test keys
    assert set(hashtable.keys()) == {2, 7, 12}

    # Test balanced_factor
    assert hashtable.balanced_factor() == 0.6

    # Test bulk_insert
    hashtable.bulk_insert([17, 24, 1])
    assert hashtable[17] == 17
    assert hashtable[24] == 24
    assert hashtable[1] == 1

    # Test rehashing
    hashtable.insert_data(21)
    hashtable.insert_data(32)
    hashtable.insert_data(44)
    assert hashtable.size == 11

