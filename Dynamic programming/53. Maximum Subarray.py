class Solution:
    def maxSubArray_dp(self, nums: List[int]) -> int:
        # dp
        # dp[i] = k -> the maximum sum of subarray ends with nums[i]
        # dp[i] = nums[i - 1] + (dp[i - 1] if dp[i - 1] > 0 else 0)
        # Time O(n), Space O(n)
        dp = [None] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
        return max(dp)
