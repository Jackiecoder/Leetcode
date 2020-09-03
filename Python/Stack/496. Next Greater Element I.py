class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_dec_stack = collections.deque()
        ele_to_next_greater = {}
        for i, num in enumerate(nums2):
            while mono_dec_stack and mono_dec_stack[-1] < num:
                ele_to_next_greater[mono_dec_stack.pop()] = num
            mono_dec_stack.append(num)
        res = []
        for num in nums1:
            res.append(ele_to_next_greater.get(num, -1))
        return res
