class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, l, r):
        if l > r:
            return
        p = self.partition(nums, l, r)
        self.quickSort(nums, l, p - 1)
        self.quickSort(nums, p + 1, r)

    def partition(self, nums, l, r):
        pivot = nums[r]
        greater = l
        for i in range(l, r):
            if nums[i] < pivot:
                nums[i], nums[greater] = nums[greater], nums[i]
                greater += 1
        nums[greater], nums[r] = nums[r], nums[greater]
        return greater
