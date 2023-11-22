import pytest

from slink.trees import BinaryTree

from .conftest import basic_tree, empty_tree_node, simple_tree_node


def test_tree_node_init(simple_tree_node):
    assert simple_tree_node.data == 5
    assert simple_tree_node.left is None
    assert simple_tree_node.right is None


def test_tree_node_bool(empty_tree_node, simple_tree_node):
    assert bool(simple_tree_node) == True
    assert bool(empty_tree_node) == False


def test_tree_init(simple_tree_node):
    tree = BinaryTree(simple_tree_node)
    assert tree.root == simple_tree_node
