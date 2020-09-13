class Solution:
    def containsDuplicate_dataStructure(self, nums: List[int]) -> bool:
        # 1. set compare list
        # time O(n), space O(n)
        return len(set(nums)) != len(nums)
