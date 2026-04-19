"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {} # maps original node to new node

        if not node:
            return node

        def dfs(node):
            if node in visited:
                return visited[node] # returns copy of node
            newNode = Node(node.val, None)
            visited[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode

        return dfs(node)