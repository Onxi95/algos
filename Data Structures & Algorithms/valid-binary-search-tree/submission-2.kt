/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
fun isValidBST(root: TreeNode?): Boolean {
        return isValidSubTree(root, Long.MIN_VALUE, Long.MAX_VALUE)
    }

    private fun isValidSubTree(node: TreeNode?, min: Long, max: Long): Boolean {
        if (node == null) return true
        
        val currentVal = node.`val`.toLong()
        if (currentVal <= min || currentVal >= max) {
            return false
        }
        
        return isValidSubTree(node.left, min, currentVal) && 
               isValidSubTree(node.right, currentVal, max)
    }
}
