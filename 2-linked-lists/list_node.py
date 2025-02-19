class ListNode:
    def __init__(self, value: int, next: 'ListNode' = None):
        self.value = value
        self.next = next

    def print(self, label: str = None):
        current = self

        if label:
            print(label, end = '')
        
        while current is not None:
            print(f'{current.value}{" -> " if current.next is not None else ""}', end = '')
            current = current.next
        
        print()