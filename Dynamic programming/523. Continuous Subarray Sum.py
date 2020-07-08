class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # brute force way is ->
        # use two loop to traval through all subarrays:
        # time O(n^2), space O(1)

        # dp
        # memory the remainder of sum of nums[:i]
        # e.g. [23, 2, 4, 6, 7]
        # dp[0] = 0
        # dp[1] = 5  -> [0, 1)
        # dp[2] = 1
        # dp[3] = 5
        # dp[4] = 5
        # dp[5] = 0
        # -> dp[0] = [0, 5]
        # -> dp[1] = [2]
        # -> dp[5] = [1,3,4]
        # if len(dp[remainder]) >= 2:
        # return true
        # Time O(n), space O (n)
        if len(nums) < 2:
            return False
        if k == 0:
            count_zero = 0
            for i, num in enumerate(nums):
                if num == 0:
                    count_zero += 1
                else:
                    count_zero = 0
                if count_zero == 2:
                    return True
            return False
        dp = defaultdict(list)
        dp[0].append(0)
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            cur_sum %= k
            dp[cur_sum].append(i + 1)
            if len(dp[cur_sum]) >= 2 and dp[cur_sum][-1] - dp[cur_sum][0] >= 2:
                return True
        return False
