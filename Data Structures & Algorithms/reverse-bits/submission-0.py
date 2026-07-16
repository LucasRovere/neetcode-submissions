class Solution:
    def reverseBits(self, n: int) -> int:
        bit = 0
        reverse = 0
        while n > 0:
            if n % 2 == 1:
                reverse += 2 ** (31-bit)
            
            n = n // 2
            bit += 1
        
        return reverse
