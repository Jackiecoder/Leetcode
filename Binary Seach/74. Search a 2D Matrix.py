class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search find row (find the row whose head is the largest smaller of target)
        #   1. if target < head of row 0 -> return False
        # binary search find col
        #   2. if can't find -> return False
        # Time O(logn + logm), space O(1)
        if not matrix or not matrix[0]:
            return False
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n - 1
        while l + 1 < r:
            mid = (l + r) // 2
            head = matrix[mid][0]
            if head == target:
                return True
            elif head < target:
                l = mid
            else:
                r = mid
        if matrix[r][0] <= target:
            row = r
        elif matrix[l][0] <= target:
            row = l
        else:
            return False
        l, r = 0, m - 1
        while l + 1 < r:
            mid = (l + r) // 2
            num = matrix[row][mid]
            if num == target:
                return True
            elif num < target:
                l = mid
            else:
                r = mid
        if matrix[row][l] == target or matrix[row][r] == target:
            return True
        return False
