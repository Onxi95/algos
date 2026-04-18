/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    fun isSameTree(p: TreeNode?, q: TreeNode?): Boolean {
        val stack = ArrayDeque<Pair<TreeNode?, TreeNode?>>()
        stack.addLast(Pair(p, q))

        while (stack.isNotEmpty()) {
            val (node1, node2) = stack.removeLast()

            if (node1 == null && node2 == null) continue
            if (node1 == null || node2 == null || node1.`val` != node2.`val`) {
                return false
            }
            stack.addLast(Pair(node1.right, node2.right))
            stack.addLast(Pair(node1.left, node2.left))
        }

        return true
    }
}