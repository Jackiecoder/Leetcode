class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # use topological graph to solve it.
        # [1, 0], [2, 0], [2, 1], [3, 1]
        # 0 -> 1 -> 2
        #   ------>
        #       -------> 3

        # graph[pair[1]].append(pair[0])
        # indegree[pair[0]] += 1
        # graph = {0: [1, 2], 1: [2, 3], 2:[], 3:[]}
        # indegree = {}
        # queue = []

        # another example:
        # [1,0], [0, 1]
        # graph = {0:[1], 1:[0]}
        # indegree = [0: 1, 1 : 1]

        # time O(n * v) space = O(n * v)
        graph, indegree = {}, {}
        for i in range(numCourses):
            graph.update({i: []})
            indegree.update({i: 0})
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] += 1
        start_nodes = [course_id for course_id,
                       val in indegree.items() if val == 0]
        queue = collections.deque(start_nodes)
        for node in start_nodes:
            indegree.pop(node)
        while queue:
            course = queue.popleft()
            connection = graph[course]
            for conn in connection:
                indegree[conn] -= 1
                if indegree[conn] == 0:
                    queue.append(conn)
                    indegree.pop(conn)
        return not indegree
