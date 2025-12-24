from list_node import ListNode
from conftest import to_list
from linked_list_reversal import reverse_linked_list


class TestLinkedListReversal:
    def test_empty_list(self):
        # arrange
        head: ListNode | None = None

        # act
        actual = reverse_linked_list(head)  # type: ignore

        # assert
        assert actual == head

    def test_single_node_list(self):
        # arrange
        head = ListNode(1)

        # act
        actual = reverse_linked_list(head)

        # assert
        assert actual == head

    def test_two_node_list(self):
        # arrange
        head = ListNode(1, ListNode(2))

        # act
        actual = reverse_linked_list(head)

        # assert
        assert to_list(actual) == [2, 1]

    def test_linked_list(self):
        # arrange
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

        # act
        actual = reverse_linked_list(head)

        # assert
        assert to_list(actual) == [5, 4, 3, 2, 1]
