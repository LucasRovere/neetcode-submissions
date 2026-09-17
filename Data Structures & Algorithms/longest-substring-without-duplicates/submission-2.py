class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        start_p = 0
        end_p = 1
        longest = 1
        current = 1
        seen = set(s[0])

        while end_p < len(s):
            if s[end_p] not in seen:
                seen.add(s[end_p])
                current += 1
                end_p += 1
                longest = max(longest, current)
            elif start_p == end_p:
                end_p += 1
            else:
                seen.remove(s[start_p])
                start_p += 1
                current -= 1

        return longest
