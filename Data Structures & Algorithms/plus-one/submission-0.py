class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [0] + digits
        n = len(digits)

        for i in range(n-1, -1, -1):
            result = digits[i] + 1
            if result < 10:
                digits[i] = result
                break
            else:
                digits[i] = 0

        if digits[0] == 0:
            return digits[1:]
        else:
            return digits
