from list_node import ListNode

def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(-1, head)
    leader = trailer = dummy

    for _ in range(k):
        leader = leader.next

        if not leader:
            return head

    while leader.next:
        leader = leader.next
        trailer = trailer.next

    if trailer.next:
        trailer.next = trailer.next.next

    return dummy.next

if __name__ == "__main__":
    for k in range(7):
        print(f'k: {k}')

        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        head.print(label='original: ')

        head = remove_kth_last_node(head, k)
        head.print(label='removed: ')

        print()