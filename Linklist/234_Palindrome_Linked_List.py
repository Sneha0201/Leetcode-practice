# Palindrome linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

values = list(map(int, input("Enter no.: ").split()))

if len(values) == 0:
    print(False)
else:
    head = Node(values[0])
    current = head
    for value in values[1: ]:
        current.next = Node(value)
        current = current.next

def isPalindrome(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        new_node = slow.next
        slow.next = prev
        prev = slow
        slow = new_node
    left = head
    right = prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next
    return True
print(isPalindrome(head))