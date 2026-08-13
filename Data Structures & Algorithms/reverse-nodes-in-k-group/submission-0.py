# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr_head, next_head, last = self.reverse_ll(head, k)
        while next_head and self.has_k_nodes(next_head, k):
            c_head, n_head, l_last = self.reverse_ll(next_head, k)
            last.next = c_head
            last = l_last
            next_head = n_head
        last.next = next_head
        return curr_head

    def has_k_nodes(self, head: Optional[ListNode], k: int) -> bool:
        while head and k > 0:
            head = head.next
            k -= 1

        return k == 0
        
    def reverse_ll(self, head: Optional[ListNode], limit: int):
        current = head
        prev = None
        last = head

        while current and limit > 0:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
            limit -= 1

        return prev, current, last