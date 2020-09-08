class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the only difference with leetcode 153 is whether there is any duplicates
        # In which condition, we need to set l -> mid (minimum on right side)
        #   nums[r] <= nums[l] and nums[mid] >= nums[r]:
        #
        # Time O(logn -> n), space O(1)

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            while l + 1 < r and nums[l] == nums[l + 1]:
                l += 1
            while l + 1 < r and nums[r] == nums[r - 1]:
                r -= 1
            mid = (l + r) // 2
            if nums[r] <= nums[l] and nums[mid] >= nums[r]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])
