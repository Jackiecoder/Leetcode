class Disjointset(object):
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = [i for i in range(n)]
        self.n = n

    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root
        self.rank[x_root] += self.rank[y_root]
        self.parent[y_root] = x_root


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # union find
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        uf = Disjointset(m * n)
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        uf.union(i * n + j, ni * n + nj)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                index = i * n + j
                if uf.parent[index] == index:
                    count += 1
        return count

        # bfs
#         if not grid:
#             return 0
#         visited = set()
#         m, n = len(grid), len(grid[0])
#         direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         island = 0
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1" and (i, j) not in visited:
#                     island += 1
#                     visited.add((i, j))
#                     queue = collections.deque([(i, j)])
#                     while queue:
#                         x, y = queue.popleft()
#                         for delta_x, delta_y in direction:
#                             new_x, new_y = x + delta_x, y + delta_y
#                             if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == '1' and (new_x, new_y) not in visited:
#                                 visited.add((new_x, new_y))
#                                 queue.append((new_x, new_y))
#         return island
