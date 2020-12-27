class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # if we only consider the array without duplicated value, this problem will be same as the 153.
        # to eliminate the duplicated value, we could move the pointer forward.
        # 1. l < mid < r -> r = mid
        # 2. mid < l, mid < r -> r = mid
        # 3. mid >= l, mid > r -> l = mid
        # in all those cases above, if any of duplicate value, move left
        # Time O(logn) -> O(n), space O(1)
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            while l + 1 < r and nums[l] == nums[l + 1]:
                l += 1
            while l + 1 < r and nums[r] == nums[r - 1]:
                r -= 1
            mid = (l + r) // 2
            if nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])
