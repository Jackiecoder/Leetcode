class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # ---- brute force ----
        # travel through all value, and find how long will the arithmetic sequence will be
        # time : O(N ** 2)

        # ------  dp  -------
        # because there are repeated calculation, thus can use memo to avoid them.
        # dp[i] = T / F --> A[i + 1] - A[i] == A[i] - A[i - 1]
        # time O(N)

        # if not A or len(A) <= 2:
        #     return 0
        # n = len(A)
        # dp = [False] * n
        # for i in range(1, n - 1):
        #     dp[i] = A[i + 1] - A[i] == A[i] - A[i - 1]
        # count, res = 0, 0
        # for i in range(n):
        #     if dp[i]:
        #         count += 1
        #     else:
        #         if count > 0:
        #             res += count * (count + 1) // 2
        #             count = 0
        # return res

        # ---- 思路是对的，但是可以用更加简介的方法: ----
        if not A or len(A) <= 2:
            return 0
        n = len(A)
        cur, summ = 0, 0
        for i in range(1, n - 1):
            if A[i + 1] - A[i] == A[i] - A[i - 1]:
                cur += 1
                summ += cur
            else:
                cur = 0
        return summ


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # find the length of longest arithmetic slices
        # for each A[i] -> find out if A[i] - A[i - 1] == A[i + 1] - A[i]
        #   if true: length += 1
        #   else:   length = 2

        # max_length = 2
        cur_length = 2
        res = 0
        for index in range(1, len(A) - 1):
            if A[index] - A[index - 1] == A[index + 1] - A[index]:
                cur_length += 1
                # max_length = max(max_length, cur_length)
            else:
                res += (1 + (cur_length - 2)) * (cur_length - 2) // 2
                cur_length = 2
        res += (1 + (cur_length - 2)) * (cur_length - 2) // 2
        return res
