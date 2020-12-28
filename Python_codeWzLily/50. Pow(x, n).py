class Solution:
    def myPow(self, x: float, n: int) -> float:
        # two edge case:
        #   1. x = 0 -> return 0
        #   2. n < 0 -> return 1 / myPow(x, -n)
        # if n % 2 == 1:
        #   -> x * myPow(x, n - 1)
        # else:
        #   -> myPow(x ** x, n // 2)
        # Time O(logn), space O(1)
        if x == 0:
            return 0
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n // 2)
