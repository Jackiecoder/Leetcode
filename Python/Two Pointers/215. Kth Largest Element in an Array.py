class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick-select
        # time O(n), worst case O(n^2), space O(1)
        if k > len(nums):
            return -1
        return self.quick_select(nums, 0, len(nums) - 1, k)

    def quick_select(self, nums, start, end, k):
        if start >= end:
            return nums[start]
        pivot = (nums[start] + nums[end]) / 2
        left, right = start, end
        while left < right:
            while left < right and nums[left] >= pivot:
                left += 1
            while left < right and nums[right] < pivot:
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
        # left side: [start, left), right side: [left, end]
        if k > left:
            return self.quick_select(nums, left, end, k)
        else:
            return self.quick_select(nums, start, left - 1, k)

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        # heap
        # create heap O(n), pop k largest elemets O(k logn)
        # time O(N + k logN), space O(N)
        if k > len(nums):
            return -1
        heap = [-num for num in nums]
        heapq.heapify(heap)
        while k > 0:
            res = -heapq.heappop(heap)
            k -= 1
        return res
