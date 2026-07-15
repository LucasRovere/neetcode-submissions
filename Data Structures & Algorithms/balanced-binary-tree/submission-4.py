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
                print("None")
                return [True, height]

            print("node:", node.val, "left")
            lBalance, lWeight = dfs(node.left, height + 1)
            print("node:", node.val, "l result", lBalance, lWeight)
            if not lBalance:
                print("node:", node.val, "Back False")
                return [False, 0]

            print("node:", node.val, "right")
            rBalance, rWeight = dfs(node.right, height + 1)
            print("node:", node.val, "r result", node.val, rBalance, rWeight)
            if not rBalance or abs(lWeight - rWeight) > 1:
                print("node:", node.val, "Back False", abs(lWeight - rWeight), lWeight, rWeight)
                return [False, 0]

            print("node:", node.val, "Back True", max(lWeight, rWeight) + 1)
            return [True, max(lWeight, rWeight)]

        return dfs(root, 0)[0]
