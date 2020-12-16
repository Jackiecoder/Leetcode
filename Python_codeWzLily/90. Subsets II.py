class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # The difference between subsetII with subset I was whether the collection of integers might contain duplicates
        # We could firstly sort the input list, and then find the different number to add to the list
        # Time O(m**2), space O(m**2)
        # m  is the number of different numbers in the list
        res = []
        nums.sort()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums[i + 1:], path + [nums[i]], res)
