# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode):
            current = node
            prev = None
            while current:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp

            return prev
        
        new_head = reverse(head)

        carry = 1

        current = new_head
        while current:
            total_val = carry + current.val
            carry = total_val // 10
            current.val = total_val % 10
            current = current.next

        new_head = reverse(new_head)

        if carry:
            tmp = new_head
            new_head = ListNode(carry, tmp)

        return new_head