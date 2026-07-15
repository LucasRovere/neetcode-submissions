# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, height):
            if not node:
                return [True, height]

            lBalance, lWeight = dfs(node.left, height + 1)
            if not lBalance:
                return [False, 0]

            rBalance, rWeight = dfs(node.right, height + 1)
            if not rBalance or abs(lWeight - rWeight) > 1:
                return [False, 0]

            return [True, max(lWeight, rWeight)]

        return dfs(root, 0)[0]
