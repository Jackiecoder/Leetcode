class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # use two colors to paint each node, and make adjancent nodes have different color.
        paint = {}  # node : color
        cur_color = 0
        # bfs
        for i in range(len(graph)):
            if i in paint:
                continue
            queue = collections.deque([i])
            while queue:
                for _ in range(len(queue)):
                    # queue all nodes are not painted yet
                    node = queue.popleft()
                    paint[node] = cur_color
                    for neighbor in graph[node]:
                        if neighbor in paint:
                            if paint[neighbor] != (cur_color + 1) % 2:
                                return False
                            continue
                        queue.append(neighbor)
                cur_color = (cur_color + 1) % 2
        return True
