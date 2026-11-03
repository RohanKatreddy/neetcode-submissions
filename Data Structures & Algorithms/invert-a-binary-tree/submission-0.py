# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self._invert(root)
        return root
        

    def _invert(self, root):
        if not root: return;
        temp = root.left
        root.left = root.right
        root.right = temp

        self._invert(root.left)
        self._invert(root.right)