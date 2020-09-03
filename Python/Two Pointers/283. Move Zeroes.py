class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0, 1, 0, 3, 12]
        #  .  .
        # -- Two Pointers --
        # zero record zero position
        # time O(N), Space O(1)
        # zero = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[i], nums[zero] = nums[zero], nums[i]
        #         zero += 1

        # -- replace the whole array --
        non_zero = [num for num in nums if num != 0]
        nums[:] = non_zero + [0] * (len(nums) - len(non_zero))
