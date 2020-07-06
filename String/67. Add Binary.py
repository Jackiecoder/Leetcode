class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Time O(N), SPACE O(N)

        a = list(a)
        b = list(b)
        carry = 0
        res = ''

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            res += str(carry % 2)
            carry //= 2
        return res[::-1]
