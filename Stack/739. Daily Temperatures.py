class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # next greater
        # decreasing stack
        # time O(n), space O(n)

        stack = collections.deque()
        days = [0] * len(T)

        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                top = stack.pop()
                days[top] = i - top
            stack.append(i)
        return days
