class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # n = 2
        # 1 3 5
        # 2 4 6

        # n = 3
        # 1   5   9
        # 2 4 6 8
        # 3   7

        # n = 4
        # 1     7       13  row 0  + (n - 1 - 0) * 2  or + (0) * 2
        # 2   6 8    12     row 1  + (n - 1 - 1) * 2  or + (1) * 2
        # 3 5   9  11       row 2  + (n - 1 - 2) * 2  or + (2) * 2
        # 4     10          row 3  + (n - 1 - 3) * 2. or + (3) * 2

        if numRows == 1:
            return s
        res = ''
        n = len(s)
        for i in range(numRows):
            index = i
            if index < n:
                res += s[index]
            while index < n:
                prev = index
                index += (numRows - i - 1) * 2
                if prev != index and index < n:
                    res += s[index]
                prev = index
                index += i * 2
                if prev != index and index < n:
                    res += s[index]
        return res
