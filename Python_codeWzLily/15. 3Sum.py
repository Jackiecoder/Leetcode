class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time O(n ** n), space O(n)
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i - 1]:
                continue
            self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums, start, res):
        memo = set()
        first = nums[start]
        l, r = start + 1, len(nums) - 1
        while l < r:
            while l < r and l > start + 1 and nums[l] == nums[l - 1]:
                l += 1
            while l < r and r < len(nums) - 1 and nums[r] == nums[r + 1]:
                r -= 1
            if not l < r:
                break
            ssum = first + nums[l] + nums[r]
            if ssum == 0:
                res.append([first, nums[l], nums[r]])
                l += 1
                r -= 1
            elif ssum < 0:
                l += 1
            else:
                r -= 1
