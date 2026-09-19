# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reverse(node: Optional[ListNode]):
            prev = None
            current = node
            while current:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp
            return prev

        max_twin = 0
        first = head
        second = reverse(slow)

        while first and second:
            twin_sum = first.val + second.val
            max_twin = max(twin_sum, max_twin)
            first = first.next
            second = second.next

        return max_twin