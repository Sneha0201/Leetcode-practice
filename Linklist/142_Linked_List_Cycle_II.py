# Linked List Cycle II
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

values = list(map(int, input("Enter nums: ").split()))
head = None
tail = None
nodes = []
for value in values:
    new_node = Node(value)
    nodes.append(new_node)
    if head is None:
        head = new_node
        tail = new_node
    else:
        tail.next = new_node
        tail = new_node

pos = int(input("Enter position for cycle (-1 for no cycle): "))
if pos != -1:
    tail.next = nodes[pos]

def detectCycle(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
result = detectCycle(head)
if result is None:
    print("No cycle")
else:
    index = 0
    current = head
    while current != result:
        current = current.next
        index += 1
    print("Cycle starts at node: ", index)