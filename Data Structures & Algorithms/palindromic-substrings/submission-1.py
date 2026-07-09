class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total = 0

        for i in range(n):
            dist = min(i+1, n-i)
            total += self.countPalindromes(s, i, dist)

        return total

    def countPalindromes(self, s, pos, dist):
        count = 0
        checkOdd = True
        checkEven = pos < len(s) - 1

        for i in range(0, dist):
            if checkOdd and s[pos - i] == s[pos + i]:
                count += 1
            else:
                checkOdd = False

            checkEven &= (pos + 1 + i < len(s))

            if checkEven and s[pos - i] == s[pos + 1 + i]:
                count += 1
            else:
                checkEven = False

            if not checkOdd and not checkEven:
                break
            
        return count


# A A A