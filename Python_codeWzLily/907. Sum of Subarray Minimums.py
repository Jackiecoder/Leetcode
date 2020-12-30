class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # THIS IS AN AMAZING SOLUTION
        # in this method, we could only store the index of each number
        #   once an index is popped out, we could get the "left" and "right"
        # this method will only need one pass
        # Time O(n), space O(n)
        total = 0
        stack = []
        arr = [0] + arr + [0]
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                cur = stack.pop()
                left_ind = stack[-1]
                total += arr[cur] * (i - cur) * (cur - left_ind)
            stack.append(i)
        return total % (10 ** 9 + 7)

    def sumSubarrayMins_2(self, arr: List[int]) -> int:
        # rather than storing the index, we could just store the length
        #   !tip: left[] will store the length of strict bigger number on the left side
        #         right[] will store the length of bigger or equal number on the right side
        #       why?
        #       when there are two equal number, we will only consider the subarray that starting with this number
        # in the stack, the (number, length) will be store
        # Time O(n), space O(n)
        n = len(arr)
        left, right, stack1, stack2 = [0] * n, [0] * n, [], []
        for ind in range(n):
            length, val = 1, arr[ind]
            while stack1 and stack1[-1][0] > val:
                length += stack1.pop()[1]
            left[ind] = length
            stack1.append((arr[ind], length))
        for ind in range(n)[::-1]:
            length, val = 1, arr[ind]
            while stack2 and stack2[-1][0] >= val:
                length += stack2.pop()[1]
            right[ind] = length
            stack2.append((arr[ind], length))
        total = 0
        for ind, val in enumerate(arr):
            total += val * left[ind] * right[ind]
        return total % (10 ** 9 + 7)

    def sumSubarrayMins_3(self, arr: List[int]) -> int:
        # sliding windows
        # find all minimum of length = 1, then length = 2, ...
        #   each length will take O(n) to get all minimum
        # totally n different length
        # Time O(n ** 2), space O(1)

        # monotonous increasing stack
        # find the previous and next number smaller than current value
        # e.g. in [3, 1, 2, 4]
        #   prev_ind = [-1, -1, 1, 2]
        #   next_ind = [1, 4, 4, 4]
        #   Q: how to achieve it?
        #   A: monotonous increasing stack
        #   stack = [], ind = None
        #   stack = [(3, 0)], ind = 1, because 3 didn't find any value smaller than it, we set prev_ind[0] = -1
        #   stack = [(1, 1)], ind = 1, same as previous step, prev_ind[1] = -1
        #   stack = [(1, 1), (2, 2)], ind = 2, prev_ind[2] = 1
        #   stack = [(1, 1), (2, 2), (4, 3)], ind = 3, prev_ind[3] = 2
        # Q: how to use the prev_ind and next_ind?
        # A: 1 + (left) * (right) + (left) + (right),
        #       left, right donate -> how many number greater than it on its left / right
        #   sum = 3 * (1+0+0+0) + 1 * (1+1+2+2) + 2 * (1+0+1+0) + 4 * (1+0+0+0) = 3 + 6 + 4 + 4 = 17
        # Time O(n), space O(n)
        prev_ind, stack = [-1] * len(arr), []
        for ind, val in enumerate(arr):
            while (stack and stack[-1][0] >= val):
                stack.pop()
            if stack:
                prev_ind[ind] = stack[-1][1]
            stack.append((val, ind))
        next_ind, stack = [len(arr)] * len(arr), []
        for ind in range(len(arr))[::-1]:
            val = arr[ind]
            while (stack and stack[-1][0] > val):
                stack.pop()
            if stack:
                next_ind[ind] = stack[-1][1]
            stack.append((val, ind))
        total = 0
        for ind, val in enumerate(arr):
            left = ind - prev_ind[ind] - 1
            right = next_ind[ind] - ind - 1
            total += val * (1 + left + right + left * right)
        return total % (10 ** 9 + 7)
