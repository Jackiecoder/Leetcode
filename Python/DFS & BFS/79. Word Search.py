class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS
        #
        # e.g.  ABCCED
        #       A
        #    B      S
        # C.   F
        # E C
        #  FES
        #  D E
        # Time O(3^K * MN)
        # Space O(K)
        if not board:
            return False
        m, n = len(board), len(board[0])
        if m * n < len(word):
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word, 1, set([(i, j)])):
                        return True
        return False

    def dfs(self, board, x, y, word, index, visited):
        # if call this function, means index - 1 is already varified
        if index == len(word):
            return True
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == word[index] and (nx, ny) not in visited:
                visited.add((nx, ny))
                if self.dfs(board, nx, ny, word, index + 1, visited):
                    return True
                visited.remove((nx, ny))
        return False
