class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # The difficulty is:
        #   when val_l == val_r, we can't know it is sorted or rotated.
        #       1. nums[l: r] same -> check if val_l == target
        #       2. rotated -> do BS
        #
        #   1. if val_l < val_r -> increasing -> BS
        #   2. if val_l >= val_r
        #       2.1 if val_l == val_r -> check if val_l == target
        #       do BS
        #           l -> mid :
        #               1. val_mid >= val_l and not val_l <= target <= val_mid
        #               2. val_mid <= val_r and val_mid <= target <= val_r
        #          else -> r -> mid
        # Time average O(logn) worst O(n) , space O(1)
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:
                l += 1

            if nums[l] <= nums[mid]:
                # rotated point is after mid
                if nums[l] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                # rotated point is before mid
                if nums[mid] < target <= nums[r]:
                    l = mid
                else:
                    r = mid
        if nums[l] == target or nums[r] == target:
            return True
        return False
