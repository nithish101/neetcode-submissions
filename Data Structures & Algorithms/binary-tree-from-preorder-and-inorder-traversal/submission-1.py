# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        numNodes = len(preorder) - 1
        inMap = {}
        for i, val in enumerate(inorder):
            inMap[val] = i

        def subTree(pL, iL, iR) -> TreeNode:
            if pL >= len(preorder) or iL > iR:
                return None
            newVal = preorder[pL]
            subHead = TreeNode(newVal, None, None)
            inIndex = inMap[newVal]
            # iL to inIndex - 1 and inIndex + 1 to iR
            left_len = inIndex - iL
            subHead.left = subTree(pL + 1, iL, inIndex - 1)
            subHead.right = subTree(pL + left_len + 1, inIndex + 1, iR)
            return subHead

        return subTree(0, 0, numNodes)
