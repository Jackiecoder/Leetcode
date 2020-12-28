class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # classic binary search problem
        # 1. l < mid < r
        #   l <= t < mid -> r = mid
        #   mid < t < r -> l = mid
        # 2. l < mid, r < mid
        #   l <= t < mid -> r = mid
        #   else:   -> l = mid
        # 3. mid < l, mid < r
        #   mid < t < r -> l = mid
        #   else    -> r = mid
        # Time O(logn), space O(1)
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[l] < nums[mid]:
                if nums[l] <= target and target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] < target and target <= nums[r]:
                    l = mid
                else:
                    r = mid
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
