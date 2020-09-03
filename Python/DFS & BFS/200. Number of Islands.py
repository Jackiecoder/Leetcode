class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs
        visited = set()
        m, n = len(grid), len(grid[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    island += 1
                    visited.add((i, j))
                    queue = collections.deque([(i, j)])
                    while queue:
                        x, y = queue.popleft()
                        for delta_x, delta_y in direction:
                            new_x, new_y = x + delta_x, y + delta_y
                            if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1' and (new_x, new_y) not in visited:
                                visited.add((new_x, new_y))
                                queue.append((new_x, new_y))
        return island
