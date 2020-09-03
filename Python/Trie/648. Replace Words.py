class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(lambda: TrieNode())
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.is_end = True

    def find_prefix(self, word):
        cur = self.root
        prefix = ''
        for char in word:
            if cur.is_end:
                return prefix
            if char not in cur.children:
                return
            prefix += char
            cur = cur.children[char]
        return


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dict:
            trie.insert(word)
        words_ls = sentence.split(' ')
        for i, word in enumerate(words_ls):
            ret = trie.find_prefix(word)
            if ret:
                words_ls[i] = ret
        return ' '.join(words_ls)
