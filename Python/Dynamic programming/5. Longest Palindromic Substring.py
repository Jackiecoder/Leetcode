class Solution:
    def longestPalindrome(self, s: str) -> str:
        # bottom-up dp
        # dp[i][j] = k -> the length of longest palindromic subsequence
        # dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        # initialize dp[i][j] = False
        # Time O(n ^ 2), Space O(n ^ 2)
        if not s:
            return ''
        res = ''
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n + 1 - length):
                # j = i + length - 1 < n -> i < n + 1 - length
                j = i + length - 1
                if length == 1:
                    dp[i][j] = True
                elif length == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
                if dp[i][j]:
                    res = s[i: j + 1]
        return res

    def longestPalindrome_reversedTwoPointer(self, s: str) -> str:
        # reversed two pointers
        # Time O(n ^ 2), Space O(1)
        res = ''
        max_length = 0
        for i in range(len(s)):
            res = self.checkPalindrome(s, i, i, max_length, res)
            if i < len(s) - 1 and s[i] == s[i + 1]:
                res = self.checkPalindrome(s, i, i + 1, max_length, res)
        return res

    def checkPalindrome(self, s, start, end, max_length, res):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        if end - start - 1 > len(res):
            return s[start + 1: end]
        return res
