import pytest
from slink.stacks import Stack
from slink.lists import LinkedList, DoublyLinkedList
from slink.hash import HashMap, HashTable


@pytest.fixture
def base_stack():
    return Stack()


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def non_empty_list():
    llist = LinkedList()
    llist.add(1)
    llist.add(2)
    llist.add(3)
    return llist


@pytest.fixture
def doubly_empty_list():
    return DoublyLinkedList()


@pytest.fixture
def doubly_non_empty_list():
    dlist = DoublyLinkedList()
    dlist.insert_at_head(1)
    dlist.insert_at_head(2)
    dlist.insert_at_head(3)
    return dlist


@pytest.fixture
def simple_hashtable():
    hashtable = HashTable(5)
    return hashtable


@pytest.fixture
def base_hashmap():
    hashmap = HashMap()
    return hashmap
