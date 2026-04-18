/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun maxDepth(root: TreeNode?, depth: Int = 0): Int {
        if(root == null) {
            return depth
        }

        val left = maxDepth(root.left, depth + 1)
        var right = maxDepth(root.right, depth + 1)

        return Math.max(left, right)
    }
}
