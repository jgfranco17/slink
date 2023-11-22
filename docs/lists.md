# Linked Lists

## Overview

A linked list is a collection of nodes, where each node contains an element and a reference to the next node in the list. Linked lists can be singly linked, where each node has a reference to the next node, or doubly linked, where each node has references to both the next and previous nodes.

## Properties

- **Dynamic size:** Linked lists can be resized dynamically by adding or removing nodes.
- **No fixed index:** Elements in a linked list are not stored at a fixed index, but rather at the nodes themselves.
- **Sequential access:** Elements in a linked list must be accessed sequentially, starting from the head or tail of the list.

## Operations

- **Access:** Get the value of an element in the linked list by traversing the list to find the corresponding node. O(n) time complexity in worst case, where n is the length of the list.
- **Search:** Find the node that contains a given element in the linked list by traversing the list. O(n) time complexity in worst case, where n is the length of the list.
  Insertion: Insert a new node with a given element at a given index in the linked list. O(n) time complexity in worst case, where n is the length of the list.
- **Deletion:** Remove a node at a given index in the linked list. O(n) time complexity in worst case, where n is the length of the list.

## Complexity Analysis

| **Operation** | **Best Case** | **Worst Case** | **Average Case** |
| ------------- | ------------- | -------------- | ---------------- |
| Access        | O(1)          | O(n)           | O(n)             |
| Search        | O(1)          | O(n)           | O(n)             |
| Insertion     | O(1)          | O(n)           | O(n)             |
| Deletion      | O(1)          | O(n)           | O(n)             |
