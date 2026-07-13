class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        squareSum = 0

        while squareSum != 1 and n not in seen:
            seen.add(n)
            squareSum = 0
            factor = 10

            while factor <= n*10:
                rest = (n % factor) // (factor / 10)
                squareSum += rest * rest
                factor *= 10
            
            n = squareSum

        return squareSum == 1
        