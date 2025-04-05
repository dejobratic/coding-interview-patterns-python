from list_node import ListNode

class LinkedList:
    def __init__(self, head: ListNode):
        self._head = head

    def add(node: ListNode, index: int)
        return

    def remove(index: int):
        return

    def print(self, label: str = None):
        current = self

        if label:
            print(label, end = '')
        
        while current is not None:
            print(f'{current.value}{" -> " if current.next is not None else ""}', end = '')
            current = current.next
        
        print()