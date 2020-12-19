class Solution:
    def findLadders_dfs(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # DFS
        # go through all of the possible path, and find the shortest path
        #   pass "cur word", "path", "shortest_length", "prev_words", "res"
        #       if len(path) >= res[0] -> end the recursion, return
        #   go the then next possible words

        # if res is empty: 1. end word -> store, return
        #                   2. not end word -> continue
        #        not empty: 1. length too long -> return
        #                   2. length equal to len(res[0]) and end word-> append return
        #                   3. length smaller than len(res[0]) and end word-> clear res return

        # Time O(NL + N), space O(KN),
        #   K = possible shortest path

        prev_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + "_" + word[i + 1:]
                prev_words[new_word].append(word)
        res = []
        visited = set(beginWord)
        self.dfs([beginWord], endWord, prev_words, visited, res)
        return res

    def dfs(self, path, endWord, prev_words, visited, res):
        # end condition
        tail = path[-1]
        if res:
            if len(path) > len(res[0]):
                return
            if endWord == tail and len(path) == len(res[0]):
                res.append(path[:])
                return
            if endWord == tail and len(path) < len(res[0]):
                res.clear()
                res.append(path[:])
                return
        if not res and endWord == tail:
            res.append(path[:])
            return

        # main function
        for i in range(len(tail)):
            new = tail[:i] + "_" + tail[i + 1:]
            for next_word in prev_words[new]:
                if next_word in visited:
                    continue
                visited.add(next_word)
                path.append(next_word)
                self.dfs(path, endWord, prev_words, visited, res)
                path.pop()
                visited.remove(next_word)

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # The only difference between the length shortest path and all shortest paths is when return the function
        # BFS
        # TLE
        # time O(NL + N), space O(n ** n)
        prev_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + "_" + word[i + 1:]
                prev_words[new_word].append(word)
        queue = deque()
        queue.append([beginWord])
        find_shortest = False
        visited = set([beginWord])
        res = []
        while queue:
            local_visited = set()
            for _ in range(len(queue)):
                path = queue.popleft()
                tail = path[-1]
                if tail == endWord:
                    res.append(path)
                    find_shortest = True
                for i in range(len(tail)):
                    new_word = tail[:i] + "_" + tail[i + 1:]
                    for next_word in prev_words[new_word]:
                        if next_word in visited:
                            continue
                        local_visited.add(next_word)
                        queue.append(path + [next_word])
            visited |= local_visited
            if find_shortest:
                break
        return res
