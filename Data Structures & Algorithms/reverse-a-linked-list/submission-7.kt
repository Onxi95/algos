/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun reverseList(head: ListNode?): ListNode? {
        var previous: ListNode? = null
        var current = head

        while (current != null) {
            val temp = current.next
            current.next = previous
            previous = current
            current = temp
        }

        return previous
    }
}
