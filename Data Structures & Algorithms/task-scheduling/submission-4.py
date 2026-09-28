class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1

        maxf = max(count)
        idle = (maxf - 1) * n + maxf-1

        for i in range(25, -1, -1):
            idle -= min(maxf - 1, count[i])
        return max(0, idle) + len(tasks)
        