# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next

        second = slow.next
        slow.next = None
        prev = None

        # reverse second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        second = prev

        while second:
            temp = head.next
            temp2 = second.next
            head.next = second
            second.next = temp
            head = temp
            second = temp2
