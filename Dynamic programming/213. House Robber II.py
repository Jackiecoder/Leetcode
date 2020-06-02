class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. divid into subproblem
        # [a, b, c, d, e, f, g, h]
        # if a have been robbed, h can not be robbed
        # -> [a, b, c, d, e, f, g] or [b, c, d, e, f, g, h]

        # 2. solve subproblem like house robber I
        # ...
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.line_rob(nums[:-1]), self.line_rob(nums[1:]))

    def line_rob(self, nums):
        '''
        @para: 
            nums: list, houses in a line, length >= 1
        @return:
            max money can rob in a line
        '''
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        dp[2] = max(nums[1], nums[0])
        for i in range(3, n + 1):
            dp[i] = max(nums[i - 1] + max(dp[i - 2], dp[i - 3]), dp[i - 1])
        return dp[-1]
