# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, greatest):
            if not root:
                return 0
            new_greatest = max(greatest, root.val)
            if root.val >= greatest:
                return 1 + helper(root.left, new_greatest) + helper(root.right, new_greatest)
            return helper(root.left, new_greatest) + helper(root.right, new_greatest)
        return helper(root, -float('inf'))