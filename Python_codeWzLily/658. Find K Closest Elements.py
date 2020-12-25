class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # compare arr[i] and arr[i + k], make the difference between the difference of arr[i] to x and the difference of arr[i + k] to x smaller
        #   why ? ? ?
        # case1: x <= arr[i] < arr[i + k - 1]  move left
        # case2: arr[i] < x < arr[i + k - 1]
        #       1. x - arr[i] < arr[i + k - 1] - x -> move left
        #       2. x - arr[i] > arr[i + k - 1] - x -> move right
        # case3: arr[i] < arr[i + k - 1] <= x  move right
        # target is find the start point of the sliding window
        #   this window has start point arr[i] and end point arr[i + k - 1]
        # left, right = 0, len(arr) - k
        # while left + 1 < right:
        #     mid = (left + right) // 2
        #     if x <= arr[mid] or arr[mid] <= x <= arr[mid + k - 1] and x - arr[mid] < arr[mid + k - 1] - x:
        #         right = mid
        #     else:
        #         left = mid
        # print(left, right)
        # if abs(arr[left + k - 1] + arr[left] - 2 * x) <= abs(arr[right + k - 1] + arr[right] - 2 * x):
        #     return arr[left: left + k]
        # return arr[right: right + k]

        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left: left + k]

    def findClosestElements_bs(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search + two pointer
        # find closest two points, and go forward and backward
        # time O(logn + k + klogk), space O(1)
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] <= x:
                left = mid
            else:
                right = mid
        res = []
        while k > 0:
            if not (0 <= right < len(arr)) or 0 <= left < len(arr) and abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
            k -= 1
        return sorted(res)

    def findClosestElements_heap(self, arr: List[int], k: int, x: int) -> List[int]:
        # method 1:
        # heap to store the difference, pop the element with minimum difference
        # time O(n + klogn + klogk), space O(n)
        heap = [(abs(val - x), val) for val in arr]
        heapq.heapify(heap)
        res = []
        while k > 0:
            diff, val = heapq.heappop(heap)
            res.append(val)
            k -= 1
        return sorted(res)
