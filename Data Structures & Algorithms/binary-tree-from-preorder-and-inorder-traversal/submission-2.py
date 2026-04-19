# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {}
        for i, val in enumerate(inorder):
            inMap[val] = i
        
        def subtree(iL, iR, pL):
            if iL > iR:
                return None
            rootVal = preorder[pL]
            inIndex = inMap[rootVal]
            newNode = TreeNode(rootVal)
            newNode.left = subtree(iL, inIndex - 1, pL + 1)
            newNode.right = subtree(inIndex + 1, iR, pL + 1 + inIndex - iL)
            return newNode

        return subtree(0, len(preorder) - 1, 0)