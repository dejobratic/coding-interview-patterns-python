from typing import Any
from list_node import ListNode
from linked_list_reversal import reverse_linked_list


def to_list(obj: Any) -> list[Any]:
    if obj is None:
        return []

    if hasattr(obj, 'val') and hasattr(obj, 'next'):
        def iterate_nodes():
            current = obj
            while current:
                yield current.val
                current = current.next

        return list(iterate_nodes())

    return obj if isinstance(obj, list) else list(obj)  # type: ignore


def test_empty_list():
    # arrange
    head: ListNode | None = None

    # act
    actual = reverse_linked_list(head)  # type: ignore

    # assert
    assert actual == head


def test_single_node_list():
    # arrange
    head = ListNode(1)

    # act
    actual = reverse_linked_list(head)

    # assert
    assert actual == head


def test_two_node_list():
    # arrange
    head = ListNode(1, ListNode(2))

    # act
    actual = reverse_linked_list(head)

    # assert
    assert to_list(actual) == [2, 1]


def test_linked_list():
    # arrange
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    # act
    actual = reverse_linked_list(head)

    # assert
    assert to_list(actual) == [5, 4, 3, 2, 1]
