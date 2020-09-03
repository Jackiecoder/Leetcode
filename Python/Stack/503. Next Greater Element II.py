class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        dec_stack = collections.deque()
        n = len(nums)
        res = [-1] * n
        for i in range(n * 2):
            i = i % n
            while dec_stack and nums[dec_stack[-1]] < nums[i]:
                res[dec_stack.pop()] = nums[i]
            dec_stack.append(i)
        return res
