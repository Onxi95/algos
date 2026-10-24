# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()
        ptr1 = list1
        ptr2 = list2

        while ptr1 and ptr2:
            val1 = ptr1.val
            val2 = ptr2.val
            if val1 < val2:
                dummy.next = ptr1
                ptr1 = ptr1.next
            else:
                dummy.next = ptr2
                ptr2 = ptr2.next
            dummy = dummy.next
        
        dummy.next = ptr1 or ptr2

        return head.next