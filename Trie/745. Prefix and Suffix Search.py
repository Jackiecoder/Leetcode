'''
use two trie to store prefix and suffix
when provide the filter conditions, travel through from the end of word list to the beginning, and check if each word have correct prefix and suffix
# number of words -> N
# ave word length -> L
# ave prefix and suffix -> M
# time: initial O(NL), f O(MN)
# space: O(NL)
'''


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(lambda: TrieNode())
        self.is_end = False
        self.weight = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, weight):
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.is_end = True
        cur.weight = weight

    def start_with(self, prefix):
        res = set()
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return res
            cur = cur.children[char]
        # bfs
        queue = collections.deque([cur])
        while queue:
            node = queue.popleft()
            if node.is_end:
                res.add(node.weight)
            for child in node.children:
                queue.append(node.children[child])
        return res


class WordFilter:
    def __init__(self, words: List[str]):
        self.pre_root = Trie()
        self.suf_root = Trie()
        for i, word in enumerate(words):
            self.pre_root.insert(word, i)
            self.suf_root.insert(word[::-1], i)

    def f(self, prefix: str, suffix: str) -> int:
        res1 = self.pre_root.start_with(prefix)
        res2 = self.suf_root.start_with(suffix[::-1])
        res = res1.intersection(res2)
        return max(res) if res else -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
