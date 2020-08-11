class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) <= 1:
            return 0
        n = len(prices)
        keep = [0] * n    # max profit if keep a stock on day i
        notKeep = [0] * n  # max profit if not keep a stock on day i
        keep[0], keep[1] = -prices[0], max(-prices[0], -prices[1])
        notKeep[1] = max(0, prices[1] - prices[0])
        for i in range(2, n):
            keep[i] = max(keep[i - 1], -prices[i] + notKeep[i - 2])
            notKeep[i] = max(notKeep[i - 1], prices[i] + keep[i])
        return notKeep[-1]
