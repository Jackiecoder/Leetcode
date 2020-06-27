class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # bfs
        # replace all 'O's that is connected to outside by 'K'.
        if not board or not board[0]:
            return []
        m, n = len(board), len(board[0])
        connections = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = collections.deque()
        for i in range(m):
            # find j = 0, n - 1
            for j in (0, n - 1):
                if board[i][j] == 'O':
                    queue.append((i, j))
        for j in range(n):
            # find j = 0, n - 1
            for i in (0, m - 1):
                if board[i][j] == 'O':
                    queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            if board[x][y] != 'O':
                continue
            board[x][y] = 'K'
            for dx, dy in connections:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] == 'O':
                    queue.append((new_x, new_y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'K':
                    board[i][j] = 'O'
