class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two pointer
        # l,r --> rightmost boundary of 0, leftmost boundary of 2
        # cur -->
        # Time O(n), space O(1)
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[l] == 0:
                l += 1
            while l < r and nums[r] == 2:
                r -= 1
            cur = l
            while cur <= r:
                if nums[cur] == 0:
                    nums[cur], nums[l] = nums[l], nums[cur]
                    l += 1
                    break
                elif nums[cur] == 2:
                    nums[cur], nums[r] = nums[r], nums[cur]
                    r -= 1
                    break
                cur += 1
            if cur > r:
                break
        return nums
