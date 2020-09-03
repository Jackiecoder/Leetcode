class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(lambda: collections.defaultdict(int))
        for u, v, w in times:
            graph[u][v] = w
        queue = collections.deque([(0, K)])
        memo = {}
        while queue:
            time, node = queue.popleft()
            if node not in memo or time < memo[node]:
                memo[node] = time
                if node not in graph:
                    # leaf node
                    continue
                for neighbor in graph[node]:
                    queue.append((time + graph[node][neighbor], neighbor))
        if len(memo) != N:
            return -1
        return max(memo.values())
