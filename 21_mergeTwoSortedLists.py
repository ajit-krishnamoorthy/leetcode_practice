# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        retList = dummy
        while list1 and list2:
            if list1.val < list2.val:
                retList.next = list1
                list1 = list1.next
            else:
                retList.next = list2
                list2 = list2.next
            retList = retList.next
        if list1:
            retList.next = list1
        elif list2:
            retList.next = list2
        return dummy.next
