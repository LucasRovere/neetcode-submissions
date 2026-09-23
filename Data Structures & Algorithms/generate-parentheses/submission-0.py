class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        options = ['(']

        for i in range(1, n*2):
            newOptions = []

            for option in options:
                openCount = option.count('(')
                closeCount = option.count(')')

                if openCount - closeCount < n*2 - i:
                    newOptions.append(option +  '(')
                if closeCount < openCount:
                    newOptions.append(option +  ')')

            options = newOptions

        return options
