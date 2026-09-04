# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import defaultdict

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        frequencies = defaultdict(int)

        current = head
        while current:
            frequencies[current.val] += 1
            current = current.next

        dummy = prev = current = ListNode(0, head)
        current = current.next
        while current:
            if frequencies[current.val] > 1:
                prev.next = current.next
            else:
                prev = current
            current = current.next

        return dummy.next