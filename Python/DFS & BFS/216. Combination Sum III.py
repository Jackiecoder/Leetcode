class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # k = 3, n = 7
        # from i = 0 ->
        #   1 -> 2, 6
        #           1, 5
        #   memo[(k, n)] = [[-,-]]
        res = []
        self.dfs(k, n, 1, [], res)
        return res

    def dfs(self, k, n, starter, path, res):
        if n == 0:
            if k == 0:
                res.append(path[:])
            return
        for val in range(starter, 10):
            if val > n:
                break
            path.append(val)
            self.dfs(k - 1, n - val, val + 1, path, res)
            path.pop()
