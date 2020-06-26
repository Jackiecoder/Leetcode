class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(lambda: TrieNode())
        self.is_end = False
        self.times = 0
        self.sen = ''


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.cur_node = self.root

    def insert(self, sentence, times):
        cur = self.root
        for char in sentence:
            cur = cur.children[char]
        cur.is_end = True
        cur.times += times
        cur.sen = sentence

    def search_with_cur_node(self, char):
        # print(self.root.children['w'].children.keys())
        # bfs
        if char not in self.cur_node.children:
            self.cur_node = self.cur_node.children[char]
            return []
        self.cur_node = self.cur_node.children[char]
        queue = collections.deque([self.cur_node])
        heap = []
        # in the heap, times smaller will pop first, and ascii larger will pop first
        # we want larger times, and smaller ascii
        while queue:
            node = queue.popleft()
            if node.is_end:
                heapq.heappush(heap, (-node.times, node.sen))
            for child in node.children:
                queue.append(node.children[child])
        res = []
        for _ in range(3):
            if not heap:
                break
            res.append(heapq.heappop(heap))
        return res


class AutocompleteSystem:
    '''
    @ self.cur_node, self.hist_record, 
    each sentence will save in the trie tree, and how many time it was searched will record as times. 
    once input some characters, self.cur_node will go to this character in its children
    -> if char not in children: create new child, and make self.record empty.
    -> if char in children: go to this child
    '''

    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.char_record = ''
        for i, sentence in enumerate(sentences):
            self.trie.insert(sentence, times[i])

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.trie.insert(self.char_record, 1)
            self.trie.cur_node = self.trie.root
            self.char_record = ''
            return []
        self.char_record += c
        res = self.trie.search_with_cur_node(c)
        return [sentence for times, sentence in res]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
