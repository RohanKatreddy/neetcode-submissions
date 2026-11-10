# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def rev(head, k):
            prev = None
            current = head
            next = None
            while current and k:
                next = current.next
                current.next = prev
                prev = current
                current = next
                k -= 1

            return next, prev

        length = 0
        current = head
        while current and length < k:
            current = current.next
            length += 1
        
        if length < k: return head
        firstEnd = head
        nextReverse, first = rev(head, k)
        firstEnd.next = self.reverseKGroup(nextReverse, k)
        return first

