class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # from k to 2
        K = 2
        n = len(prices)
        if n <= 1:
            # no transaction can be done
            return 0
        if K > n / 2:
            max_profit = 0
            for i in range(1, n):
                max_profit += max(0, prices[i] - prices[i - 1])
            return max_profit

        dp = [[0] * n for _ in range(K + 1)]
        for i in range(1, K + 1):
            local_max = 0  # -> local_max is the max
            for j in range(1, n):
                profit = prices[j] - prices[j - 1]
                local_max = max(dp[i - 1][j - 1] + profit,
                                local_max + profit, dp[i - 1][j - 1])
                dp[i][j] = max(dp[i][j - 1], local_max)
        return dp[-1][-1]

    def maxProfit_two_pass(self, prices: List[int]) -> int:
        # find two price that have a greater than it
        # b1 s1 b2 s2

        if not prices:
            return 0

        # profits[i] -> the max profit of prices[: i + 1]
        profits = []
        max_profit = 0
        cur_min = prices[0]
        for price in prices:
            cur_min = min(cur_min, price)
            max_profit = max(max_profit, price - cur_min)
            profits.append(max_profit)

        total_max = 0
        max_profit = 0
        cur_max = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            cur_max = max(cur_max, prices[i])
            max_profit = max(max_profit, cur_max - prices[i])
            total_max = max(total_max, max_profit + profits[i])
        return total_max
