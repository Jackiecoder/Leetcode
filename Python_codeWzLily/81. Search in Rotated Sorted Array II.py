class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # let consider without duplicated value
        # 1. l < mid < r:
        #   t < mid -> r = mid
        #   mid < t -> l = mid
        # 2. l < mid, r < mid:
        #   t < mid -> r = mid
        #   else: -> l = mid
        # 3. mid < l, mid < r:
        #   mid < t -> l = mid
        #   else: r = mid
        # conclusion:
        #   l < mid:
        #      l <= t < mid -> r = mid
        #       else: l = mid
        #   mid < l:
        #       mid < t <= r: l = mid
        #        else: r = mid
        #   l == mid:
        #       l += 1
        # Time O(logn) -> O(n), space O(1)
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            if nums[l] == nums[mid]:
                l += 1
                continue
            elif nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid
        if nums[l] == target or nums[r] == target:
            return True
        return False
