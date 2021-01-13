class Solution:
    def validPalindrome(self, s: str, deleted=False) -> bool:
        # Time O(n), space O(1)
        if not s:
            return True
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if deleted:
                    return False
                else:
                    return self.validPalindrome(s[l: r], deleted=True) or self.validPalindrome(s[l + 1: r + 1], deleted=True)
            l += 1
            r -= 1
        return True
