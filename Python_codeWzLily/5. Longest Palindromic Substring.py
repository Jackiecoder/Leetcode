class Solution:
    def longestPalindrome(self, s: str) -> str:
        # bottom up dp
        # dp[i][j] = True -> s[i: j + 1] is palindromic
        # dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        # if i == j: dp[i][j] = True
        # if i + 1 == j: dp[i][j] = s[i] == s[j]
        # Time O(n ** 2), space O(n ** 2)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = ""
        for length in range(1, n + 1):
            for i in range(n + 1 - length):
                j = i + length - 1
                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                if dp[i][j] and length > len(res):
                    res = s[i: j + 1]
        return res
