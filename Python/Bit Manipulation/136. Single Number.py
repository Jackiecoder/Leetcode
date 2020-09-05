class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bit manipulation
        # XOR opeartion
        # a ^ a = 0
        # 0 ^ a = a
        # Time O(n), space O(1)
        res = 0
        for num in nums:
            res ^= num
        return res
