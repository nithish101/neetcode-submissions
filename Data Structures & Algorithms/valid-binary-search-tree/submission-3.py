# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkSubtree(node, minimum, maximum):
            if not node:
                return True
            if node.val <= minimum or node.val >= maximum:
                return False
            return checkSubtree(node.left, minimum, node.val) and checkSubtree(node.right, node.val, maximum)

        return checkSubtree(root, -1 * float('inf'), float('inf'))