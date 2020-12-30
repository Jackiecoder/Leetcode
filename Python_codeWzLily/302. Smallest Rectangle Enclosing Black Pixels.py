class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # bfs or dfs
        # traverse the connected black pixels.
        # Time O(E), space O(V)

        # Binary search
        # find left and right boundry, and also top and bottom boundry
        # Time O(mlogn + nlogm), space O(1)
        if not image or not image[0]:
            return 0
        m, n = len(image), len(image[0])
        left_boundry = self.find_left_boundry(image, 0, y)
        right_boundry = self.find_right_boundry(image, y, n - 1)
        top_boundry = self.find_top_boundry(image, 0, x)
        bottom_boundry = self.find_bottom_boundry(image, x, m - 1)
        return (right_boundry - left_boundry + 1) * (bottom_boundry - top_boundry + 1)

    def find_left_boundry(self, image, start, end):
        l, r = start, end
        while l + 1 < r:
            mid = (l + r) // 2
            if self.check_column(image, mid):
                r = mid
            else:
                l = mid
        if self.check_column(image, l):
            return l
        return r

    def find_right_boundry(self, image, start, end):
        l, r = start, end
        while l + 1 < r:
            mid = (l + r) // 2
            if self.check_column(image, mid):
                l = mid
            else:
                r = mid
        if self.check_column(image, r):
            return r
        return l

    def find_top_boundry(self, image, start, end):
        l, r = start, end
        while l + 1 < r:
            mid = (l + r) // 2
            if self.check_row(image, mid):
                r = mid
            else:
                l = mid
        if self.check_row(image, l):
            return l
        return r

    def find_bottom_boundry(self, image, start, end):
        l, r = start, end
        while l + 1 < r:
            mid = (l + r) // 2
            if self.check_row(image, mid):
                l = mid
            else:
                r = mid
        if self.check_row(image, r):
            return r
        return l

    def check_column(self, image, col):
        for i in range(len(image)):
            if image[i][col] == "1":
                return True
        return False

    def check_row(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == "1":
                return True
        return False
