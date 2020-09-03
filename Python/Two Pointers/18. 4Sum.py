class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # time O(n^(k-1)), space O(nk)
        nums.sort()
        res = []
        self.kSum(nums, 0, 4, target, res, [])
        return res

    def kSum(self, nums, start, k, target, res, path):
        if k == 2:
            left, right = start, len(nums) - 1
            while left < right:
                ssum = nums[left] + nums[right]
                if ssum == target:
                    res.append(path + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif ssum < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                self.kSum(nums, i + 1, k - 1, target - nums[i], res, path)
                path.pop()
