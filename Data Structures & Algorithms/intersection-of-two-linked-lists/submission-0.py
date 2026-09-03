# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1 = 0
        len2 = 0

        curr1 = headA
        curr2 = headB

        while curr1:
            len1 += 1
            curr1 = curr1.next

        while curr2:
            len2 += 1
            curr2 = curr2.next

        diff = abs(len1 - len2)
        if len1 > len2:
            for _ in range(diff):
                headA = headA.next
        elif len2 > len1:
            for _ in range(diff):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None
