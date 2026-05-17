/**
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */

class Solution {
	fun mergeKLists(lists: Array<ListNode?>): ListNode? {
		if (lists.isEmpty()) return null

		var currentLists = lists

        for (i in 1 until currentLists.size) {
            currentLists[i] = mergeLists(currentLists[i - 1], currentLists[i])
        }
		return currentLists.last()
	}

	fun mergeLists(list1: ListNode?, list2: ListNode?): ListNode? {
		val dummy = ListNode(0)
		var current: ListNode? = dummy
		var l1 = list1
		var l2 = list2
		while (l1 != null && l2 != null) {
			val v1 = l1.`val`
			val v2 = l2.`val`

			when {
				v1 > v2 -> {
					current?.next = l2
					l2 = l2.next
				}

				else -> {
					current?.next = l1
					l1 = l1.next
				}
			}
			current = current?.next
		}
		current?.next = l1 ?: l2
		return dummy.next
	}
}
