class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # binary search
        # 1. mid largest -> move left
        # 2. l largest -> move right
        # 3. r largest -> move left
        # Time O(logn), space O(1)
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid
        if arr[left] > arr[right]:
            return left
        return right
