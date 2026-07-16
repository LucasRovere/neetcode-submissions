# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]

            lLength, lLargest = dfs(node.left)
            rLength, rLargest = dfs(node.right)

            curLength = max(lLength, rLength) + 1
            curTotal = lLength + rLength + 1

            return [curLength, max(curTotal, lLargest, rLargest)]

        return dfs(root)[1] - 1
        