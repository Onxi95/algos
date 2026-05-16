/**
 * Definition for singly-linked list.
d
 */

class Solution {
    fun reorderList(head: ListNode?): Unit {

        var slow: ListNode? = head
        var fast: ListNode? = head?.next

        while (fast != null && fast.next != null) {
            slow = slow?.next
            fast = fast?.next?.next
        }

        val second = slow?.next
        slow?.next = null

        var previous: ListNode? = null
        var current = second

        while (current != null) {
            var tmp = current.next
            current.next = previous
            previous = current
            current = tmp
        }

        var firstList: ListNode? = head
        var secondList: ListNode? = previous

        while (firstList != null && secondList != null) {
            val tmp1 = firstList.next
            val tmp2 = secondList.next

            firstList.next = secondList
            secondList.next = tmp1

            firstList = tmp1
            secondList = tmp2
        }
    }
}
