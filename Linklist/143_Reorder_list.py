# Reorder list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

values = list(map(int, input("Enter num: ").split()))

if len(values) == 0:
    head = None
else:
    head = Node(values[0])
    current = head
    for value in values[1: ]:
        current.next = Node(value)
        current = current.next

def reorderList(head):
    if head is None or head.next is None:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = None
    prev = None
    while second:
        new_node = second.next
        second.next = prev
        prev = second
        second = new_node
    first = head
    second = prev
    while second:
        next_first = first.next
        next_second = second.next
        first.next = second
        second.next = next_first
        first = next_first
        second = next_second
    return head
head = reorderList(head)
current = head
while current:
    print(current.data, end = " ")
    current = current.next