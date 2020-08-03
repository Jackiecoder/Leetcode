class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # get the diff by the min and max, and length
        # Time O(n), space O(1)
        diff = (max(arr) - min(arr)) / (len(arr) - 1)
        arr_set = set(arr)
        if diff == 0:
            return len(arr_set) == 1
        cur = min(arr)
        while cur <= max(arr):
            if cur not in arr_set:
                return False
            cur += diff
        return True

    def canMakeArithmeticProgression_nlogn(self, arr: List[int]) -> bool:
        # sort the arr, and find diff
        # Time O(nlogn), space O(1)
        arr.sort()
        diff = arr[1] - arr[0]
        for index in range(1, len(arr)):
            if arr[index] - arr[index - 1] != diff:
                return False
        return True
