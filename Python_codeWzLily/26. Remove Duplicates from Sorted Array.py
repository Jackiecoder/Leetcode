class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Time O(n), space O(1)
        if not nums:
            return 0
        start = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if i > 0 and nums[i] != prev:
                prev = nums[i]
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
                continue
            prev = nums[i]
        return start
