class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(lambda: TrieNode())
        self.is_end = False


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        # O(number of char in dict)
        for word in dict:
            cur = self.root
            for char in word:
                cur = cur.children[char]
            cur.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return self.modify_search(word, 1, self.root)

    def modify_search(self, word, modify, node):
        if modify < 0:
            return False
        if not word:
            return node.is_end and modify == 0

        head = word[0]
        for child in node.children:
            if (child == head and self.modify_search(word[1:], modify, node.children[child])) or (child != head and self.modify_search(word[1:], modify - 1, node.children[child])):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
