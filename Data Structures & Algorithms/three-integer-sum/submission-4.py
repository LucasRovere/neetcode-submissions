class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        fixed = 0
        result = []
        n = len(nums)

        while fixed < n - 2 and nums[fixed] <= 0:
            l = fixed + 1
            r = n - 1

            while l < r and nums[r] >= 0:
                val = nums[fixed] + nums[l] + nums[r]
                if val == 0:
                    result.append([nums[fixed], nums[l], nums[r]])

                if val >= 0:
                    last = nums[r]
                    while nums[r] == last and l < r:
                        r -= 1
                if val <= 0:
                    last = nums[l]
                    while nums[l] == last and l < r:
                        l += 1

            last = nums[fixed]
            while fixed < n and nums[fixed] == last:
                fixed += 1

        return result
