# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        res = lists
        while len(res) > 1:
            list1, list2 = res.pop(), res.pop()
            result = self.merge_lists(list1, list2)
            res.append(result)

        return res[0]
        
    def merge_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next

        dummy.next = list1 or list2

        return result.next