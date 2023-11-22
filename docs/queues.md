# Queue

## Overview

A queue is a collection of elements that can be accessed according to the First-In-First-Out (FIFO) principle, where the first element added to the queue is the first to be removed.

## Properties

- **Dynamic size:** Queues can be resized dynamically by adding or removing elements.
- **FIFO ordering:** Elements in a queue are accessed in the same order of their insertion, according to the FIFO principle.
- **No random access:** Elements in a queue cannot be accessed by their index, but only by adding or removing elements from the front or back of the queue.

## Operations

- **Enqueue:** Add a new element to the back of the queue.
- **Dequeue:** Remove the element at the front of the queue.
- **Peek:** Get the value of the element at the front of the queue without removing it.

## Complexity Analysis

| **Operation** | **Best Case** | **Worst Case** | **Average Case** |
| ------------- | ------------- | -------------- | ---------------- |
| Enqueue       | O(1)          | O(1)           | O(1)             |
| Dequeue       | O(1)          | O(1)           | O(1)             |
| Peek          | O(1)          | O(1)           | O(1)             |
