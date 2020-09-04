class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # this problem can be converted into a graph problem.
        # this graph can be explored by DFS / BFS
        #   because it needs shortest transformation -> BFS
        # and to avoid duplicated calculation -> memo to store visited words
        # e.g.
        # hit -> hot -> dot -> dog
        #                   -> lot -> log -> cog
        # Time O(kn), space O(kn). k is average length of word

        # 1. build graph
        word_dict = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                word_dict[word[:i] + '_' + word[i + 1:]].append(word)

        queue = deque([(beginWord, 1)])
        # visited = set([beginWord])
        while queue:
            word, lvl = queue.popleft()
            if word == endWord:
                return lvl
            for i in range(len(word)):
                new_word = word[:i] + '_' + word[i + 1:]
                if new_word in word_dict:
                    for tmp in word_dict[new_word]:
                        queue.append((tmp, lvl + 1))
                    word_dict.pop(new_word)
        return 0
