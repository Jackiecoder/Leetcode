class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # topological sort
        # in queue -> this node already have indegree == 0
        #   once node pop out -> the node will be removed from the graph

        # 1. generate graph
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        for course, pre in prerequisites:
            graph[course]
            indegrees[pre]
            graph[pre].append(course)
            indegrees[course] += 1

        # 2. go through the graph
        initial_nodes = [course for course,
                         indegree in indegrees.items() if indegree == 0]
        queue = deque(initial_nodes)
        while queue:
            node = queue.popleft()
            for next_node in graph[node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0 and next_node in graph:
                    queue.append(next_node)
            graph.pop(node)
        return len(graph) == 0
