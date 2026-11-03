# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        self.best = 0

        def _diameter(root):
            if not root: return 0
            l, r = _diameter(root.left), _diameter(root.right)
            self.best = max(self.best, l + r)
            return max(l, r) + 1

        _diameter(root)

        return self.best