class Solution:
    def numTrees(self, n: int) -> int:
        # if I choose a root value i -> [1, i - 1] + [i + 1, n]
        # divide and conquer
        # choose i from [1, n]
        #   choose j from [1, i - 1]
        #     choose k from [1, j - 1]
        #        .....
        # there will be the duplicate calculation
        #   when i = 2 -> [1] , [3, n]
        #   when i > 2, and j = 2 -> [1], [3, i - 1]
        #   so need a memory to store result in a range

        # bottom up DP
        # dp[i][j] -> all BST with [i, j]
        # dp[i][j] = sum of all k in [i, j] that has dp[i][k - 1] * dp[k + 1][j]
        # [3,10] -> [] 3 [4,10], [3] 4 [5,10],

        # n = 5 -> n = 1 n = 3, n = 2, n = 2
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]

    # def dfs(self, start, end, memo):
    #     # start and end are included
    #     if start > end:
    #         return None
    #     for i in range(start, end + 1):
    #         left = self.dfs(start, i)
    #         right = self.dfs(i + 1, end)
