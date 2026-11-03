# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 0
        check = head
        while check:
            check = check.next
            l += 1
        
        n = l - n
        prev = None
        iterator = head
        while n > 0:
            prev = iterator
            iterator = iterator.next
            n -= 1
            
        if prev: prev.next = iterator.next
        else: head = head.next

        return head