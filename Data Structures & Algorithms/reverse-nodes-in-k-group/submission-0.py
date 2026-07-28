# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k < 2:
            return head

        lastNode = head
        head = ListNode(None, head)
        prevNode = head

        while lastNode:
            reverseNodes = [prevNode]
            for _ in range(k):
                if not lastNode:
                    return head.next
                
                reverseNodes.append(lastNode)
                lastNode = lastNode.next
            
            # if not reverseNodes[-1].next:
            #     reverseNodes[-1].next = ListNode(None, None)
            
            # print(list(map(lambda x: [x.val, x.next.val], reverseNodes)))
            
            reverseNodes[0].next = reverseNodes[-1]
            reverseNodes[1].next = reverseNodes[-1].next
            prevNode = reverseNodes[1]
            for i in range(0, k-1):
                reverseNodes[k-i].next = reverseNodes[k-i-1]
            
            # print(list(map(lambda x: [x.val, x.next.val], reverseNodes)))

        return head.next



# k = 3


# 1: 2
# 2: 3 
# 3: 4
# 4: 5 < last
# 5: 6

# [
#     0: 4
#     1: 3
#     2: 2
#     3: 1
# ]

# tmp => 2