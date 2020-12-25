# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left, right = 0, 2 * 10 ** 4
        while left + 1 < right:
            mid = (left + right) // 2
            val = reader.get(mid)
            if val == target:
                return mid
            elif val == 2147483647 or target < val:
                right = mid
            else:
                left = mid
        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right
        return -1
