class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force
        # select number_i as starter, and select from i to j to calculate sum
        # O(n ^ 2), space O(1)

        # memo to store calculation result
        # memo[sum]: [index]
        # for sum in memo.keys():
        #   if (sum + k) not in memo:
        #       continue
        #   else: two pointers to travel through
        # e.g. [1, 1, 0, 0, 1, 0, 1], k = 2
        # dp[1] -> sum(nums[0: 1]) = 1
        # dp = {0: [0], 1: [1], 2:[2, 3, 4], 3:[5, 6], 4:[7]}
        # key = 0,
        # find = 2
        # count = 3 + 2 + 3 = 8
        # Time O(n), space O(n)

        memo = defaultdict(int)
        memo[0] += 1
        cumulate = 0
        res = 0
        for i in range(len(nums)):
            cumulate += nums[i]
            res += memo[cumulate - k]
            memo[cumulate] += 1
        return res
