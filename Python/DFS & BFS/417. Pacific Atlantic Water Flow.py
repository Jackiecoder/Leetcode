class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        for i in range(m):
            self.dfs(matrix, i, 0, pacific, m, n, direction)
            self.dfs(matrix, i, n - 1, atlantic, m, n, direction)
        for j in range(n):
            self.dfs(matrix, 0, j, pacific, m, n, direction)
            self.dfs(matrix, m - 1, j, atlantic, m, n, direction)
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, i, j, visited, m, n, direction):
        # when function called means this pointer already validated
        visited[i][j] = True
        for di, dj in direction:
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and not visited[x][y] and matrix[x][y] >= matrix[i][j]:
                self.dfs(matrix, x, y, visited, m, n, direction)
