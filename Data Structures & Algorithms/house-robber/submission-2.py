class Solution:
    def rob(self, nums: List[int]) -> int:
        prevs = deque([0,0,0])
        n = len(nums)

        for i in range(n):
            best = max(prevs[-2], prevs[-3])
            prevs.append(best + nums[i])
            prevs.popleft()

        return max(prevs)

# [1,2,3,4,5,1,2,3,4,5]
# 1 + 3 > 2 -> cur = 0
# 3 + 5 > 4 -> cur = 2
# 5 + 2 > 1 -> cur = 4
# 