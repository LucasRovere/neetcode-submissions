class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False

        half = total/2
        all_sums = set([0])

        for num in nums[1:]:
            new_sums = set()

            for s in all_sums:
                new_sum = s + num

                if new_sum == half:
                    return True
                elif new_sum < half:
                    new_sums.add(new_sum)

            all_sums = all_sums.union(new_sums)

        return False
        