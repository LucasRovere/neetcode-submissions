class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        inSubGraph = {}
        subGraphs = []

        for i in range(n):
            inSubGraph[i] = i
            subGraphs.append(set([i]))

        counter = n

        for edge in edges:
            nodeA = edge[0]
            nodeB = edge[1]

            if inSubGraph[nodeA] != inSubGraph[nodeB]:
                minSubGraph = min(inSubGraph[nodeA], inSubGraph[nodeB])
                maxSubGraph = max(inSubGraph[nodeA], inSubGraph[nodeB])

                for node in subGraphs[maxSubGraph]:
                    inSubGraph[node] = minSubGraph
                    subGraphs[minSubGraph].add(node)

                counter -= 1

        return counter
