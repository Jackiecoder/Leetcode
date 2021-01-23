class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        j = 1
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                if cnt < 2:
                    nums[j] = nums[i]
                    j += 1
                    cnt += 1
            else:
                nums[j] = nums[i]
                j += 1
                cnt = 1
        return j
