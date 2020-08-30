class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # set first element in same row and first element in same column.
        # Time O(mn), space O(1)
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # brutal force
        # find all 0 and set entire row and col to 'k' except 0
        # Time O(mn(m + n)), space O(1)
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.setK(matrix, i, j)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0

    def setK(self, matrix, x, y):
        for j in range(len(matrix[0])):
            if matrix[x][j] != 0:
                matrix[x][j] = float('inf')
        for i in range(len(matrix)):
            if matrix[i][y] != 0:
                matrix[i][y] = float('inf')
