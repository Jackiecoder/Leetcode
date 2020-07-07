class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ''
        carry = 0

        while num1 or num2 or carry:
            if num1:
                carry += int(num1[-1])
                num1 = num1[:-1]
            if num2:
                carry += int(num2[-1])
                num2 = num2[:-1]
            res += str(carry % 10)
            carry //= 10
        return res[::-1]
