class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # topological sort
        # make sure while in bfs, the length of queue will never greater than 1
        graph, indegree = {}, {}
        for seq in seqs:
            for val in seq:
                graph[val] = []
                indegree[val] = 0
        for seq in seqs:
            for i in range(len(seq) - 1):
                graph[seq[i]].append(seq[i + 1])
                indegree[seq[i + 1]] += 1
        start_points = [node for node, val in indegree.items() if val == 0]
        queue = collections.deque(start_points)
        for node in start_points:
            indegree.pop(node)
        order = []
        while queue:
            if len(queue) > 1:
                return False
            cur = queue.popleft()
            order.append(cur)
            for child in graph[cur]:
                if child in indegree:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        queue.append(child)
                        indegree.pop(child)
        return not indegree and order == org
