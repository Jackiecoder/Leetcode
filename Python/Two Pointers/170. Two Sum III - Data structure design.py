class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.vals.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        remainer = set()
        for val in self.vals:
            if val in remainer:
                return True
            remainer.add(value - val)
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
