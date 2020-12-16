class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # this problem could be regarded as a graph problem
        # Time O(n**2), Space O(n**2)
        res = []
        # self.dfs(nums, 0, [], res)
        self.dfs1(nums, [], res)
        return res

    def dfs(self, nums, ind, path, res):
        res.append(path[:])
        for i in range(ind, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res)
            path.pop()

    def dfs1(self, nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            self.dfs1(nums[i + 1:], path + [nums[i]], res)
