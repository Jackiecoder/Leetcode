class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # for nums[i]
        # left[0: i + 1], right[i:n]
        # time O(n), space O(1)
        output = []
        prod = 1
        for i, num in enumerate(nums):
            output.append(prod)
            prod *= num
            # prod [-, 1, 12, 123]
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= prod
            prod *= nums[i]
            # [234, 34 , 4 , -]
        return output
