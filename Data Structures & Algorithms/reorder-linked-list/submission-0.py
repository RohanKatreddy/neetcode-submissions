# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return None

        stack = []
        
        temp = head
        while temp:
            stack.append(temp)
            temp = temp.next

        dummy = ListNode()
        output = dummy

        while head != stack[-1] and head != stack[-2]:
            output.next = head
            head = head.next
            output.next.next = stack[-1]
            stack.pop()
            output = output.next.next

        output.next = head
        if head != stack[-1]:
            head.next = stack[-1]
            head = stack[-1]
        head.next = None
        