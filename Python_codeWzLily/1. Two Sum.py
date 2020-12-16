class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # use hash map to save remain: index
        # Detail:
        #   for each number, store (target - number) as key, and number index as the value
        # once new number found, check if it is in the key set
        # e.g.
        #   {}
        #   {7: 0} (1, 7) -> [0,1]

        # time O(n), space O(n)
        mapping = {}
        for i, number in enumerate(nums):
            if number in mapping:
                return [mapping[number], i]
            mapping[target - number] = i
