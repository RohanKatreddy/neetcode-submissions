"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping = defaultdict()
        return self._calculate(node, mapping)
        

    def _calculate(self, node, mapping):
        if not node: return None
        if node in mapping:
            return mapping[node]
        copy = Node(node.val)
        mapping[node] = copy

        if not node.neighbors:
            return copy

        new_neighbors = []
        for neighbor in node.neighbors:
            new_neighbors.append(self._calculate(neighbor, mapping))
        copy.neighbors = new_neighbors

        return copy