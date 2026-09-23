class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = {}
        for edge in edges:
            if edge[0] not in parents and edge[1] not in parents:
                parents[edge[0]] = edge[0]
                parents[edge[1]] = edge[0]
            elif edge[0] in parents and edge[1] not in parents:
                parents[edge[1]] = parents[edge[0]]
            elif edge[0] not in parents and edge[1] in parents:
                parents[edge[0]] = parents[edge[1]]
            elif parents[edge[0]] != parents[edge[1]]:
                old_parent = parents[edge[1]]
                for node, parent in parents.items():
                    if parent == old_parent:
                        parents[node] = parents[edge[0]]
            else:
                return edge
