class Solution:
    def integerBreak(self, n: int) -> int:
        # for any  --> 2 choices,
        # 1. number as large as possible  ->  k / 2 * k / 2 or ((k - 1) / 2) * ((k + 1) / 2)
        # 2. as many number as possible   ->  2 ^ (k / 2)  or  2 ^ ((k -  1) / 2)

        # for even k
        # k = 2 -> 1 * 1
        # k = 4 -> 2 * 2 = 2 ^ 2
        # k = 6 -> 3 * 3 > 2 ^ 3
        # ---> for even k, when k > 4, choice 1 is better
        #
        # for odd k
        # k = 1 -> 1
        # k = 3 -> same
        # k = 5 -> 6 > 4
        # k = 7 -> 12 > 8
        # ---> for odd k, when k > 5, choice 1 is better

        # 10 -> 3 * 3 * 4
        # 10 -> 3 * 7
        # 7 -> 3 * 4
        # time O(n ** 2)

        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
        return dp[-1]
