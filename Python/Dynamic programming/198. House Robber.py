class Solution:
    def rob(self, A: List[int]) -> int:
        # each 4 house
        # 0 0 0 0
        # 1 0 1 0 or 0 1 0 1
        # 1 0 0 1

        # eg. [2,7,9,3,1]
        # len = 1 -> money = A[0] = 2
        # len = 2 -> money = max(A[0], A[1]) = A[1] = 7
        # len = 3 -> money = max(A[1], A[2] + max money when reach A[0](len = 1) )
        # len = 4 -> money = max(A[3] + max(max money when reach len 2, max money when reach len 1), max money when reach len = 3)

        # dp[i] = k represents max money is k when reach len = i
        # when reach dp[i], the robber must decide rob A[i - 1]
        # dp[1] = A[0]
        # dp[2] = max(A[0], A[1])
        # dp[3] = max(A[2] + dp[1], A[1])
        # dp[4] = max(dp[3], max(dp[1], dp[2]) + A[3])
        # ...
        # dp[i] = max(dp[i - 1], max(dp[i - 3], dp[i - 2]) + A[i - 1])  [i >= 4]
        if not A:
            return 0
        n = len(A)
        if n <= 2:
            return max(A)
        dp = [0] * (n + 1)
        dp[1] = A[0]
        dp[2] = max(A[1], A[0])
        for i in range(3, n + 1):
            dp[i] = max(dp[i - 1], max(dp[i - 3], dp[i - 2]) + A[i - 1])
        return dp[-1]
