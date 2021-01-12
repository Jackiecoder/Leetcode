class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select
        # time O(n), worst O(n**2), space O(1)
        self.quick_select(nums, 0, len(nums) - 1, k)
        return nums[len(nums) - k]

    def quick_select(self, nums, start, end, k):
        if start >= end:
            return
        p = self.partition(nums, start, end)
        if p == k:
            return
        elif p < k:
            self.quick_select(nums, p + 1, end, k)
        else:
            self.quick_select(nums, start, p - 1, k)

    def partition(self, nums, start, end):
        pivot = nums[end]
        greater = start
        for i in range(start, end):
            if nums[i] <= pivot:
                nums[i], nums[greater] = nums[greater], nums[i]
                greater += 1
        nums[greater], nums[end] = nums[end], nums[greater]
        return greater
