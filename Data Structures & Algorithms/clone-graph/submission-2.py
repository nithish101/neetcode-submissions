"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}

        def clone(node):
            if not node:
                return node
            if node in cloneMap:
                return cloneMap[node]
            newNode = Node(node.val)
            cloneMap[node] = newNode
            for nei in node.neighbors:
                newNode.neighbors.append(clone(nei))
            return newNode

        return clone(node)