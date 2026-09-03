# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        def reversell(head: Optional[ListNode]):
            current = head
            prev = None
            while current:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp
        
            return prev

        l1 = head
        l2 = reversell(slow)

        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return True