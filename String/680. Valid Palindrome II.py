class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.validPalindromeDeleteK(s, 1)

    def validPalindromeDeleteK(self, s, k):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                if k == 0:
                    return False
                return self.validPalindromeDeleteK(s[left + 1: right + 1], k - 1) or self.validPalindromeDeleteK(s[left: right], k - 1)
            left += 1
            right -= 1
        return True
