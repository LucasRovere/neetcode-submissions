class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mappings = { "(": 1, ")": -1, "[": 2, "]": -2, "{": 3, "}": -3 }

        if len(s) % 2 == 1 or mappings[s[0]] < 0:
            return False

        for c in s:
            val = mappings[c]
            if val > 0:
                stack.append(val)
            else:
                if len(stack) == 0 or val + stack[-1] != 0:
                    return False 
                else:
                    stack.pop()

        return len(stack) == 0
        