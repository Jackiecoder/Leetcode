class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1. find the last element that smaller than target
        #    the next element -> is target, store index, else -1
        # 2. find the first element that greater than target
        #    the prev element -> is target, store index, else -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        first = l

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        second = r

        if first > second:
            return [-1, -1]
        return [first, second]
