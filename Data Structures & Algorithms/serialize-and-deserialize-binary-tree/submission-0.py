# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tree = []
        def dfs(node):
            if not node:
                tree.append("N")
                return

            tree.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return "#".join(tree)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        def dfs(tree):
            val = tree.popleft()
            if val == "N":
                return None

            node = TreeNode(
                val,
                dfs(tree),
                dfs(tree)
            )

            return node

        tree = deque(data.split("#"))
        return dfs(tree)
