class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brute force - nested loop
        # length_of_LIS = [1] * n --> if subsequence use nums[i] as ending, the length of LIS is k
        # e.g.
        # [10,9,2,5,3,7,101,18]
        # [1 ,1, 1, 1, 1, 1, 1, 1]
        # i = 0 -> ls[0] = 1
        # i = 1 -> ls[1] = 1
        # i = 2 -> ls[2] = 1
        # i = 3 -> ls[3] = 2
        # ls[4] -> 2
        # ls[5] -> 3
        # ...
        # dp[i] = max(dp[j] + 1: dp[j] )
        # time O(n ** 2), space O(n)
        # code :
        # . .....

        # DP + binary search
        # tail[i] = k --> when length is i, k is the smallest tail.
        # i = 0, tail[1] = 10
        # i = 1, tail[1] = 9
        # i = 2, tail[1] = 2
        # i = 3, tail[2] = 5
        # i = 4, tail[2] = 3
        # ...
        # for any i < j, we will have tail[i] < tail[j]
        # so, when we want to update A[4] = 3, if we can find tail[i] < A[4] <= tail[j], then tail[j] = A[4].
        # which means we need to find the largest smaller of A[4]
        # if there is not any largest smaller of A[4], tail will append A[4]
        tail = [-float('INFINITY')]
        for i, num in enumerate(nums):
            if num > tail[-1]:
                tail.append(num)
            else:
                left, right = 0, len(tail) - 1
                while left + 1 < right:
                    mid = (left + right) // 2
                    if tail[mid] < num:
                        left = mid
                    else:
                        right = mid
                if tail[right] < num:
                    tail[right + 1] = num
                else:
                    tail[left + 1] = num
        return len(tail) - 1
