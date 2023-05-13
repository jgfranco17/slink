import pytest
from slink.nodes import SinglyLinkedNode
from slink.lists import LinkedList, DoublyLinkedList, CircularLinkedList


def test_linked_list_init():
    llist = LinkedList()
    assert isinstance(llist, LinkedList)
    assert llist.head is None


def test_linked_list_len(empty_list, non_empty_list):
    assert len(empty_list) == 0
    assert len(non_empty_list) == 3


def test_linked_list_repr(empty_list, non_empty_list):
    assert str(empty_list) == ""
    assert str(non_empty_list) == "1 -> 2 -> 3"


def test_linked_list_add(empty_list):
    empty_list.add(1)
    assert len(empty_list) == 1
    assert empty_list.head.data == 1


def test_linked_list_insert(empty_list):
    empty_list.insert(1)
    assert len(empty_list) == 1
    assert empty_list.head.data == 1


def test_linked_list_insert_nth(empty_list):
    empty_list.insert_nth(0, 1)
    assert len(empty_list) == 1
    assert empty_list.head.data == 1
    empty_list.insert_nth(1, 2)
    assert len(empty_list) == 2
    assert empty_list.head.next.data == 2


def test_linked_list_is_empty(empty_list, non_empty_list):
    assert empty_list.is_empty is True
    assert non_empty_list.is_empty is False


def test_doubly_linked_list_init():
    dlist = DoublyLinkedList()
    assert dlist.head is None
    assert dlist.tail is None
    assert dlist.is_empty is True
    assert str(dlist) == ""


def test_doubly_linked_list_len(doubly_empty_list, doubly_non_empty_list):
    assert len(doubly_empty_list) == 0
    assert len(doubly_non_empty_list) == 3


def test_doubly_linked_list_insert_at_head(doubly_empty_list):
    doubly_empty_list.insert(1)
    assert len(doubly_empty_list) == 1
    assert doubly_empty_list.head.data == 1
    assert doubly_empty_list.tail.data == 1


def test_doubly_linked_list_insert_at_tail(doubly_empty_list):
    doubly_empty_list.add(1)
    assert len(doubly_empty_list) == 1
    assert doubly_empty_list.head.data == 1
    assert doubly_empty_list.tail.data == 1


def test_doubly_linked_list_insert_at_nth(doubly_empty_list):
    doubly_empty_list.insert_nth(0, 1)
    assert len(doubly_empty_list) == 1
    assert doubly_empty_list.head.data == 1
    assert doubly_empty_list.tail.data == 1
    doubly_empty_list.insert_at_nth(1, 2)
    assert len(doubly_empty_list) == 2
    assert doubly_empty_list.head.next.data == 2
    assert doubly_empty_list.tail.data == 2


def test_doubly_linked_list_is_empty(doubly_empty_list, doubly_non_empty_list):
    assert doubly_empty_list.is_empty is True
    assert doubly_non_empty_list.is_empty is False


def test_circular_linked_list_init(circular_empty_list):
    assert len(circular_empty_list) == 0
    assert circular_empty_list.is_empty is True


def test_circular_linked_list_methods(circular_empty_list):
    for invalid_index in (0, -1):
        with pytest.raises(IndexError):
            circular_empty_list.delete_nth(invalid_index)