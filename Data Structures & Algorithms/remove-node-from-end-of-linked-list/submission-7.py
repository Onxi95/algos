# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy
        after = dummy

        for _ in range(n):
            after = after.next

        while after.next:
            before = before.next
            after = after.next

        before.next = before.next.next

        return dummy.next