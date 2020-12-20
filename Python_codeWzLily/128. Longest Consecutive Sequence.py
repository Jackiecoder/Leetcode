class UnionFind():
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.max_rank = 0

    def create_x(self, x):
        self.parent[x] = x
        self.rank[x] = 1
        self.max_rank = max(self.max_rank, 1)

    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return x

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.rank[x] < self.rank[y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.rank[root_x] += self.rank[root_y]
        self.max_rank = max(self.max_rank, self.rank[root_x])
        # print(self.parent, self.rank, self.max_rank)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set()
        uf = UnionFind()
        for i, num in enumerate(nums):
            if num in visited:
                continue
            uf.create_x(num)
            visited.add(num)
            for neighbor in (num - 1, num + 1):
                if neighbor in visited:
                    uf.union(num, neighbor)
        return uf.max_rank
