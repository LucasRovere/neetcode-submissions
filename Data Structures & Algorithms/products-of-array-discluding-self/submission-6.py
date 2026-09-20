class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        partial_l = [1] * n
        partial_r = [1] * n

        for i in range(1, n):
            partial_l[i] = partial_l[i-1] * nums[i-1]
            partial_r[n-1-i] = partial_r[n-i] * nums[n-i]

        for i in range(n):
            nums[i] = partial_l[i] * partial_r[i]

        return nums
