class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        notSeen = set(range(len(nums) + 1))
        for num in nums:
            notSeen.remove(num)
        
        return notSeen.pop()
