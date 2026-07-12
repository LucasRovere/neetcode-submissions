class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)

        if len(t) != n:
            return False

        diff = {}

        for i in range(n):
            if s[i] not in diff:
                diff[s[i]] = 1
            else:
                diff[s[i]] += 1

            if diff[s[i]] == 0:
                del diff[s[i]]

            if t[i] not in diff:
                diff[t[i]] = -1
            else:
                diff[t[i]] -= 1

            if diff[t[i]] == 0:
                del diff[t[i]]

        return not diff
