"""
Reverse a singly linked list.

Example:
  Input:  (1) -> (2) -> (3) -> (4) -> (5)
  Output: (5) -> (4) -> (3) -> (2) -> (1)
"""

from list_node import ListNode


def reverse_linked_list(head: ListNode) -> ListNode:
    prev, cur = None, head

    while cur:
        next = cur.next
        cur.next = prev

        prev = cur
        cur = next

    return prev  # type: ignore
