class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy
        # start from the end and go back
        #   varible last_reach -> the farthest index need to reach
        # e.g. [2,3,1,1,4], n = 5
        # initialize.
        #   i = 4 -> last_reach = 4
        # i = 3 -> because i + nums[i] >= last_reach, so last_reach = 3
        # i = 2 -> because i + nums[i] >= last_reach, so last_reach = 2
        # i = 1 -> because i + nums[i] >= last_reach, so last_reach = 1
        # i = 0 -> because i + nums[i] >= last_reach, so last_reach = 0
        #   if last_reach == 0 -> True

        # Time O(n), Space O(1)
        last_reach = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last_reach:
                last_reach = i
        return last_reach == 0
