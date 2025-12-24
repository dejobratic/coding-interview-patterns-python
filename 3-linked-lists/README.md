# Linked Lists

## Overview

Linked lists are sequential data structures where each node contains a value and reference(s) to adjacent nodes. Unlike arrays, nodes are not stored contiguously in memory but connected through pointers. Singly linked lists have each node pointing to the next node, while doubly linked lists maintain pointers to both previous and next nodes. This structure enables efficient insertions and deletions without shifting elements, at the cost of sequential access and additional memory for pointers.

## Pattern Characteristics

- **When to use**: Problems involving frequent insertions/deletions at arbitrary positions; implementing stacks, queues, or LRU caches; when dynamic sizing is crucial and random access is not needed; problems requiring in-place list manipulation or reversal.
- **Advantages**: O(1) time for insertions/deletions at known positions; dynamic memory allocation without reallocation overhead; efficient list splitting and merging.
- **Common variations**:
  - Singly linked list (forward traversal only, minimal memory)
  - Doubly linked list (bidirectional traversal, previous/next pointers)
  - Circular linked list (tail connects to head for cyclic operations)

## Problems (Book Order)

### 1. Linked List Reversal ([linked_list_reversal.py](linked_list_reversal.py))

Reverse a singly linked list.

### 2.
