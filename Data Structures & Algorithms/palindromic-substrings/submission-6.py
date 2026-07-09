class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total = 0

        for i in range(n):
            total += self.countPalindromes(s, i)

        return total

    def countPalindromes(self, s, pos):
        n = len(s)
        count = 0
        checkOdd = True
        checkEven = pos < n - 1

        dist = min(pos+1, n-pos)

        for i in range(0, dist):
            if checkOdd and s[pos - i] == s[pos + i]:
                count += 1
            else:
                checkOdd = False

            checkEven &= (pos + 1 + i < n)

            if checkEven and s[pos - i] == s[pos + 1 + i]:
                count += 1
            else:
                checkEven = False

            if not checkOdd and not checkEven:
                break
            
        return count


# A A A