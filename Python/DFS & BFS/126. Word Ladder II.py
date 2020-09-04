class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # quite similar as  126.word Ladder I
        # do BFS, but also store the path
        # Time O(kn), space O((kn) ^ 2)

        # 1. build graph
        dic = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                dic[word[:i] + '_' + word[i + 1:]].append(word)
        queue = deque([(beginWord, beginWord)])
        visited = set([beginWord])
        res = []
        end_lvl = None
        while queue:
            tmp_visited = set()
            for _ in range(len(queue)):
                word, path = queue.popleft()
                if word == endWord:
                    res.append(path.split(' '))
                for i in range(len(word)):
                    dummy_word = word[:i] + '_' + word[i + 1:]
                    for next_word in dic[dummy_word]:
                        if next_word in visited:
                            continue
                        queue.append((next_word, path + ' ' + next_word))
                        tmp_visited.add(next_word)
            if res:
                return res
            visited |= tmp_visited
        return []
