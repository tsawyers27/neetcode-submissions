class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                continue
            sub = prices[:i]
            if prices[i] - min(sub) > profit:
                profit = prices[i] - min(sub)
        return profit