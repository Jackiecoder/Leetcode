class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # amazing !!
        # Regarding this matrix as a binary search tree
        # the top right should be the root
        # we could start from the top right entry
        # if val > target:
        #   go left (col - 1)
        # if val < target:
        #   go right (row + 1)
        # Time O(m + n), space O(1)
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while 0 <= x < m and 0 <= y < n:
            val = matrix[x][y]
            if val == target:
                return True
            elif val < target:
                x += 1
            else:
                y -= 1
        return False
