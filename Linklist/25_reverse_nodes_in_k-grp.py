# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        grpPrev = dummy
        while True:
            kth = grpPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            grpNext = kth.next
            prev = grpNext
            curr = grpPrev.next
            while curr != grpNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = grpPrev.next
            grpPrev.next = kth
            grpPrev = temp