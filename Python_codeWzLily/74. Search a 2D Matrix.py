class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row
        #   -> binary search row[0] < target < row + 1[0]
        # then binary search
        # Time O(logn + logm), space O(1)
        m, n = len(matrix), len(matrix[0])
        if m <= 1:
            row = 0
        elif matrix[-1][0] <= target:
            row = m - 1
        else:
            row = self.find_row(matrix, target)
        if row == -1:
            return False
        arr = matrix[row]
        l, r = 0, n - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid
            else:
                r = mid
        if arr[l] == target or arr[r] == target:
            return True
        return False

    def find_row(self, matrix, target):
        m = len(matrix)
        l, r = 0, m - 2
        while l + 1 < r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target < matrix[mid + 1][0]:
                return mid
            elif matrix[mid][0] > target:
                r = mid
            else:
                l = mid
        if matrix[l][0] <= target < matrix[l + 1][0]:
            return l
        if matrix[r][0] <= target < matrix[r + 1][0]:
            return r
        return -1
