class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp
        # dp[i,j] -> max square with matrix[i][j] as bottom right conner
        # dp[i,j] = min(dp[i - 1, j], dp[i, j - 1], dp[i - 1, j - 1]) + 1
        # use max_length to record max square length
        # Time O(mn), space O(mn)
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_length = 0
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                max_length = 1
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] == 1:
                max_length = 1
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                               dp[i - 1][j - 1]) + 1
                max_length = max(max_length, dp[i][j])
        return max_length ** 2
