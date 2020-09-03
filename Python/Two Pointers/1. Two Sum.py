class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointer
        # sort and find
        # time O(nlogn), space O(1)
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        left, right = 0, len(nums) - 1
        while left < right:
            ssum = nums[left][1] + nums[right][1]
            if ssum == target:
                return sorted([nums[left][0], nums[right][0]])
            elif ssum < target:
                left += 1
            else:
                right -= 1

    def twoSum_hashmap(self, nums: List[int], target: int) -> List[int]:
        # time O(n), space O(n)
        remain_to_num = {}
        for i, num in enumerate(nums):
            remain = target - num
            if num in remain_to_num:
                return [i, remain_to_num[num]]
            remain_to_num[remain] = i
