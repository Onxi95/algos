/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun levelOrder(root: TreeNode?): List<List<Int>> {
        if (root == null) return listOf()
        
        val result = mutableListOf<List<Int>>()
        val queue = ArrayDeque<TreeNode>(listOf(root))

        while (queue.isNotEmpty()) {
            val innerResult = mutableListOf<Int>()
            for (i in 0 until queue.size) {
                val current = queue.removeFirst()
                innerResult.add(current.`val`)
                current.left?.let { queue.add(it) }
                current.right?.let { queue.add(it) }
            }
            result.add(innerResult)
        }
        return result
    }
}
