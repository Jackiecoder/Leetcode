class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remain_to_num = {}
        for i, num in enumerate(nums):
            remain = target - num
            if num in remain_to_num:
                return [i, remain_to_num[num]]
            remain_to_num[remain] = i
