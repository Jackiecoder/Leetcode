class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if target in lists -> return index
        # if not found return the first number that greater than it
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return l