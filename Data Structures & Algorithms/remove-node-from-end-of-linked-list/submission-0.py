# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# [1,2,3,4,5,6,7], 3
#          ^
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        faster = head
        slower = head

        for _ in range(n):
            faster = faster.next

        if not faster:
            return head.next

        while faster.next:
            slower = slower.next
            faster = faster.next

        slower.next = slower.next.next

        return head