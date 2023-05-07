# Stack

## Overview
A stack is a collection of elements that can be accessed according to the Last-In-First-Out (LIFO) principle, where the last element added to the stack is the first to be removed.

## Properties
- **Dynamic size:** Stacks can be resized dynamically by adding or removing elements.
- **LIFO ordering:** Elements in a stack are accessed in reverse order of their insertion, according to the LIFO principle.
- **No random access:** Elements in a stack cannot be accessed by their index, but only by adding or removing elements from the top of the stack.

## Operations
- **Push:** Add a new element to the top of the stack. O(1) time complexity.
- **Pop:** Remove the element at the top of the stack. O(1) time complexity.
- **Peek:** Get the value of the element at the top of the stack without removing it. O(1) time complexity.

## Complexity Analysis
| **Operation** | **Best Case** | **Worst Case** | **Average Case** |
|---------------|---------------|----------------|------------------|
| Push          |      O(1)     |      O(1)      |       O(1)       |
| Pop           |      O(1)     |      O(1)      |       O(1)       |
| Peek          |      O(1)     |      O(1)      |       O(1)       |