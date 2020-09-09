class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 1.  brutal force
        # for each nums[i] compare nums[i - 1] and nums[i + 1]
        # Time O(n), space O(1)

        # 2.  binary search
        # for each mid,
        #  if we have nums[mid] < nums[mid + 1] -> peak on right part
        #  elif we have nums[mid] < nums[mid - 1] -> peak on left part
        # Time O(logn), space O(1)
        nums = [-float('inf')] + nums + [-float('inf')]
        l, r = 1, len(nums) - 2
        while l + 1 < r:
            mid = (l + r) // 2
            if nums[mid] < nums[mid + 1]:
                l = mid
            elif nums[mid] < nums[mid - 1]:
                r = mid
            else:
                return mid - 1
        if nums[l] > nums[l + 1] and nums[l] > nums[l - 1]:
            return l - 1
        if nums[r] > nums[r + 1] and nums[r] > nums[r - 1]:
            return r - 1
        return -1
