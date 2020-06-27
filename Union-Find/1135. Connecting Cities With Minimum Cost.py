class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # union find
        parent = [x for x in range(N + 1)]
        rank = [1] * (N + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return False
            if rank[root_y] > rank[root_x]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            rank[root_x] += rank[root_y]
            return True

        connections.sort(key=lambda x: x[2])
        res = 0
        for x, y, val in connections:
            if union(x, y):
                res += val
        groups = len({find(x) for x in parent}) - 1
        return res if groups == 1 else -1
