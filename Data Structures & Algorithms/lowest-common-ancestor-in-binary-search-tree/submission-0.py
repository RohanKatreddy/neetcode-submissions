# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.memo = {}

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if not node: continue

            leftCheck = self.DoesTreeContain(node.left, p) and self.DoesTreeContain(node.right, q)
            rightCheck = self.DoesTreeContain(node.right, p) and self.DoesTreeContain(node.left, q)

            if (leftCheck or rightCheck) or (node.val == p.val and (self.DoesTreeContain(node.left, q) or self.DoesTreeContain(node.right, q))) or (node.val == q.val and (self.DoesTreeContain(node.left, p) or self.DoesTreeContain(node.right, p))): return node


            queue.append(node.left)
            queue.append(node.right)

        
    
    def DoesTreeContain(self, node, target):
        if not node: return False
        if node.val == target.val:
            return True

        if (node.val, target.val) in self.memo: return self.memo[(node.val, target.val)]

        self.memo[(node.val, target.val)] = self.DoesTreeContain(node.left, target) or self.DoesTreeContain(node.right, target)

        return self.memo[(node.val, target.val)]