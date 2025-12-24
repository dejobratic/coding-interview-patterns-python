class ListNode:
    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f'ListNode(val={self.val!r},next={self.next!r})'
