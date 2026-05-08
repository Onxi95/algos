class Solution {
    fun removeNthFromEnd(
        head: ListNode?,
        n: Int,
    ): ListNode? {
        val dummy = ListNode(0).apply { next = head }
        var breakPtr: ListNode? = dummy
        var current: ListNode? = dummy

        for (i in 0 until n) {
            breakPtr = breakPtr?.next
        }

        while (breakPtr?.next != null) {
            breakPtr = breakPtr?.next
            current = current?.next
        }

        current?.next = current?.next?.next

        return dummy.next
    }
}

