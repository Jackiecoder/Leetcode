class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
        # write your code here

        # 1. two pointers
        # choose color from colors
        # use two pointers travel list, if left > color, and right == color, swap
        # Time O(kn), Space O(1)
        # n = len(colors)
        # for color in range(1, k + 1):
        #     left, right = 0, n - 1
        #     while left < right:
        #         while left < right and colors[left] <= color:
        #             left += 1
        #         while left < right and colors[right] != color:
        #             right -= 1
        #         if left < right:
        #             colors[left], colors[right] = colors[right], colors[left]

        # 2. divide and conquer + two pointers
        # choose mid color as pivot, if color < pivot put on left, else put on right
        # Time O(logk N), Space O(1)
        n = len(colors)
        self.sortSubcolors(colors, [0, k], 0, n - 1)

    def sortSubcolors(self, colors, color_range, index_from, index_to):
        if index_from >= index_to or color_range[0] >= color_range[1]:
            return
        mid_color = (color_range[0] + color_range[1]) // 2
        left, right = index_from, index_to
        while left < right:
            # "<=" 000111121111
            while left < right and colors[left] <= mid_color:
                left += 1
            while left < right and colors[right] > mid_color:
                right -= 1
            if left < right:
                colors[left], colors[right] = colors[right], colors[left]
        # loop end, left and right are equal
        self.sortSubcolors(
            colors, [color_range[0], mid_color], index_from, left)
        self.sortSubcolors(
            colors, [mid_color + 1, color_range[1]], left, index_to)
