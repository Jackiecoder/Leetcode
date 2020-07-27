class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # regard it as a regular 3 sum problem
        # sort it, and then travel throgh index
        # [-4, -1, 1, 2]
        # i     = -4
        # left  = 1
        # right = 2

        # time O(nlogn + n ^ 2), space O(n)

        nums.sort()
        closest_sum = float('INFINITY')
        for i, num in enumerate(nums):
            left, right = i + 1, len(nums) - 1
            while left < right:
                ssum = sum((nums[i], nums[left], nums[right]))
                if abs(target - ssum) < abs(target - closest_sum):
                    closest_sum = ssum
                if ssum > target:
                    right -= 1
                elif ssum < target:
                    left += 1
                else:
                    return closest_sum
        return closest_sum
