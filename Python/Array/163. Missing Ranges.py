class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # prev = num
        # travel through the array, and push the first number into prev
        # then when I reach a number, I'll compare it with prev,
        #   if prev + 1 = number -> prev = number
        #   else: -> fill the interval
        #       1. prev + 2 = number -> "{prev + 1}"
        #       2. prev + 2 < number -> "{prev + 1}->{number - 1}"
        #       prev = number
        # Time O(n), space O(n)
        prev = lower - 1
        nums.append(upper + 1)
        res = []
        for num in nums:
            if prev + 1 < num:
                # fill the interval
                if prev + 2 == num:
                    res.append(str(prev + 1))
                else:
                    res.append(str(prev + 1) + "->" + str(num - 1))
            prev = num
        return res
