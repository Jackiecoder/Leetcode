class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # bucket sort
        # Time O(n), space O(max(heights))
        max_height = max(heights)
        height_freq = [0] * (max_height + 1)
        for h in heights:
            height_freq[h] += 1
        height_index = 0
        count_diff = 0
        for h in range(max_height + 1):
            freq = height_freq[h]
            for _ in range(freq):
                if heights[height_index] != h:
                    count_diff += 1
                height_index += 1
        return count_diff
