class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # The brutal force method is comparing each length = m substring with the needle.
        # Time O(nm), space O(1)
        if len(needle) == 0:
            return 0
        n, m = len(haystack), len(needle)
        # i + m - 1 <= n - 1
        for i in range(n - m + 1):
            if haystack[i: i + m] == needle:
                return i
        return -1
