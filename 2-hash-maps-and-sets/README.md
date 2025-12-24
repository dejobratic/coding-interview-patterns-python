# Hash Maps and Sets

## Overview

Hash-based data structures use hash functions to enable constant-time lookups and insertions by mapping keys to specific memory locations. Hash maps (dictionaries) store key-value pairs for quick data retrieval, while hash sets track unique elements for fast membership testing. This pattern transforms problems requiring linear searches into constant-time operations.

## Pattern Characteristics

- **When to use**: Problems requiring fast lookups, duplicate detection, frequency counting, or tracking seen elements; finding pairs/complements with specific properties; validating uniqueness constraints across rows, columns, or regions.
- **Advantages**: O(1) average-case time complexity for lookups, insertions, and deletions; natural fit for counting and grouping operations.
- **Common variations**:
  - Hash map for key-value mappings (counting, indexing, caching)
  - Hash set for membership testing (seen elements, duplicates)
  - Multiple sets/maps for tracking different dimensions (rows, columns, grids)

## Problems (Book Order)

### 1. Pair Sum - Unsorted ([pair_sum_unsorted.py](pair_sum_unsorted.py))

Return the indices of any pair of numbers in an unsorted array that sum to a target value.

### 2. Verify Sudoku Board ([verify_sudoku_board.py](verify_sudoku_board.py))

Determine if a 9x9 Sudoku board's state adheres to the rules of the game.

### 3. Zero Striping ([zero_striping.py](zero_striping.py))

For each zero in an m x n matrix, set its entire row and column to zero
in place.
