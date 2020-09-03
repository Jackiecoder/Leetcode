class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # The most tricky method is ->
        # matrix = list(map(list, zip(*matrix[::-1])))

        # more common way to solve it is "transpose" + "filp"
        # Time O(n ^ 2), Space O(1)

        # 1. transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i] = reversed(matrix[i])
