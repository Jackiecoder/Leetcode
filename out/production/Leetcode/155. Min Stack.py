class MinStack:
    # requirement: push, pop, top, get min -> O(n)
    # how to get min in O(n)
    # use a stack to store the minimum
    # main_stack =    [-2, 0 , -3]
    # minimum_stack = [-2, -2, -3]
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = collections.deque()
        self.min_stack = collections.deque([float('INFINITY')])

    def push(self, x: int) -> None:
        self.min_stack.append(min(x, self.min_stack[-1]))
        self.main_stack.append(x)

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
