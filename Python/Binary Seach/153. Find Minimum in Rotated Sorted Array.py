class Solution:
    def findMin(self, nums: List[int]) -> int:
        # -> find the head of original sorted array
        # use binary search
        # the starter must be on the left side, when
        # 1. nums[l] < nums[r]
        # 2. nums[l] > nums[r] and nums[mid] < nums[r]

        # time O(logn), space O(1)

        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[l] < nums[r] or (nums[l] > nums[r] and nums[mid] < nums[r]):
                r = mid
            else:
                l = mid
        return min(nums[l], nums[r])
