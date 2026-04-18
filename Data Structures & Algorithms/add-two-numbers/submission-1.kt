/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        var overflow = 0
        val result = ListNode(0)
        var current: ListNode? = result

        var first = l1
        var second = l2

        while(first != null || second != null) {
            val l1val = first?.`val` ?: 0
            val l2val = second?.`val` ?: 0
            val currentTotal = l1val + l2val + overflow
            
            val withoutOverflow = currentTotal % 10
            val newOverflow = currentTotal / 10

            println("$withoutOverflow | $newOverflow")

            current?.next = ListNode(withoutOverflow)
            current = current?.next

            overflow = newOverflow

            first = first?.next
            second = second?.next
        }

        if(overflow != 0) {
            current?.next = ListNode(overflow)
        }

        return result.next
    }
}
