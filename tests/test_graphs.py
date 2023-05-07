import pytest
from slink.graphs import Graph, GraphNode
from .conftest import graph_nodes, graph_edges


def test_add_node(graph_nodes):
    graph = Graph()
    node_a, _, _, _, _, _ = graph_nodes
    graph.add_node(node_a.data)
    assert len(graph.nodes) == 1
    assert node_a in graph.nodes


def test_add_edge(graph_nodes):
    graph = Graph()
    node_a, node_b, _, _, _, _ = graph_nodes
    graph.add_node(node_a.data)
    graph.add_node(node_b.data)
    graph.add_edge(node_a, node_b)
    assert node_a.neighbors == [node_b]


def test_remove_node(graph_edges):
    graph = Graph()
    node_a, node_b, node_c, _, _, _ = graph_edges
    graph.nodes = {node_a, node_b, node_c}
    graph.remove_node(node_b)
    assert len(graph.nodes) == 2
    assert node_b not in graph.nodes
    assert node_b not in node_a.neighbors
    assert node_b not in node_c.neighbors


def test_remove_edge(graph_edges):
    graph = Graph()
    node_a, node_b, node_c, _, _, _ = graph_edges
    graph.nodes = {node_a, node_b, node_c}
    node_a.add_neighbor(node_b)
    node_b.add_neighbor(node_c)
    graph.remove_edge(node_a, node_b)
    assert node_a.neighbors == []
    assert node_b.neighbors == [node_c]


def test_depth_first_search(graph_edges, capsys):
    graph = Graph()
    node_a, _, _, _, _, _ = graph_edges
    graph.nodes = {node_a}
    graph.depth_first_search(node_a)
    captured = capsys.readouterr()
    assert captured.out == "A\nB\nC\nD\nE\nF\nC\n"


def test_breadth_first_search(graph_edges, capsys):
    graph = Graph()
    node_a, _, _, _, _, _ = graph_edges
    graph.nodes = {node_a}
    graph.breadth_first_search(node_a)
    captured = capsys.readouterr()
    assert captured.out == "A\nB\nC\nD\nE\nF\n"