class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 1. O(nlogn) Solution
        #  record sums[i] = sum(nums[:i])
        #  for each sum[i], use binary search to find (sum[i] + s)
        # Time O(nlogn), space O(n)

        # 2. O(n) Solution
        #   sliding windows
        #   l, r start from 0, 0
        #   if sum < target: r += 1
        #   else: l += 1
        # Time O(n), space O(1)
        if not nums or sum(nums) < s:
            return 0
        l = r = 0
        cur_sum = nums[0]  # sum of nums[l] -> nums[r], inclusive
        min_len = float('inf')
        while r < len(nums):
            while cur_sum >= s:
                min_len = min(min_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1
            # cur_sum < s:
            r += 1
            if r < len(nums):
                cur_sum += nums[r]
        while cur_sum >= s:
            min_len = min(min_sum, r - l + 1)
            cur_sum -= nums[l]
            l += 1
        return min_len
