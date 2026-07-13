# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        nextQ = deque()

        currentLevel = 0
        result = [[]]

        hasNextLevel = True
        while q:
            node = q.popleft()
            
            if node:
                result[currentLevel].append(node.val)
                nextQ.append(node.left)
                nextQ.append(node.right)
                hasNextLevel = True
            else:
                nextQ.append(None)

            if not q and hasNextLevel:
                q = nextQ
                nextQ = deque()
                result.append([])
                currentLevel += 1
                hasNextLevel = False

        return result[:-1]
            