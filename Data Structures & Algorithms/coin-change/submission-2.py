class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        result = -1
        queue = deque()
        n = len(coins)
        seen = set()

        for i in range(n):
            val = coins[n-1-i]
            queue.append((val, 1))
            seen.add(val)

            if val == amount:
                return 1

        while queue and result == -1:
            node = queue.popleft()

            for coin in coins:
                newNode = (node[0] + coin, node[1] + 1)
                if newNode[0] == amount:
                    result = newNode[1]
                    break
                elif newNode[0] < amount and newNode[0] not in seen:
                    seen.add(newNode[0])
                    queue.append(newNode)

        return result
        