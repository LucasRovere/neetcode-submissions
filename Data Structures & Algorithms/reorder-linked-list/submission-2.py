# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return

        fast = head
        slow = head

        while fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next

        halfPoint = slow
        newLast = halfPoint.next

        while newLast.next:
            tmp = newLast.next
            newLast.next = tmp.next
            tmp.next = halfPoint.next
            halfPoint.next = tmp

        cur = head
        while halfPoint.next:
            tmp = halfPoint.next
            halfPoint.next = halfPoint.next.next
            tmp.next = cur.next
            cur.next = tmp
            
            cur = tmp.next
