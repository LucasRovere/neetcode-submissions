class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curMin = curMax = prices[0]
        for price in prices[1:]:
            if price < curMin:
                curMin = curMax = price
            else:
                curMax = max(curMax, price)

            profit = max(profit, curMax - curMin)

        return profit
        