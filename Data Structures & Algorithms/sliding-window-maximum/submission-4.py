class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return [max(nums)]
        if k == 1:
            return nums

        begin = 0
        end = k-1
        currMax = max(nums[begin:end])
        result = []

        while end < len(nums):
            if nums[end] > currMax:
                currMax = nums[end]
            result.append(currMax)

            begin += 1
            end += 1

            if nums[begin-1] == currMax:
                currMax = max(nums[begin:end])

        return result
