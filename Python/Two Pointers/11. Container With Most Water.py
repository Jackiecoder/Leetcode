class Solution:
    def maxArea(self, height: List[int]) -> int:
        # we want the min(height) * index
        # so we set length max first:
        # left, right = 0, n - 1
        # then compare height[left] and height[right], which is lower, then move this side
        # left = 0
        # right = 7
        # area = 1 * (right - left)

        # time O(n), space O(1)
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, area)
        return max_area
