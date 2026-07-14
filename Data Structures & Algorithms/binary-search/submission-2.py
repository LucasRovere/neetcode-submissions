class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = (l + r) // 2

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                r = mid
            else:
                if l == mid:
                    l = mid = r
                else:
                    l = mid

            if l == r:
                break

        if nums[mid] == target:
            return mid
        else:
            return -1  
        