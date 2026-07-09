class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.n = len(nums)
        self.nums = nums
        self.current = [0] * self.n
        self.target = target
        self.results = []

        for i in range(self.n):
            self.extendPath(i)

        return self.results

    def extendPath(self, extend):
        if extend > -1:
            self.current[extend] += 1

        sum = 0
        for i in range(self.n):
            sum += self.nums[i] * self.current[i]

        # print(self.current)
        if sum == self.target:
            result = []
            for i in range(self.n):
                for j in range(self.current[i]):
                    result.append(self.nums[i])
            
            self.results.append(result)
        elif sum < self.target:
            for i in range(extend, self.n):
                self.extendPath(i)
            
        self.current[extend] -= 1
