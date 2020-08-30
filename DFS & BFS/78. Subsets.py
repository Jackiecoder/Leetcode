class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res)
            path.pop()
