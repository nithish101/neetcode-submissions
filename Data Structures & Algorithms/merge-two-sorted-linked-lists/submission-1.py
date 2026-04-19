# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            res = list1
        else:
            res = list2
        curr = res
        while list1 and list2:
            if list1.val < list2.val:
                temp = list1
                list1 = list1.next
                curr.next = temp
                curr = curr.next
            else:
                temp = list2
                list2 = list2.next
                curr.next = temp
                curr = curr.next  

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return res