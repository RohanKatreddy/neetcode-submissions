# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1: return l2
        if not l2: return l1

        dummy = ListNode()
        outputIter = dummy

        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum // 10
            new = ListNode(sum - (carry * 10))
            outputIter.next = new
            l1 = l1.next
            l2 = l2.next
            outputIter = outputIter.next


        while l1:
            sum = l1.val + carry
            carry = sum // 10
            new = ListNode(sum - (carry * 10))
            outputIter.next = new
            l1 = l1.next
            outputIter = outputIter.next

        while l2:
            sum = l2.val + carry
            carry = sum // 10
            new = ListNode(sum - (carry * 10))
            outputIter.next = new
            l2 = l2.next
            outputIter = outputIter.next

        if carry:
            new = ListNode(1)
            outputIter.next = new

        return dummy.next