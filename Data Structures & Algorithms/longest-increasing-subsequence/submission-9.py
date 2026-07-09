class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = [nums[0]]

        for i in range(1, len(nums)):
            print(seq)
            if nums[i] > seq[-1]:
                seq.append(nums[i])
                continue

            j = len(seq) - 1
            while j > 1 and seq[j-1] >= nums[i]:
                j -= 1

            if seq[0] >= nums[i]:
                j = 0

            seq[j] = nums[i]

        return len(seq)