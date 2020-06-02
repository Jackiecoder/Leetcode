class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # time O(mn), space O(mn)
        # dp = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     dp[i][0] = 1
        # for j in range(n):
        #     dp[0][j] = 1
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # return dp[-1][-1]

        # follow up: optimize space
        # time O(mn), space O(n)
        dp = [[1] * n for _ in range(2)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i % 2][j] = dp[i % 2 - 1][j] + dp[i % 2][j - 1]
        return dp[m % 2 - 1][-1]
