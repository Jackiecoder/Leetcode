class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # because nums[-1] = nums[n] = -infinity
        #   so there will alway exist a peak
        # 1. brute force way:
        #   travel through the list, if one number is greater than its left and right, return this index
        #   Time O(n), space O(1)
        # 2. binary search
        #   assume we have one index, and it have A[index - 1] < A[index] < A[index + 1]
        #   then we can make sure that there must be a peak on right side
        #
        # if A[index - 1] < A[index] < A[index + 1]: l = mid
        # if A[index - 1] > A[index] > A[index + 1]: r = mid
        # if A[index - 1] > A[index] < A[index + 1]: whatever
        # Time O(logn), space O(1)
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            left_val, right_val = self.get_neighbor_value(mid, nums)
            if left_val < nums[mid] and right_val < nums[mid]:
                return mid
            elif nums[mid] < right_val:
                l = mid
            else:
                r = mid
        left_val, right_val = self.get_neighbor_value(l, nums)
        if left_val < nums[l] and nums[l] > right_val:
            return l
        return r

    def get_neighbor_value(self, index, nums):
        left_val = nums[index - 1] if 0 <= index - \
            1 < len(nums) else -float('inf')
        right_val = nums[index + 1] if 0 <= index + \
            1 < len(nums) else -float('inf')
        return left_val, right_val
