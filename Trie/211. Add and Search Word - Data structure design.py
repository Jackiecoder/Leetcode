class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(lambda: TrieNode())
        self.is_end = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for char in word:
            cur = cur.children[char]
        cur.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        root = self.root
        return self.search_substring(word, root)

    def search_substring(self, word, node):
        if not word:
            return node.is_end
        if not node:
            return False

        head = word[0]
        if head != '.':
            if head in node.children:
                return self.search_substring(word[1:], node.children[head])
        else:
            for child in node.children:
                if self.search_substring(word[1:], node.children[child]):
                    return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
