# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        nextP = p
        nextQ = q
        pQueue = deque()
        qQueue = deque()

        if p == None or q == None:
            if p == q:
                return True
            else:
                return False

        while nextP != None:
            if nextP.val != nextQ.val:
                return False

            leftP = nextP.left
            rightP = nextP.right

            leftQ = nextQ.left
            rightQ = nextQ.right

            if leftP != leftQ:
                if leftP == None or leftQ == None:
                    return False
                else:
                    pQueue.append(leftP)
                    qQueue.append(leftQ)
                    

            if rightP != rightQ:
                if rightP == None or rightQ == None:
                    return False
                else:
                    pQueue.append(rightP)
                    qQueue.append(rightQ)

            if len(pQueue) == 0:
                return True

            nextP = pQueue.popleft()
            nextQ = qQueue.popleft()

        return True