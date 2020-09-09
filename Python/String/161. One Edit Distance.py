class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        # add -> t skip one step
        # delete -> s skip one step
        # replace -> s, p move one step forward at same time
        n, m = len(s), len(t)
        # if not m: return n == 1
        # if not n: return m == 1
        i, j = 0, 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            return s[i:] == t[j + 1:] or s[i + 1:] == t[j:] or s[i + 1:] == t[j + 1:]
        if i == n:
            return j + 1 == m
        if j == m:
            return i + 1 == n
        return False
