class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compls = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in compls:
                return [compls[num], i]
            else:
                compl = target - num
                compls[compl] = i
