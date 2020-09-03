class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        negative = False
        if x < 0:
            negative = True
            x = -x
        x = str(x)[::-1]
        index = 0
        while index < len(x) and x[index] == '0':
            index += 1
        x = x[index:]

        x = int(x)
        if not -2 ** 31 <= x < 2 ** 31:
            return 0
        if not negative:
            return int(x)
        return -int(x)
