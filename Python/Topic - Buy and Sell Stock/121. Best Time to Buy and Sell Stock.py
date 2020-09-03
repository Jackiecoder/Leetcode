class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find one pair of (prices[i], prices[j]), that i < j. and have maximum different
        # Time O(n), Space O(1)
        buy = float('inf')
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - buy)
            buy = min(buy, price)
        return max_profit
