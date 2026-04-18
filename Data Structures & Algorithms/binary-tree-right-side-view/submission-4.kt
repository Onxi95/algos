/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun rightSideView(root: TreeNode?): List<Int> {
        val result = mutableListOf<Int>()
        val stack = ArrayDeque<TreeNode>()

        root?.let { stack.add(it) }

        while (stack.size > 0) {
            val inner = mutableListOf<Int>()
            for (i in 0 until stack.size) {
                val current = stack.removeFirst()
                inner.add(current.`val`)
                current.left?.let { stack.add(it) }
                current.right?.let { stack.add(it) }
            }
            if (inner.size > 0) {
                result.add(inner.last())
            }
        }

        return result
    }
}
