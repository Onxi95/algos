/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun invertTree(root: TreeNode?): TreeNode? {
        if(root == null) {
            return root
        }
        root.left = root.right.also {
            root.right = root.left
        }

        invertTree(root.left)
        invertTree(root.right)

        return root
    }
}
