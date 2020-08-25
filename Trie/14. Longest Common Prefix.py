class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.child:
                node.child[char] = TrieNode()
            node = node.child[char]
        node.is_end = True

    def startWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.child:
                return False
            node = node.child[char]
        return True

    def commonPrefix(self):
        root = self.root
        res = ''
        while len(root.child) == 1 and not root.is_end:
            char = list(root.child.keys())[0]
            res += char
            root = root.child[char]
        return res


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Trie Tree
        '''
        tree = Trie()
        for str in strs:
            tree.addWord(str)
        return tree.commonPrefix()
