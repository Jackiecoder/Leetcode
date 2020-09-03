class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] = the least number of perfect square numbers
        # dp[i] = dp[i - j] + dp[j] (j in [1, i - 1])
        #   if i is perfect square -> return 1
        # n = 1 -> 1
        # n = 2 -> 2
        # n = 3 -> 3
        # n = 4 -> 1
        # n = 5 -> 2, 5
        # n = 6 -> 3,
        # n = 7 -> 4
        # n = 8 -> 2
        # ...

        # --- dp ---  time O(n * sqrt(n)), space O(n)
        dp = [float('INFINITY')] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            square_root = sqrt(i)
            for j in range(1, int(sqrt(i)) + 1):
                if j == square_root:
                    dp[i] = 1
                    break
                dp[i] = min(dp[i - j ** 2] + 1, dp[i])
        return dp[-1]
