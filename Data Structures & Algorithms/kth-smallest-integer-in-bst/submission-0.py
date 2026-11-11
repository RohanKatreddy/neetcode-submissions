# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0

        def dfs(node):
            nonlocal counter
            if not node: return None
            left = dfs(node.left)
            if left is not None: return left
            counter += 1
            if counter == k: return node.val
            return dfs(node.right)



        return dfs(root)