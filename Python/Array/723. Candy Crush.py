class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        board = list(map(list, zip(*reversed(board))))
        m, n = len(board), len(board[0])
        found = True
        while found:
            found = False
            for i in range(m):
                for j in range(2, n):
                    val = abs(board[i][j])
                    if val == 0:
                        continue
                    if val == abs(board[i][j - 1]) == abs(board[i][j - 2]):
                        board[i][j] = -val
                        board[i][j - 1] = -val
                        board[i][j - 2] = -val
                        found = True
            for j in range(n):
                for i in range(2, m):
                    val = abs(board[i][j])
                    if val == 0:
                        continue
                    if val == abs(board[i - 1][j]) == abs(board[i - 2][j]):
                        board[i][j] = -val
                        board[i - 1][j] = -val
                        board[i - 2][j] = -val
                        found = True
            if found:
                for i in range(m):
                    # move zero in each row to the end
                    board[i] = [val for val in board[i] if val > 0]
                    board[i].extend([0] * (n - len(board[i])))
        return reversed(list(map(list, zip(*board))))
