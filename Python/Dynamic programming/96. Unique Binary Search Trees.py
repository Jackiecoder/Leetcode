class Solution:
    def numTrees(self, n: int) -> int:
        # dp
        # dp[i] = k -> when n = i, there are k unique BST
        # dp[i] = sum(dp[j - 1] * dp[i - j]),  1 <= j <= i
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                # j is the root
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]

    def numTrees_dfs_memo(self, n: int) -> int:
        # divide and conquer
        # if we choose i as the root,
        #   there will be (1 -> i - 1)  (i + 1 -> n)
        return self.numSubtrees(1, n, {})

    def numSubtrees(self, start, end, memo):
        if end - start + 1 in memo:
            return memo[end - start + 1]
        # if start > end:
        #     return 0
        if start >= end:
            return 1
        res = 0
        for i in range(start, end + 1):
            left = self.numSubtrees(start, i - 1, memo)
            right = self.numSubtrees(i + 1, end, memo)
            res += left * right
        memo[end - start + 1] = res
        return res
