class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_to_index = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.val_to_index)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        # swap val_index with last valid index
        if val not in self.val_to_index:
            return False
        val_index = self.val_to_index[val]
        end_index = len(self.vals) - 1
        self.val_to_index[self.vals[end_index]] = val_index
        self.val_to_index.pop(val)
        self.vals[end_index], self.vals[val_index] = self.vals[val_index], self.vals[end_index]
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.vals[random.randint(0, len(self.val_to_index) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
