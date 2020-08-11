class Node:
    def __init__(self, key, val):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key


class LRUCache:

    '''
    dic = {key1: (0, val1)} 
    list = [key1, key2]
    capacity = 2
    1. Time:
        get() -> O(n)
        put() -> O(n)

    -- Follow Up ---
    dic = {key1: node1}
    node1(key1, val) -> node2(key2, val) -> node3(key3, val)
    '''

    def __init__(self, capacity: int):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dic = {}  # key : node
        self.capacity = capacity

    def _add(self, node):
        # add to tail
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        node = Node(key, value)
        self.dic[key] = node
        self._add(node)
        if len(self.dic) > self.capacity:
            del_node = self.head.next
            self._remove(del_node)
            self.dic.pop(del_node.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
