class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        helperSet = set(nums)
        seen = set()
        res = 1
        
        for num in nums:
            if num in seen:
                continue

            if num - 1 not in helperSet:
                curRes = 1
                i = 1
                while num + i in helperSet:
                    seen.add(num+i)
                    i += 1
                    curRes += 1
                
                res = max(res, curRes)
            
        return res
        