class Solution:
    def isMatc(self, s: str, p: str) -> bool:
        # travel p
        # if meet '?' -> s and p move 1 step forward
        # if meet '*' -> s move 1 step or p move 1 step forward
        # if s and p reach end at same time -> True
        #   else: False
        # use a memo to remeber result
        return self.dfs(s, p, 0, 0, {})

    def dfs(self, s, p, i, j, memo):
        # return True if s[i:] match p[j:]
        if (i, j) in memo:
            return memo[(i, j)]
        if j == len(p):
            return i == len(s)
        res = False
        if i < len(s) and (s[i] == p[j] or p[j] == '?'):
            if self.dfs(s, p, i + 1, j + 1, memo):
                res = True
        if p[j] == '*':
            if self.dfs(s, p, i, j + 1, memo) or (i < len(s) and self.dfs(s, p, i + 1, j, memo)):
                res = True
        memo[(i, j)] = res
        return res
