class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = [0] * n
        trusts = [0] * n

        for t in trust:
            trusted_by[t[1]-1] += 1
            trusts[t[0]-1] += 1
        
        for i in range(n):
            if trusted_by[i] == n-1 and trusts[i] == 0:
                return i+1
        
        return -1
        