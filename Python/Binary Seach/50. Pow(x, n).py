class Solution:
    def myPow(self, x: float, n: int) -> float:
        # e.g.
        # x =   256
        # res = 4
        # n =   1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        res = 1
        while n > 1:
            print(x, res, n)
            if n % 2 == 1:
                # odd
                n -= 1
                res *= x
            else:
                # even
                x *= x
                n //= 2
        return res * x

    def myPow_recursive(self, x: float, n: int) -> float:
        # Time O(logn), space O(1)
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n % 2 == 0 and n <= 2 ** 31 - 1:
            return self.myPow(x * x, n // 2)
        else:
            return x * self.myPow(x, n - 1)
