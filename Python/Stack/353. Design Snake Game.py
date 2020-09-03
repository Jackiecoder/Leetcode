class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food_queue = collections.deque(food)
        self.body_queue = collections.deque([(0, 0)])
        self.head = (0, 0)

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        # s  s
        #    s  f
        # body_queue = [(0, 0), (0, 1), (1, 1)]
        # new_head = (1, 2) -> y + 1
        # check if touch wall, or touch body, return -1
        # else: body_queue.append(new_head)
        #   if new_head == food[0]:
        #       food_queue.popleft
        #   else:
        #       body_queue.popleft
        # score = len(body_queue) - 1
        row, col = self.head
        if direction == 'U':
            self.head = (row - 1, col)
        elif direction == 'L':
            self.head = (row, col - 1)
        elif direction == 'R':
            self.head = (row, col + 1)
        else:
            self.head = (row + 1, col)
        # print(self.head, self.body_queue, self.food_queue)
        if not 0 <= self.head[0] < self.height or not 0 <= self.head[1] < self.width or (self.head in self.body_queue and self.head != self.body_queue[0]):
            return -1
        self.body_queue.append(self.head)
        if self.food_queue:
            cur_food = tuple(self.food_queue[0])
        else:
            cur_food = None
        if self.head != cur_food:
            self.body_queue.popleft()
        else:
            self.food_queue.popleft()
        return len(self.body_queue) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
