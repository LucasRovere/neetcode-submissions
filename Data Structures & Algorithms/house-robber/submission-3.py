class Solution:
    def rob(self, nums: List[int]) -> int:
        prevs = deque([0,0,0])
        n = len(nums)

        for i in range(n):
            best = max(prevs[-2], prevs[-3])
            prevs.append(best + nums[i])
            prevs.popleft()

        return max(prevs)
