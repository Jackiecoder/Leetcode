class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # dp with space optimize
        if not prices:
            return 0
        n = len(prices)
        if k >= n // 2:
            res = 0
            for i in range(1, n):
                res += max(0, prices[i] - prices[i - 1])
            return res
        # swap two loops and rolling array
        dp = [[0] * (k + 1) for _ in range(2)]
        min_cost = [prices[0]] * (k + 1)
        for i in range(1, n):
            for times in range(1, k + 1):
                min_cost[times] = min(
                    min_cost[times], prices[i] - dp[(i - 1) % 2][times - 1])
                dp[i % 2][times] = max(
                    dp[(i - 1) % 2][times], prices[i] - min_cost[times])
        return dp[(n - 1) % 2][k]

    def maxProfit_dp(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        if k >= n // 2:
            res = 0
            for i in range(1, n):
                res += max(0, prices[i] - prices[i - 1])
            return res
        dp = [[0] * n for _ in range(k + 1)]
        # dp[k][i] -> max profit utill day i, with k times transaction. prices[:i]
        for times in range(1, k + 1):
            min_cost = prices[0]
            for i in range(1, n):
                min_cost = min(min_cost, prices[i] - dp[times - 1][i - 1])
                dp[times][i] = max(dp[times][i - 1], prices[i] - min_cost)
        return dp[-1][-1]
