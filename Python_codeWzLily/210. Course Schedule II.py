class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, indegrees = {}, {}
        for i in range(numCourses):
            graph[i] = []
            indegrees[i] = 0
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegrees[course] += 1
        initial_nodes = [
            course for course in indegrees if indegrees[course] == 0]
        queue = deque(initial_nodes)
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)
            for next_course in graph[course]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0 and next_course in graph:
                    queue.append(next_course)
            graph.pop(course)
        return res if len(graph) == 0 else []
