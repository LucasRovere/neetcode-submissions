class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stacks = [[nums[0]]]
        curMax = 1

        for num in nums[1:]:
            keepStacks = []
            maxAppended = []
            maxNewStack = []
            print(num)

            for stack in stacks:
                if stack[-1] < num and len(stack) >= len(maxAppended):
                    stack.append(num)
                    keepStacks.append(stack)
                    # maxAppended = stack

                    if len(stack) > curMax:
                        curMax = len(stack)
                elif stack[-1] == num and len(stack) > len(maxAppended):
                    maxAppended = stack
                elif stack[-1] > num:
                    keepStacks.append(stack)
                    newStack = stack.copy()
                    isRepeat = False
                    while newStack and newStack[-1] >= num:
                        if newStack[-1] == num:
                            isRepeat = True
                            break

                        newStack.pop()

                    if not isRepeat:
                        newStack.append(num)
                        
                        if len(newStack) > len(maxNewStack):
                            maxNewStack = newStack
            
            stacks = keepStacks
            if maxNewStack:
                stacks.append(maxNewStack)
            if maxAppended:
                stacks.append(maxAppended)

            # print(stacks)

        return curMax
