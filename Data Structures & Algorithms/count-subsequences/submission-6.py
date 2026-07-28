class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def dfs(iS, iT):
            if (iS, iT) in cache:
                return cache[(iS, iT)]

            if s[iS] != t[iT]:
                cache[(iS, iT)] = 0
                return 0
            
            if iT == len(t) - 1:
                cache[(iS, iT)] = 1
                return 1

            total = 0
            for i in range(iS+1, len(s)):
                total += dfs(i, iT+1)

            cache[(iS, iT)] = total
            return total

        total = 0
        for i in range(0, len(s)-len(t)+1):
            total += dfs(i, 0)

        return total
        