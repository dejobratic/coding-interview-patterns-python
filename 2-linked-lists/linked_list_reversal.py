from list_node import ListNode

def reverse_iterative(head: ListNode) -> ListNode:
    (prev, current, next) = (None, head, None)

    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

def reverse_recursive(head: ListNode) -> ListNode:
    if (not head) or (not head.next):
        return head
    
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head
        
if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    head.print(label='original: ')

    head = reverse_iterative(head)
    head.print(label='reversed iterative: ')

    head = reverse_recursive(head)
    head.print(label='reversed recursive: ')
