class UnionFind():
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.island = 0

    def create_x(self, x):
        self.parent[x] = x
        self.rank[x] = 0
        self.island += 1

    def find(self, x):
        parent = self.parent[x]
        if parent != x:
            return self.find(parent)
        return parent

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.rank[root_x] += 1
        self.island -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # union find
        uf = UnionFind()
        visited = set()
        res = []
        for i, j in positions:
            pos = i * n + j
            if pos not in visited:
                uf.create_x(pos)
                visited.add(pos)
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if not (0 <= ni < m and 0 <= nj < n):
                    continue
                n_pos = ni * n + nj
                if n_pos in visited:
                    uf.union(pos, n_pos)
            res.append(uf.island)
        return res
