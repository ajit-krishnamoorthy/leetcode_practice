# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        listDict = {}
        while head:
            if head in listDict:
                return True
            listDict[head] = 1
            head = head.next
        return False