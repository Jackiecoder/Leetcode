class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        # m * n problem --> divid into m' * n' subproblem
        # so --> dp
        # dp[i][j] = k --> the minimum of sum to (i, j)
        # for i >= 1 and j >= 1:
        #   dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + A[i][j]
        # if i ==  0 or j == 0:
        #   dp[i][0] = A[0][0] + A[1][0] + ... + A[i][0]
        #   dp[0][j] = A[0][0] + A[0][1] + ... + A[0][j]
        # return dp[-1][-1]
        # time O(mn), space O(mn)
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]
        '''

        # follow up: optimize space complexity
        # because dp row i is noly related to row i - 1, so the previous minimum sum is not necessary to memory
        # dp -> 2 * n --> dp[0][j] = k represent the minimum sum of even grid rows,
        #                 dp[1][j] = k represent the minimum sum of odd grid rows,
        # for row0 : dp[0][j] = dp[0][j - 1] + A[0][j]
        # for row i > 0:
        #   if j > 0 : dp[i % 2][j] = min(dp[i % 2 - 1][j], dp[i % 2][j - 1]) + A[i][j]
        #   if j == 0: dp[i % 2][j] = dp[i % 2 - 1][j] + A[i][j]
        # return dp[m % 2 - 1][-1]
        # time O(mn), space O(2 * n)
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[i % 2][j] = dp[i % 2 - 1][j] + grid[i][j]
                else:
                    dp[i % 2][j] = min(
                        dp[i % 2 - 1][j], dp[i % 2][j - 1]) + grid[i][j]
        return dp[m % 2 - 1][-1]
