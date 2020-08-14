class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # bottom-up dp
        # dp[i][j] = k -> the length of longest palindromic subsequence
        # dp[i][j] = dp[i + 1][j - 1] + 1 if s[i] == s[j] else dp[i + 1][j - 1]
        # Time O(n ^ 2), Space O(n ^ 2)
        if not s:
            return 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n + 1 - length):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
         return dp[0][-1]
        
