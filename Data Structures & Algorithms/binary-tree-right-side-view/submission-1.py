# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        current_layer = [root]
        r_view = []

        while len(current_layer) > 0:
            r_view.append(current_layer[-1].val)
            next_layer = []

            for node in current_layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)

            current_layer = next_layer
        
        return r_view
        