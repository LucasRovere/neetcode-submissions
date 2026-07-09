# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        last = head
        while last.next:
            tmp = last.next
            last.next = tmp.next
            tmp.next = head
            head = tmp

        return head