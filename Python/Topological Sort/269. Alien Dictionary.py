class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # w -> r -> t
        #        -> f
        #   -> a -> t
        #        -> y

        # w -> e -> r
        # r -> t
        # t -> f

        # for  word[i]  and  word[i + 1]
        # .  travel through each index in them
        # .  if word[i][j] == word[i + 1][j] -> continue
        #   else: word[i + 1][j] is lexicographically larger than word[i][j]
        #         so word[i + 1][j] is word[i][j]' child.
        #

        graph, indegree = {}, {}
        for word in words:
            for char in word:
                graph[char] = []
                indegree[char] = 0
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j == len(words[i + 1]):
                    return ""
                if words[i][j] == words[i + 1][j]:
                    continue
                graph[words[i][j]].append(words[i + 1][j])
                indegree[words[i + 1][j]] += 1
                break
        start_points = [char for char, val in indegree.items() if val == 0]
        for char in start_points:
            indegree.pop(char)
        order = []
        queue = collections.deque(start_points)
        while queue:
            cur = queue.popleft()
            order.append(cur)
            for child in graph[cur]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                    indegree.pop(child)
        if indegree:
            return ""
        return ''.join(order)
