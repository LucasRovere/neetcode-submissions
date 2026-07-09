class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        norm = ord('a') - 1
        base = ord('z') - ord('a')

        for word in strs:
            eq = 0
            for c in word:
                print(ord(c) - norm)
                eq += base ** (ord(c) - norm)

            if eq not in grouped:
                grouped[eq] = [word]
            else:
                grouped[eq].append(word)

        return list(grouped.values())
