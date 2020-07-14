class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, candidates, target, path, res):
        if target == 0:
            res.append(path[:])
            return
        for i, cur in enumerate(candidates):
            if i > 0 and cur == candidates[i - 1]:
                continue
            if cur > target:
                break
            path.append(cur)
            self.dfs(candidates[i + 1:], target - cur, path, res)
            path.pop()
