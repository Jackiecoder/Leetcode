class Solution:
    def convertToTitle(self, n: int) -> str:
        # 1 -> A
        # 2 -> B
        # ...
        # 26 -> 10 -> Z
        # 27 -> 11 -> AA
        res = ''
        while n:
            n -= 1
            res = chr(n % 26 + ord('A')) + res
            n //= 26
        return res
