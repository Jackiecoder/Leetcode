class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # graph
        # because the size of queries is large, so we can use topological sort to get the relative order
        # V = n
        # E = prerequisites
        # time O(VE) + O(Q)
        # Space O(VE)
        graph = defaultdict(list)
        indegree = {course_id: 0 for course_id in range(n)}
        pres = defaultdict(set)
        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
            pres[course].add(pre)

        queue = collections.deque(
            [course_id for course_id, val in indegree.items() if val == 0])
        # travel through all courses O(V), each Vertex have O(E) parents to update
        while queue:
            cur = queue.popleft()
            for child in graph[cur]:
                pres[child].update(pres[cur])
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        return [pre in pres[course] for pre, course in queries]

        '''
        #Topological sort by Zixuan
        
        # initialization - O(n)
        graph = defaultdict(list)
        inDegree = {i: 0 for i in range(n)}
        precourses = defaultdict(set)
        
        # build graph - O(p)
        for parent, child in prerequisites:
            graph[parent].append(child)
            inDegree[child] += 1
            precourses[child].add(parent)
        
        # O(n)
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        # Outer loop - O(n)
        while sources:
            parent = sources.popleft()
            
            # O(p) in total since we visit all edges
            for child in graph[parent]:
                precourses[child] |= precourses[parent] # O(n)
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        # O(q)
        # results = []
        # for parent, child in queries:
        #     results.append(parent in precourses[child])
        return [c1 in precourses[c2] for c1, c2 in queries]
        '''
