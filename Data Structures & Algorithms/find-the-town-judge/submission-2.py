class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = [0] * n

        for t in trust:
            delta[t[1]-1] += 1
            delta[t[0]-1] -= 1
        
        for i in range(n):
            if delta[i] == n-1:
                return i+1
        
        return -1
        