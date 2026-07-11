class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqAmount = [0] * numCourses
        edges = [[] for i in range(numCourses)]
        
        for after, before in prerequisites:
            prereqAmount[after] += 1
            edges[before].append(after)

        queue = deque()
        for i in range(numCourses):
            amount = prereqAmount[i]
            if amount == 0:
                queue.append(i)

        if not queue:
            return False

        coursesTaken = []
        
        while queue:
            q = queue.popleft()
            coursesTaken.append(q)
            for edge in edges[q]:
                prereqAmount[edge] -= 1
                if prereqAmount[edge] == 0:
                    queue.append(edge)

        return len(coursesTaken) == numCourses
