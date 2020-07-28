class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # this problem can be splited into the subproblem ->
        #   result of root = result of left_subtree + result of right_subtree + product of root.
        #   assume [0, i] leaf are belonged to left subtree
        #       and [i + 1, n - 1] left nodes are belonged to the right subtree
        #    result of left_subtree = mctFromLeafValues(arr[:i+1])
        #    result of right_subtree = mctFromLeafValues(arr[i+1: n - 1])
        #    product = max(arr[:i+1]) * max(arr[i+1: -1])
        #   the i in [0, n - 1], and we find the i which gets the minimum result

        # -> dp[i][j] -> min sum of all nodes except left nodes, and the leaf in arr[i, j]
        #   dp[i][j] -> k in [i, j] -> dp[i][j] = min(dp[i][k] + dp[k + 1][j] + max(arr[i: k + 1]) * max(arr[k + 1: j + 1]))

        # 1. dp[i][j] -> min sum of all nodes except left nodes, and the leaf in arr[i, j]
        #   i -> [0, n),  j -> [i, n)
        #   dp[i][i] -> only one left node, dp[i][i] = 0

        # 2. dp[i][j] = dp[i][k] + dp[k+1][j] + max(arr[i:k+1]) * max(arr[k+1:j+1])
        #   k -> [i, j - 1]

        # initial dp[i][j] = float('inf')
        # return  dp[0][n - 1]
        # Time O(N ^ 3), Space O(n ^ 2)

        n = len(arr)
        dp = [[float('inf')] * n for _ in range(n)]

        for length in range(1, n + 1):
            for i in range(n + 1 - length):
                j = i + length - 1  # < n
                if length == 1:
                    dp[i][j] = 0
                    continue
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] +
                                   max(arr[i: k + 1]) * max(arr[k + 1: j + 1]))
        return dp[0][n-1]
