# Trees

## Overview

A tree is a collection of nodes connected by edges, with a designated root node at the top. Each node can have any number of child nodes, and the nodes are often organized into levels.

## Properties

- **Hierarchical structure:** Nodes in a tree are organized into a hierarchical structure, with the root node at the top and child nodes branching out from the parent nodes.
- **Recursive definition:** Trees are defined recursively as a collection of nodes, each of which is itself the root of a subtree.
- **Directed acyclic graph:** Trees are a special case of directed acyclic graphs, where there are no cycles in the graph.

## Operations

- **Traversal:** Visit each node in the tree exactly once, according to a specific traversal order, such as pre-order, in-order, or post-order traversal.
- **Search:** Find a node with a given value in the tree by traversing the tree.
- **Insertion:** Add a new node with a given value to the tree at the appropriate position.
- **Deletion:** Remove a node with a given value from the tree and adjust the tree to maintain the binary search tree property.

## Complexity Analysis

| **Operation** | **Best Case** | **Worst Case** | **Average Case** |
| ------------- | ------------- | -------------- | ---------------- |
| Traversal     | O(n)          | O(n)           | O(n)             |
| Search        | O(1)          | O(n)           | O(n)             |
| Insertion     | O(1)          | O(log n)       | O(log n)         |
| Deletion      | O(1)          | O(log n)       | O(log n)         |
