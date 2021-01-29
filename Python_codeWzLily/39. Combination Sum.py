class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        res = []
        self.dfs(candidates, 0, target, [], res)
        return res

    def dfs(self, candidates, ind, target, path, res):
        if target == 0:
            res.append(path[:])
            return
        for i in range(ind, len(candidates)):
            val = candidates[i]
            if val > target:
                continue
            path.append(val)
            self.dfs(candidates, i, target - val, path, res)
            path.pop()
