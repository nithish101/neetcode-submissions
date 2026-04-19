/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    int i = 0;
    Map<Integer, Integer> inHash = new HashMap<>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < preorder.length; i++) {
            inHash.put(inorder[i], i);
        }
        return helper(preorder, 0, preorder.length);
    }
    private TreeNode helper(int[] preorder, int l, int r) {
        if (r - l <= 0) {
            return null;
        }
        int headVal = preorder[i++];
        int index = inHash.get(headVal);
        TreeNode head = new TreeNode(headVal);
        head.left = helper(preorder, l, index);
        head.right = helper(preorder, index + 1, r);
        return head;
    }
}
