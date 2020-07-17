class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time O(n), space O(1)
        min_price = float('INFINITY')
        profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit
