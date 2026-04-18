/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
    fun removeNthFromEnd(head: ListNode?, n: Int): ListNode? {
        val result = ListNode(0)
        result.next = head

        var ptr1: ListNode? = result
        var ptr2: ListNode? = head

        for(i in 0 until n) {
            ptr2 = ptr2?.next
        }

        while(ptr2 != null) {
            ptr2 = ptr2?.next
            ptr1 = ptr1?.next
        }

        ptr1?.next = ptr1?.next?.next

        return result?.next
    }
}
