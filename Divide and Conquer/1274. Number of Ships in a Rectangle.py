# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # divide into 4 part
        # x1, y1 = bottomleft
        # (x1, x2, y1, y2) -> (x1, (x1 + x2)/2, y1, (y1 + y2)/2)
        x1, y1 = bottomLeft.x, bottomLeft.y
        x2, y2 = topRight.x, topRight.y
        if x1 > x2 or y1 > y2 or not sea.hasShips(topRight, bottomLeft):
            return 0
        if x1 == x2 and y1 == y2:
            return 1
        res = 0
        mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
        res += self.countShips(sea, Point(mid_x, mid_y), Point(x1, y1))
        res += self.countShips(sea, Point(x2, y2), Point(mid_x + 1, mid_y + 1))
        res += self.countShips(sea, Point(mid_x, y2), Point(x1, mid_y + 1))
        res += self.countShips(sea, Point(x2, mid_y), Point(mid_x + 1, y1))
        return res
