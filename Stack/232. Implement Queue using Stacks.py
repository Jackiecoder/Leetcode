class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.peek_of_queue = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack1:
            self.peek_of_queue = x
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.stack1) > 1:
            self.peek_of_queue = self.stack1.pop()
            self.stack2.append(self.peek_of_queue)
        res = self.stack1.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.peek_of_queue

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
