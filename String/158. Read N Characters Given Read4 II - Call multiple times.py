# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:


class Solution:
    def __init__(self):
        self.q = [''] * 4

    def read(self, buf: List[str], n: int) -> int:
        # call buf4 -> buf4 will contain k chars
        # if n > k : n -= k, buf.extend(buf4)
        # if n < k : n = 0, k -= n, the rest of buf4 will push to buf
        # e.g. abcde
        # read(1,2,1,3)
        # buf4  = []
        # buf   = [a]
        # queue = [bcd]
        # k     = 0
        # n.    = 2
        count = 0
        k = 0
        for char in self.q:
            if char != '':
                k += 1
        while n > 0:
            if k == 0:
                k = read4(self.q)
                if k == 0:
                    return count
            buf[count] = self.q.pop(0)
            n -= 1
            self.q.append('')
            k -= 1
            count += 1
        return count
