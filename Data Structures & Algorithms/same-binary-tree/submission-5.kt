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
        val stack = ArrayDeque<Pair<TreeNode?, TreeNode?>>(listOf(Pair(p, q)))

        while (stack.isNotEmpty()) {
            val (first, second) = stack.removeLast()

            if (first == null && second == null) continue
            if (first == null || second == null || first?.`val` != second.`val`) return false

            stack.add(Pair(first?.left, second?.left))
            stack.add(Pair(first?.right, second?.right))
        }
        
        return true
    }
}