class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # time O(n**3), space O(n)
        res = []
        nums.sort()
        self.kSum(nums, 0, 4, target, [], res)
        return res

    def kSum(self, nums, start, k, target, path, res):
        if k > 2:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                self.kSum(nums, i + 1, k - 1, target - nums[i], path, res)
                path.pop()
        else:
            l, r = start, len(nums) - 1
            while l < r:
                while l < r and l > start and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and r < len(nums) - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                if l >= r:
                    break
                t = nums[l] + nums[r]
                if t == target:
                    res.append(path[:] + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif t < target:
                    l += 1
                else:
                    r -= 1
