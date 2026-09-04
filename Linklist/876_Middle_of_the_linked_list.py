# Middle of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

values = list(map(int, input("Enter num: ").split()))

head = None
tail = None
for value in values:
    new_node = Node(value)
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
middle = middleNode(head)
while middle is not None:
    print(middle.data, end = " ")
    middle = middle.next