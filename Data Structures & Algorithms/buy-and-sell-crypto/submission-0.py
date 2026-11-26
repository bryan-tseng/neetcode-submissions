class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        profit = 0
        buy = prices[0]
        for price in prices[1:]:
            if price < buy:
                buy = price
            elif price > buy:
                sell = price
                profit = max(profit, sell - buy)
        return profit