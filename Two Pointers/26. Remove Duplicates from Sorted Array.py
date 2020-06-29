class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [0, 1, 1, 2, 3,3,3,3,3,3,3]
        #  i
        #     j
        # j + 1 untill num_j != num_i
        if not nums:
            return 0
        tail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1
