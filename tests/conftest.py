import pytest

from slink.arrays import Array
from slink.graphs import Graph, GraphNode
from slink.hash import HashMap, HashTable
from slink.lists import CircularLinkedList, DoublyLinkedList, LinkedList
from slink.nodes import BinaryTreeNode
from slink.stacks import Stack
from slink.trees import BinaryTree


@pytest.fixture
def empty_array():
    return Array(0)


@pytest.fixture
def simple_array():
    return Array(5)


@pytest.fixture
def base_stack() -> Stack:
    return Stack()


@pytest.fixture
def empty_list() -> LinkedList:
    return LinkedList()


@pytest.fixture
def non_empty_list() -> LinkedList:
    llist = LinkedList()
    llist.add(1)
    llist.add(2)
    llist.add(3)
    return llist


@pytest.fixture
def doubly_empty_list() -> DoublyLinkedList:
    return DoublyLinkedList()


@pytest.fixture
def doubly_non_empty_list() -> DoublyLinkedList:
    dlist = DoublyLinkedList()
    dlist.insert(1)
    dlist.insert(2)
    dlist.insert(3)
    return dlist


@pytest.fixture
def circular_empty_list() -> CircularLinkedList:
    return CircularLinkedList()


@pytest.fixture
def simple_hashtable() -> HashTable:
    hashtable = HashTable(5)
    return hashtable


@pytest.fixture
def base_hashmap() -> HashMap:
    hashmap = HashMap()
    return hashmap


@pytest.fixture
def empty_tree_node() -> BinaryTreeNode:
    empty_node = BinaryTreeNode(None)
    return empty_node


@pytest.fixture
def simple_tree_node() -> BinaryTreeNode:
    node = BinaryTreeNode(5)
    return node


@pytest.fixture
def basic_tree() -> BinaryTree:
    node = BinaryTreeNode(1)
    node.left = BinaryTreeNode(2)
    node.left.left = BinaryTreeNode(4)
    node.right = BinaryTreeNode(3)
    node.right.left = BinaryTreeNode(5)
    node.right.left.left = BinaryTreeNode(6)
    tree = BinaryTree(node)
    return tree


@pytest.fixture
def graph_nodes() -> tuple[GraphNode]:
    node_data = tuple(GraphNode(letter) for letter in "ABCDEF")
    return node_data


@pytest.fixture
def graph_edges(graph_nodes) -> tuple[GraphNode]:
    node_a, node_b, node_c, node_d, node_e, node_f = graph_nodes
    node_a.add_neighbor(node_b)
    node_b.add_neighbor(node_c)
    node_c.add_neighbor(node_d)
    node_c.add_neighbor(node_e)
    node_e.add_neighbor(node_f)
    node_f.add_neighbor(node_c)
    return node_a, node_b, node_c, node_d, node_e, node_f
