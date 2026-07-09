# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def rec(node):
            if not node:
                return 0

            maxRightPath = rec(node.right)
            maxLeftPath = rec(node.left)

            pathMax = max(node.val, node.val + maxRightPath, node.val + maxLeftPath)
            localMax = max(pathMax, node.val + maxRightPath + maxLeftPath)

            if localMax > self.max:
                self.max = localMax
            
            return pathMax

        rec(root)

        return self.max


#  -15
#  10  20
# X X 15 5
#   -5 -6
