import pytest
from slink.nodes import TreeNode
from slink.stacks import Stack
from slink.trees import BinaryTree
from slink.lists import LinkedList, DoublyLinkedList
from slink.graphs import Graph, GraphNode
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


@pytest.fixture
def empty_tree_node():
    empty_node = TreeNode(None)
    return empty_node


@pytest.fixture
def simple_tree_node():
    node = TreeNode(5)
    return node


@pytest.fixture
def basic_tree():
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.left = TreeNode(4)
    node.right = TreeNode(3)
    node.right.left = TreeNode(5)
    node.right.left.left = TreeNode(6)
    tree = BinaryTree(node)
    return tree


@pytest.fixture
def graph_nodes():
    node_data = [GraphNode(data) for data in "ABCDEF".split()]
    return node_data


@pytest.fixture
def graph_edges(graph_nodes):
    node_a, node_b, node_c, node_d, node_e, node_f = graph_nodes
    node_a.add_neighbor(node_b)
    node_b.add_neighbor(node_c)
    node_c.add_neighbor(node_d)
    node_c.add_neighbor(node_e)
    node_e.add_neighbor(node_f)
    node_f.add_neighbor(node_c)
    return node_a, node_b, node_c, node_d, node_e, node_f
