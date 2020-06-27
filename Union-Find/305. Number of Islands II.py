class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = [1] * (m * n)
        self.count = 0

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
                x = parent[x]
            return x

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            rank[root_x] += rank[root_y]
            self.count -= 1
            return True

        def set_parent(x):
            if x in parent:
                return
            parent[x] = x
            self.count += 1

        num_of_island = []
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for x, y in positions:
            index = x * n + y
            set_parent(index)
            for dx, dy in direction:
                new_x, new_y = x + dx, y + dy
                new_index = new_x * n + new_y
                if 0 <= new_x < m and 0 <= new_y < n and new_index in parent:
                    union(index, new_index)
            num_of_island.append(self.count)
        return num_of_island
