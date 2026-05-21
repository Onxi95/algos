/**
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */

class Solution {
    fun maxDepth(root: TreeNode?): Int {
        if (root == null) return 0

        val stack = ArrayDeque(listOf(Pair(root, 1)))
        var maxSize = 1

        while (stack.isNotEmpty()) {
            val (node, level) = stack.removeLast()
            maxSize = max(level, maxSize)
            
            node?.left?.let { stack.add(Pair(it, level + 1)) }
            node?.right?.let { stack.add(Pair(it, level + 1) )}
        }

        return maxSize
    }
}
