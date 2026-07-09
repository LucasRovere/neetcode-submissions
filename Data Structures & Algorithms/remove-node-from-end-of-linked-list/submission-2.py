# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        pointerA = head
        pointerB = head

        for i in range(n):
            pointerA = pointerA.next

        if not pointerA:
            return head.next
        
        while pointerA.next:
            pointerA = pointerA.next
            pointerB = pointerB.next

        pointerB.next = pointerB.next.next

        return head