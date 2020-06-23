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
