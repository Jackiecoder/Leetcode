class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # Time O(n ** 2), space O(n ** 2)
        memo = {}
        self.dp(s, 0, len(s) - 1, memo)
        return memo[(0, len(s) - 1)] <= k

    def dp(self, s, start, end, memo):
        if start >= end:
            return 0
        if (start, end) in memo:
            return memo[(start, end)]

        k = 0
        if s[start] == s[end]:
            k = self.dp(s, start + 1, end - 1, memo)
        else:
            k = 1 + min(self.dp(s, start + 1, end, memo),
                        self.dp(s, start, end - 1, memo))
        memo[(start, end)] = k
        return k
