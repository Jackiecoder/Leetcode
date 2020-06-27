class DJS:
    def __init__(self):
        self.parent = {}
        self.vals = defaultdict(lambda: 1.0)

    def find(self, x):
        self.parent.setdefault(x, x)
        if self.parent[x] != x:
            self.parent[x], val = self.find(self.parent[x])
            self.vals[x] *= val
        return self.parent[x], self.vals[x]

    # x / rx = valx
    # y / x = 1 / k
    # ry / y = 1 / valy
    def union(self, x, y, k):
        rx, valx = self.find(x)
        ry, valy = self.find(y)
        if rx != ry:
            self.parent[ry] = rx
            self.vals[ry] = valx / (valy * k)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        Union-find class
        '''
        uf = DJS()
        for (x, y), val in zip(equations, values):
            uf.union(x, y, val)
            # print(uf.parent)
            # print(uf.vals)
        res = []
        for start, end in queries:
            if start not in uf.parent or end not in uf.parent:
                res.append(-1)
                continue
            rstart, val_start = uf.find(start)
            rend, val_end = uf.find(end)
            if rstart != rend:
                res.append(-1)
            else:
                res.append(val_start / val_end)
        return res

        '''
        # Union Find
        parent = {}
        ratio = {}
        
        def add(x):
            if x in parent:
                return
            parent[x] = x
            ratio[x] = 1
        
        def find(x):
            if x != parent[x]:
                parent[x], val = find(parent[x])
                ratio[x] *= val
            return parent[x], ratio[x]
        
        def union(x, y, k):
            add(x)
            add(y)
            root_x, _ = find(x)
            root_y, _ = find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                ratio[root_x] = k * (ratio[y] / ratio[x])
                
        
        res = []
        for i, (start, end) in enumerate(equations):
            union(start, end, values[i])
        for start, end in queries:
            if start in parent and end in parent and find(start)[0] == find(end)[0]:
                res.append(ratio[start] / ratio[end])
            else:
                res.append(-1)
        return res
        '''

        '''
        # graph + BFS
        # 
        # graph = {node1: {node2: val}, node2: {node1: 1 / val}}
        # for each (node1, node2) find the path from node1 to node2
        # time O(N) + O(NQ), space O(N)
        
        graph = collections.defaultdict(lambda: collections.defaultdict(int))
        for i, (node1, node2) in enumerate(equations):
            graph[node1][node2] = values[i]
            graph[node2][node1] = 1 / values[i]
        res = []
        for i, (start, end) in enumerate(queries):
            if start not in graph or end not in graph:
                res.append(-1)
                continue
            queue = collections.deque([(start, 1)])
            visited = set()
            while queue:
                node, cur_val = queue.popleft()
                if node == end:
                    res.append(cur_val)
                    break
                visited.add(node)
                for neighbor, val in graph[node].items():
                    if neighbor in visited:
                        continue
                    queue.append((neighbor, cur_val * val))
            if len(res) <= i:
                res.append(-1)
        return res
        '''
