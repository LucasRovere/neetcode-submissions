class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        return len(nums) > len(seen)
        