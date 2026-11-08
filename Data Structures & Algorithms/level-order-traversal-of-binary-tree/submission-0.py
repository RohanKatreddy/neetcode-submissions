# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.lst = []
        self.traverse(root, 0)
        return self.lst
        

    def traverse(self, node, depth):
        if not node: return
        while depth >= len(self.lst):
            self.lst.append([])
        self.lst[depth].append(node.val)
        self.traverse(node.left, depth+1)
        self.traverse(node.right, depth+1)