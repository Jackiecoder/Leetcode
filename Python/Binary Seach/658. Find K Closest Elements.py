class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # bs + two pointer
        # use absolute difference to find the smallest absolute
        # Time O(logn + k), space O(k)
        if k >= len(arr):
            return arr
        l, r = 0, len(arr) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if arr[mid] <= x:
                l = mid
            else:
                r = mid

        res = []
        for _ in range(k):
            if r >= len(arr) or abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
        return sorted(res)
