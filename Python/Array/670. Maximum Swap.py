class Solution:
    def maximumSwap(self, num: int) -> int:
        # for each index
        # if cur index is largest
        #  -> if it is, continue, and remove this number
        #  -> if it is not, swap cur number with the largest number and return
        nums = list(str(num))
        largest = [0] * len(nums)
        cur_largest = 0
        for i in range(len(nums) - 1, -1, -1):
            cur_largest = max(cur_largest, int(nums[i]))
            largest[i] = cur_largest
        for i in range(len(nums)):
            if int(nums[i]) == largest[i]:
                continue
            for j in range(len(nums) - 1, i, -1):
                if int(nums[j]) == largest[i]:
                    nums[i], nums[j] = nums[j], nums[i]
            break
        return int(''.join(nums))
