class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ls = []
        while x:
            ls.append(x % 10)
            x //= 10
        l, r = 0, len(ls) - 1
        while l < r:
            if ls[l] != ls[r]:
                return False
            l += 1
            r -= 1
        return True
