class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force
        #   -> return min(nums)
        # Time O(n), space O(1)

        # binary search
        #   1. l < mid < r -> r = mid
        #   2. l > mid, r > mid -> r = mid
        #   3. l < mid, mid > r -> l = mid
        # Time O(logn), space O(1)
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[l] < nums[mid] and nums[r] < nums[mid]:
                l = mid
            else:
                r = mid
        return min(nums[l], nums[r])
