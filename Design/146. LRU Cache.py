'''
use ordered dictionary
'''


class LRUCache:

    def __init__(self, capacity: int):
        self.remain = capacity
        self.dic = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dic:
            ret = self.dic[key]
            self.dic.pop(key)
            self.dic[key] = ret
        else:
            ret = -1
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
            self.dic[key] = value
        else:
            if self.remain == 0:
                self.dic.popitem(last=False)
                self.remain += 1
            self.dic[key] = value
            self.remain -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''
use double linked list + dictionary
'''


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    # use double linked list + dictionary

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}  # key -> node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove_node(node)
        self.add_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove_node(self.dic[key])
        new_node = Node(key, value)
        self.add_node(new_node)
        self.dic[key] = new_node
        if len(self.dic) > self.capacity:
            removed_node = self.head.next
            self.remove_node(removed_node)
            self.dic.pop(removed_node.key)

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def add_node(self, node):
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
