# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map = {}
        for i, val in enumerate(inorder):
            map[val] = i

        def dfs(pl, pr, il, ir):
            if not inorder[pl:pr] or not inorder[il:ir]: return None
            root = TreeNode(preorder[pl])
            mid = map[preorder[pl]]
            size = mid - il
            root.left = dfs(pl+1, pl + size + 1, il, mid)
            root.right = dfs(pl + size + 1, pr, mid+1, ir)
            return root

        return dfs(0, len(preorder), 0, len(inorder))
