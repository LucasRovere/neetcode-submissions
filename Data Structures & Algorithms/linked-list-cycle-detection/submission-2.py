# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        seen = set([head.next])

        while head.next:
            head = head.next
            if head.next in seen:
                return True
            
            seen.add(head.next)

        return False
        