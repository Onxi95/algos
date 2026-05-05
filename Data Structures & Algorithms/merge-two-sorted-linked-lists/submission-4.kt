/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        var dummy = ListNode(0)
        var current: ListNode? = dummy

        var l1 = list1
        var l2 = list2
        while (l1 != null && l2 != null) {
            val val1 = l1.`val`
            val val2 = l2.`val`

            when {
                val1 < val2 -> {
                    current?.next = ListNode(val1)
                    l1 = l1.next
                }
                else -> {
                    current?.next = ListNode(val2)
                    l2 = l2.next
                }
            }

            current = current?.next
        }

        current?.next = l1 ?: l2
        return dummy.next
    }
}
