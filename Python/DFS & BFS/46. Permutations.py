class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Time O(n!), space O(n!)
        res = []
        self.dfs(nums, [], set(), res)
        return res

    def dfs(self, nums, path, used, res):
        if len(nums) == len(used):
            res.append(path[:])
            return
        for i, num in enumerate(nums):
            if i in used:
                continue
            path.append(num)
            used.add(i)
            self.dfs(nums, path, used, res)
            used.remove(i)
            path.pop()
