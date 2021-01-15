class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # Time O(n ** 2), space O(1)
        nums.sort()
        res = 0
        for i in range(len(nums) - 1, 1, -1):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res
