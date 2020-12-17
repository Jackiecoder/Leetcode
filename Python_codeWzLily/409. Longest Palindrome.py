class Solution:
    def longestPalindrome(self, s: str) -> int:
        # time O(n), space O(n)
        letter_freq = Counter(s)
        res = 0
        odd = False
        for l, freq in letter_freq.items():
            res += freq // 2 * 2
            if not odd and freq % 2 == 1:
                res += 1
                odd = True
        return res
