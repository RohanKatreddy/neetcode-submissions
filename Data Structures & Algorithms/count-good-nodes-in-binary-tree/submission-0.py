# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root, root.val))

        result = 0
        while queue:
            node, maxSoFar = queue.popleft()
            if not node: continue
            if node.val >= maxSoFar:
                result += 1
                maxSoFar = node.val
            queue.append((node.left, maxSoFar))
            queue.append((node.right, maxSoFar))

        return result