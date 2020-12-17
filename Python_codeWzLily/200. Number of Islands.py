class Solution:
    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        # reach each island, and use BFS/DFS to mark all connected islands.
        # Time O(mn), space O(mn)
        visited = set()
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != "1" or (i, j) in visited:
                    continue
                res += 1
                visited.add((i, j))
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx, ny = x + dx, y + dy
                        if not 0 <= nx < m or not 0 <= ny < n or (nx, ny) in visited or grid[nx][ny] == "0":
                            continue
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        return res

    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    res += 1
                    self.dfs(grid, i, j, visited)
        return res

    def dfs(self, grid, x, y, visited):
        if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]) or grid[x][y] != "1" or (x, y) in visited:
            return
        visited.add((x, y))
        self.dfs(grid, x, y + 1, visited)
        self.dfs(grid, x, y - 1, visited)
        self.dfs(grid, x + 1, y, visited)
        self.dfs(grid, x - 1, y, visited)
