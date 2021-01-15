class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                ssum = num + nums[l] + nums[r]
                if ssum == target:
                    return target
                elif ssum < target:
                    l += 1
                else:
                    r -= 1
                if abs(ssum - target) < abs(res - target):
                    res = ssum
        return res
