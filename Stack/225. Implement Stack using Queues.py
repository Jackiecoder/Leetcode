class MyStack:
    # pop_right -> O(n)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()
        self.top_of_stack = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)
        self.top_of_stack = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.queue1) > 1:
            self.top_of_stack = self.queue1.popleft()
            self.queue2.append(self.top_of_stack)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_of_stack

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
