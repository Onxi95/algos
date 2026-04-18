/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        val queue = ArrayDeque<TreeNode>()
        var level = 0
        val result = mutableListOf<List<Int>>()

        if (root != null) {
            queue.add(root)
        }

        while (queue.size > 0) {
            val size = queue.size
            var innerResult = mutableListOf<Int>()
            for (i in 0 until size) {
                val current = queue.removeFirst()
                innerResult.add(current.`val`)
                current.left?.let { queue.add(it) }
                current.right?.let { queue.add(it) }
            }
            result.add(innerResult)
            level++
        }

        return result
    }
}
