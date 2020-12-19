class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # asking for shortest path, thus we can use BFS to solve it
        # queue = []
        # res = 0

        # step 1: generate dict from previous word to cur word
        replace_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                replace_words[word[:i] + "_" + word[i + 1:]].append(word)
        # step 2:
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            cur, step = queue.popleft()
            if endWord == cur:
                return step
            for i in range(len(cur)):
                new_word = cur[:i] + "_" + cur[i + 1:]
                for next_word in replace_words[new_word]:
                    if next_word in visited:
                        continue
                    visited.add(next_word)
                    queue.append((next_word, step + 1))
        return 0
