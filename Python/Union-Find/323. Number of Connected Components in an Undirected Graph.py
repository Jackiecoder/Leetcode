class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [x for x in range(n)]
        rank = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
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
            return True

        for x, y in edges:
            union(x, y)
        # print(parent)
        groups = len(set([find(x) for x in parent]))
        return groups
