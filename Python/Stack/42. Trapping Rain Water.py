class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        # left[i] -> highest bar in A[0] - A[i]
        # right[i] -> highest bar in A[i] - A[n - 1]
        # for each i
        #   volume[i] = min(left[i], right[i]) - A[i]
        # time O(n), space O(n)

        n = len(height)
        left = [0] * n
        right = [0] * n
        volume = [0] * n
        for i in range(n):
            if i == 0:
                left[i] = height[0]
                continue
            left[i] = max(left[i - 1], height[i])
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                right[i] = height[i]
                continue
            right[i] = max(right[i + 1], height[i])
        # print(left, right)
        res = 0
        for i in range(n):
            res += max(min(left[i], right[i]) - height[i], 0)
        return res
        '''

        # decreasing stack
        # when stack[-1] > h: append
        # when stack[-1] == h: append
        # when stack[-1] < h: pop and res += max( min(left, h) * length, 0 )
        #                      utill len(stack) == 1: stack.append
        # stack =  [0, 7, 8, 10, 11]
        # length = [0, 3, 2, 2 , 1]
        # i   = 10
        # val = 2
        # add =
        # res =  6
        if not height:
            return 0
        res = 0
        stack = collections.deque()
        for i, h in enumerate(height):
            if not stack:
                stack.append(i)
                continue
            while len(stack) > 1 and height[stack[-1]] < h:
                # print(res, stack)
                cur_index = stack.pop()
                cur_height = height[cur_index]
                res += max((min(height[stack[-1]], h) -
                            cur_height) * (i - stack[-1] - 1), 0)
            stack.append(i)
            # print(res, stack, i)
        return res
