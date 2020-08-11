class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # using monotomous stack
        # want the results is stay in my stack
        #
        # algo:
        #   1. travel through the array
        #       1. compare the num with the peek of stack
        #       2. if num > peek -> append
        #       3. elif num <= peek -> pop out
        #       4. if length of stack == 2 -> current peek of stack is the potential second number of result, record it
        #       5. if current num > recorded second number || length of stack == 3: --> True

        # e.g.
        #   nums = [2, 5, 3, 4, 5]
        #   num = 2, stack = [2]
        #   num.= 5, stack = [2, 5]
        #   num.= 3, stack = [2, 3]
        #   num = 4, stack = [2, 3, 4]

        # e.g.
        #   nums = [1, 0, 10, 0, 100]
        # Time O(n), Space O(n)

        # remeber the minimum top of two number subsquence, if any number is greater than min_top, return True
        min_top = float('inf')
        stack = []
        for num in nums:
            while stack and stack[-1] >= num:
                stack.pop()
            stack.append(num)
            if len(stack) == 2:
                min_top = min(min_top, stack[-1])
            if len(stack) == 3 or num > min_top:
                return True
        return False
