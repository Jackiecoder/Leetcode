# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # binary search
        # find smallest version which returns true
        # ffftt
        # if not bad:
        #   left = mid
        # else:
        #   right = mid
        # l = 3
        # r = 4
        left, right = 1, n
        while left + 1 < right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid
            else:
                right = mid
        if isBadVersion(left):
            return left
        return right
