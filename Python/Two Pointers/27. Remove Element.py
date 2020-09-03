class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # swap val to the end
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            while left <= right and nums[right] == val:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
        return left
