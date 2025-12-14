# Two Pointers

## Overview

Two-pointer algorithms use two indices (pointers) to traverse sequence-like data structures that have some form of predictable dynamics (e.g. sorted arrays, palindromic strings).

## Pattern Characteristics

- **When to use**: Linear data structure input (e.g. arrays, lists) with predictable structure, ordering or constraints (sorted array, palindromic strings); problems involving finding pairs, subarrays, or in-place sequence transformations.
- **Advantages**: O(1) space, efficient O(n) time
- **Common variations**:
  - Inward traversal (opposite-direction pointers)
  - Unidirectional traversal (same-direction pointers)
  - Staged traversal (sliding window)

## Problems (Book Order)

### 1. Pair Sum - Sorted ([pair_sum_sorted.py](pair_sum_sorted.py))

Return the indices of any pair of numbers in a sorted array that sum to a target value.

### 2. Triplet Sum ([triplet_sum.py](triplet_sum.py))

Return all distinct triplets [a, b, c] from an array, such that a + b + c = 0.

### 3. [Next Problem]

Coming soon...
