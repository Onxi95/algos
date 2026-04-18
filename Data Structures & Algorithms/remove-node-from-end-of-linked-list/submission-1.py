# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0, head)
        ptr_1 = result
        ptr_2 = head

        for _ in range(n):
            ptr_2 = ptr_2.next

        while ptr_2:
            ptr_1 = ptr_1.next
            ptr_2 = ptr_2.next

        ptr_1.next = ptr_1.next.next

        return result.next