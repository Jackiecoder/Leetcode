class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegree = {}
        for i in range(numCourses):
            graph[i] = []
            indegree[i] = 0
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] += 1

        start_courses = [course_id for course_id,
                         val in indegree.items() if val == 0]
        queue = collections.deque(start_courses)
        for course in start_courses:
            indegree.pop(course)
        course_order = []
        while queue:
            course = queue.popleft()
            course_order.append(course)
            for connection in graph[course]:
                indegree[connection] -= 1
                if indegree[connection] == 0:
                    queue.append(connection)
                    indegree.pop(connection)

        if not indegree:
            return course_order
        else:
            return []
