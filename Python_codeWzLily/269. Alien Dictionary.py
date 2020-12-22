class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # topological sort
        # e.g.
        #   ["wrt","wrf","er","ett","rftt"]
        #  graph:       indegree
        #    w = [r]        0
        #    r = [t, f]     2
        #    t = []         3
        #    f = [t]        1
        #    e = [r, t]     0
        #  w, e, r, f, t
        # if this edge was not added yet, add to graph, indegree += 1
        # Time o(V + E), SPACE O(V + E)
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        chars = set()
        if not words:
            return ""
        chars |= set(words[0])
        for i in range(len(words) - 1):
            prev_word, next_word = words[i], words[i + 1]
            ind = 0
            chars |= set(prev_word)
            chars |= set(next_word)
            while ind < len(prev_word):
                if ind >= len(next_word):
                    return ""
                if prev_word[ind] != next_word[ind]:
                    graph[prev_word[ind]].append(next_word[ind])
                    indegrees[next_word[ind]] += 1
                    indegrees[prev_word[ind]]
                    break
                ind += 1
        if not graph:
            return "".join(list(chars))
        initial_nodes = [i for i in indegrees if indegrees[i] == 0]
        queue = deque(initial_nodes)
        res = ""
        while queue:
            node = queue.popleft()
            res = res + node
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                # print(node, neighbor, indegrees[neighbor])
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
            graph.pop(node)
            chars.remove(node)
        if chars:
            res = res + "".join(list(chars))
        return res if not graph else ""
