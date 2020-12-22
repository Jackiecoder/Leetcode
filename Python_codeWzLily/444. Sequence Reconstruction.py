class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        # convert into graph
        # 1. there should be one start vertex and one end vertex
        #                   (indegree == 0)       (neighbors = [])
        # 2. each step there should be one indegree == 0
        # e.g. [[1,2],[1,3],[2,3]]
        #   graph[1] = [2, 3]
        #        [2] = [3]
        #        [3] = []
        #   indegree[1] = 0
        #   indegree[2] = 1
        #   indegree[3] = 2
        # e.g. [[5,2,6,3],[4,1,5,3]]
        #   graph[5] = [2, 3]
        #        [2] = [6]
        #        [6] = [3]
        #        [3] = []
        #        [4] = [1]
        #        [1] = [5]
        #   indegree[5] = 0
        #           [2] = 0
        #           [6] = 0
        #           [3] = 0
        #           [4] = 0
        #           [1] = 0
        #  4, 1, 5, 2, 6, 3
        # Time O(V+E), Space O(V + E)
        if not seqs:
            return False
        graph = defaultdict(list)  # graph[seq[i]].append(seq[i+1])
        indegree = defaultdict(int)  # indegree[seq[i + 1]] += 1
        for seq in seqs:
            if not seq:
                continue
            indegree[seq[0]]
            graph[seq[-1]]
            for i in range(1, len(seq)):
                graph[seq[i - 1]].append(seq[i])
                indegree[seq[i]] += 1
        initial_node = [i for i in indegree if indegree[i] == 0]
        queue = deque(initial_node)
        res = []
        while queue:
            if len(queue) > 1:
                return False
            node = queue.popleft()
            res.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            graph.pop(node)
        return res == org and not graph
