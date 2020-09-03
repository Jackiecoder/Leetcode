class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        if k >= n / 2:
            max_profit = 0
            for i in range(1, n):
                max_profit += max(0, prices[i] - prices[i - 1])
            return max_profit

        dp = [[0] * n for _ in range(k + 1)]
        # dp[i][j] -> the max profit of doing at most i times transaction within day 0 to day j
        # dp[i][j] = max of ( max(dp[i - 1][k] + prices[j] - prices[k], k is [0, j)), dp[i - 1][j], dp[i][j - 1])
        for i in range(1, k + 1):
            local_max = 0
            for j in range(1, n):
                local_max = max(local_max + prices[j] - prices[j - 1], dp[i - 1]
                                [j - 1] + prices[j] - prices[j - 1], dp[i - 1][j - 1])
                dp[i][j] = max(dp[i][j - 1], local_max)
        return dp[-1][-1]
