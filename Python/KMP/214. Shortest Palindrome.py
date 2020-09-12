class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # brutal force
        # for each s[:len]
        # compare s[:len] with s[len: 2len] and s[len: 2len + 1]
        # Time O(n^2), space O(1)
        # https://leetcode.com/problems/shortest-palindrome/discuss/60099/AC-in-288-ms-simple-brute-force

        # s     abcd
        # r.    dcba
        # r    dcba
        # r.  dcba
        # r  dcba
        if not s:
            return ''
        r = s[::-1]
        for i in range(len(s)):
            if r[i:] == s[:len(s) - i]:
                return r + s[len(s) - i:]
