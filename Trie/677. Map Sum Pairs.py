class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(lambda: TrieNode())
        self.is_end = False
        self.val = 0


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur = self.root
        for char in key:
            cur = cur.children[char]
        cur.is_end = True
        cur.val = val
        return

    def sum(self, prefix: str) -> int:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        sum_val = 0
        queue = collections.deque([cur])
        while queue:
            node = queue.popleft()
            if node.is_end:
                sum_val += node.val
            for child in node.children:
                queue.append(node.children[child])
        return sum_val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
