class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # DFS
        # (s[i] == p[j] or p[j] == '.') -> isMatch(s[i + 1:], p[j:])  or isMatch(s[i:], p[j+2:])
        # if s[i] != p[j]:
        #   1. if  p[j + 1] == '*' -> j += 2
        #   2. else:   -> False
        # once s reach end, and p reach end: true
        #   if s reach end, and p not reach end: -> check if p[j + 1] == '*':
        #                                           if so -> j += 2
        #                                           else  -> False
        # if p[j + 1] == '*':
        #   if s[i] match -> i + 1 or j + 2
        #   else: j + 2
        # else:
        #   if s[i] match -> i + 1 and j + 1

        # e.g.
        #   s = aa
        #   p = a*
        #   i = 0
        #   j = 0
        #   1. i = 1, j = 0
        #       3. i = 2, j = 0
        #           5. i = 2, j = 2 -> True
        #       4. i = 1, j = 2
        #           False
        #   2. i = 0, j = 2 False
        return self.dfs(s, p, len(s), len(p), 0, 0, {})

    def dfs(self, s, p, n, m, i, j, memo):
        # return True or False
        if (i, j) in memo:
            return memo[(i, j)]
        if j > m or i > n or (j == m and i != n):
            return False
        if i == n:
            if j == m:
                return True
            elif j + 1 < m and p[j + 1] == '*':
                return self.dfs(s, p, n, m, i, j + 2, memo)
            else:
                return False
        res = False
        if j + 1 < m and p[j + 1] == '*':
            if s[i] == p[j] or p[j] == '.':
                if self.dfs(s, p, n, m, i + 1, j, memo):
                    res = True
            if self.dfs(s, p, n, m, i, j + 2, memo):
                res = True
        else:
            if s[i] == p[j] or p[j] == '.':
                if self.dfs(s, p, n, m, i + 1, j + 1, memo):
                    res = True
        memo[(i, j)] = res
        return res
