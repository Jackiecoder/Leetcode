class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # brute force:
        # for each height: search width
        # time O(n ** 2), space O(n)

        # increasing stack:
        stack = collections.deque([-1])
        heights.append(0)
        max_area = 0
        for i, height in enumerate(heights):
            while heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area
