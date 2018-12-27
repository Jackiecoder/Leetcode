class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if target < nums[0]:
            return 0
        if nums[length-1] <target:
            return length
        if nums[length-1] == target:
                return length-1
        for nLen in range(length-1):
            if nums[nLen] == target:
                return nLen
            elif nums[nLen]<target and nums[nLen+1]>target:
                return nLen+1