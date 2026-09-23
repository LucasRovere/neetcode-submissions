class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def rec(pa, pb):
            if (pa, pb) in memo:
                return memo[(pa, pb)]

            if pa >= len(text1) or pb >= len(text2):
                return 0

            if text1[pa] == text2[pb]:
                best = 1 + rec(pa+1, pb+1)
            else:
                best = max(rec(pa+1, pb), rec(pa, pb+1), rec(pa+1, pb+1))

            memo[(pa, pb)] = best
            return best
        
        return rec(0, 0)
        