class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = max(dp[i - 1], dp[i - 2]) + 1
        # dp = [0, 1, 2, 3]
        if n < 0:
            return -1
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
