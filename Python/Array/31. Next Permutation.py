class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Let's redo it
        # from end to start, if it is decreasing, just swap those two.
        #                    if it is increasing or equal, continue
        if len(nums) == 1:
            return
        index = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                index = i - 1
                break
        if index == -1:
            nums.sort()
            return
        smallest = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[index]:
                smallest = i
                break
        nums[index], nums[smallest] = nums[smallest], nums[index]
        nums[index + 1:] = sorted(nums[index + 1:])
        return

    def nextPermutation_best(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the largest i, that nums[i] < nums[i + 1]
        #       Q: why not find nums[i] < nums[j], i < j ?
        #       A: it is not necessary, if we try to find all i that have a j satisify nums[i] < nums[j], we will find all of possible permutations greater than current number. Here we find nums[i] < nums[i + 1], this i means I'm pretty sure this i can be swapped with some index after it to make the number greater, but I don't known if this i is the index that I will swap.

        # find the largest j, that nums[i] < nums[j]
        #       Q: why do this?
        #       A: this i is the last index that have nums[i + 1] greater than it, which means nums[i + 1:] is decreasing. then the largest j will be the smallest greater for nums[i].

        # swap nums[i] and nums[j]
        # edge case: if not such i, means nums is decreasing, so this number should be reversed.

        # sort nums[i + 1:] to be increasing
        #       e.g. [1, 5, 4, 3, 2] -> swap [2, 5, 4, 3, 1] -> sort [2, 1, 3, 4, 5]

        last_smaller = -1
        n = len(nums)
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                last_smaller = i
        if last_smaller == -1:
            nums.sort()
            return
        smallest_greater = None
        for j in range(last_smaller + 1, n):
            if nums[last_smaller] < nums[j]:
                smallest_greater = j
        nums[last_smaller], nums[smallest_greater] = nums[smallest_greater], nums[last_smaller]
        nums[last_smaller + 1:] = sorted(nums[last_smaller + 1:])
        return
