class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # there are two difficulty in this problem
        # 1. if num == 0:
        # 2. if num < 0
        # for condition 1. we can just compare (cur_max * num) with (cur_max)
        # for condition 2. we need another (cur_min) to store all negative result
        #     when num < 0, we can make cur_max = cur_min * num, cur_min = cur_max * num
        # return

        # *** cur_max and cur_min definition
        #   cur_max -> if current num is the tail of subarray, what is the maximum product so far.
        #   cur_min -> if current num is the tail of subarray, what is the minimum product so far.

        # Time O(n), space O(1)
        if not nums:
            return
        cur_max, cur_min = nums[0], nums[0]
        res = cur_max
        for i in range(1, len(nums)):
            num = nums[i]
            tmp_max = max(num, cur_max * num, cur_min * num)
            cur_min = min(num, cur_max * num, cur_min * num)
            cur_max = tmp_max
            res = max(cur_max, res)
        return res
