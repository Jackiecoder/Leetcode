class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort it, and do two sum
        # Time O(nlogn + n^2) = O(n^2)
        # Space O(n)
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(nums, i + 1, -num, res)
        return res

    def twoSum(self, nums, index, target, res):
        left, right = index, len(nums) - 1
        visited = set()
        while left < right:
            ssum = nums[left] + nums[right]
            if ssum == target and (nums[left], nums[right]) not in visited:
                visited.add((nums[left], nums[right]))
                res.append([-target, nums[left], nums[right]])
            elif ssum < target:
                left += 1
            else:
                right -= 1
