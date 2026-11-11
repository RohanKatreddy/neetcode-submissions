# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, mi, ma):
            if not node: return True
            if not (mi < node.val < ma): return False
            return dfs(node.left, mi, node.val) and dfs(node.right, node.val, ma)

        return dfs(root, float('-inf'), float('inf'))