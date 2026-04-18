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
        val queue = ArrayDeque<TreeNode>()

        root?.let { queue.add(it) }

        while (queue.isNotEmpty()) {
            val inner = mutableListOf<Int>()
            val levelSize = queue.size
            repeat(levelSize) { i ->
                val current = queue.removeFirst()
                if (i == levelSize - 1) {
                    result.add(current.`val`)
                }
                current.left?.let { queue.add(it) }
                current.right?.let { queue.add(it) }
            }
        }

        return result
    }
}
