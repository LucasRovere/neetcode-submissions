class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        
        def dfs(current, currentSum, remaining):
            for i in range(len(remaining)):
                if i > 0 and remaining[i] == remaining[i-1]:
                    continue

                c = remaining[i]
                nextSum = currentSum + c

                if nextSum > target:
                    return
                    
                nextPath = current + [c]
                
                if nextSum == target:
                    results.append(nextPath)
                else:
                    dfs(nextPath, nextSum, remaining[i+1:])
        
        dfs([], 0, candidates)
        return results
