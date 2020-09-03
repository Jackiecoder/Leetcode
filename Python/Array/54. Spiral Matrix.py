class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        m, n = len(matrix), len(matrix[0])
        top_row, top_col, bot_row, bot_col = 0, 0, m - 1, n - 1
        while len(res) < m * n:
            # ends when len(res) == m * n

            # reach top row
            for j in range(top_col, bot_col + 1):
                res.append(matrix[top_row][j])
            top_row += 1
            if len(res) == m * n:
                break

            # reach right column
            for i in range(top_row, bot_row + 1):
                res.append(matrix[i][bot_col])
            bot_col -= 1
            if len(res) == m * n:
                break

            # reach bottom row (in reversed order)
            for j in range(bot_col, top_col - 1, -1):
                res.append(matrix[bot_row][j])
            bot_row -= 1
            if len(res) == m * n:
                break

            # reach left column
            for i in range(bot_row, top_row - 1, -1):
                res.append(matrix[i][top_col])
            top_col += 1
            if len(res) == m * n:
                break

        return res
