"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        inputIter = head

        dummy = Node(inputIter.val)
        outputIter = dummy

        inputIter = inputIter.next
        
        mapping = {head: dummy}

        while inputIter:
            outputIter.next = Node(inputIter.val)

            outputIter = outputIter.next
            mapping[inputIter] = outputIter     
            inputIter = inputIter.next

        mapping[None] = None
        
        inputIter = head
        outputIter = dummy
        while inputIter:
            outputIter.random = mapping[inputIter.random]
            outputIter = outputIter.next
            inputIter = inputIter.next

        return dummy