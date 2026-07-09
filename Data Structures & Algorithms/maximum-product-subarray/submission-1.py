class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        maxPositive = 0
        maxAbs = 0
        curSubarray = [0, 0]
        maxSubarray = [0, 0]

        cur = nums[0]

        for i in range(1, len(nums)):
            if cur == 0:
                cur = nums[i]
            else:
                cur *= nums[i]

            if cur == 0:
                curSubarray = [i+1, i+1]
            else:
                curSubarray[1] = i
                maxPositive = max(cur, maxPositive)
                if abs(cur) > maxAbs:
                    maxAbs = abs(cur)
                    maxSubarray[0] = curSubarray[0]
                    maxSubarray[1] = curSubarray[1]

        if maxPositive == maxAbs or maxSubarray[0] == maxSubarray[1]:
            return maxPositive

        nums = nums[maxSubarray[0]:maxSubarray[1]+1]

        right = -1 * maxAbs / nums[0]
        left = nums[0]
        maxPositive = max(maxPositive, right, left)

        for i in range(1, len(nums) - 1):
            left *= nums[i]
            right /= nums[i]
            maxPositive = max(maxPositive, right, left)
        
        return int(maxPositive)
