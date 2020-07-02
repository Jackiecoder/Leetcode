class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """

    def winSum(self, nums, k):
        # write your code here
        # travel through the array from 0 to n - k
        # time O(n), space O(n)

        # sum(nums[0:k]),
        # last_sum - nums[0] + nums[k] i = 1
        # last_sum - nums[1] + nums[k + 1] i = 2
        # ...
        # last_sum - nums[i] + nums[k + i - 1], i from 0 to (k + i - 1 < n)
        if not nums:
            return []
        elif k >= len(nums):
            return [sum(nums)]
        n = len(nums)
        res = []
        cur = 0
        for i in range(n - k + 1):
            if i == 0:
                cur = sum(nums[:k])
                res.append(cur)
                continue
            cur = cur - nums[i - 1] + nums[k + i - 1]
            res.append(cur)
        return res
