class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ways = { 0: 1 }
        for i in range(len(nums)):
            newWays = defaultdict(int)
            for way in ways:
                add = way + nums[i]
                sub = way - nums[i]

                newWays[add] += ways[way]
                newWays[sub] += ways[way]

            ways = newWays

        return ways[target]


        # memo = {}
        # def rec(curr, nums):
        #     if not nums:
        #         if curr == target:
        #             return 1
        #         else:
        #             return 0

        #     tpl = tuple(nums + [curr])
        #     if tpl in memo:
        #         return memo[tpl]
            
        #     num = nums[0]
        #     ways = rec(curr + num, nums[1:]) + rec(curr - num, nums[1:])
        #     memo[tpl] = ways

        #     return ways

        # return rec(0, nums)
        