class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Time O(n)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        return

    def rotate_kTimes(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. brute force
        #   rotate k times
        # Time O(kn), space O(1)
        if k == 0:
            return
        nums[:] = [nums[-1]] + nums[:-1]
        return self.rotate(nums, k - 1)
