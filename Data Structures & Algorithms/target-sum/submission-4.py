class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def rec(curr, nums):
            if not nums:
                if curr == target:
                    return 1
                else:
                    return 0

            tpl = tuple(nums + [curr])
            if tpl in memo:
                return memo[tpl]
            
            num = nums[0]
            ways = rec(curr + num, nums[1:]) + rec(curr - num, nums[1:])
            memo[tpl] = ways

            return ways

        return rec(0, nums)
        