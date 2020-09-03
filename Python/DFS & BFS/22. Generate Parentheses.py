class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # count_left  = 0
        # count_right = 0
        # if equal -> only add left
        #   elif left > right -> add left or right
        # if left reach end:
        #    add N-right * ')' to string
        #           ''   , 0, 0
        #           '('  , 1, 0
        #       '((', 2,0.              '()'  1, 1
        #    '(((' 3,0. '(()' 2, 1.       '()(' 2, 1
        #   '((()))' 3,3

        # dfs ->
        # Time O(4 ^ n) , space O(n^2)
        res = []
        self.dfs(n, '', 0, 0, res)
        return res

    def dfs(self, n, path, left, right, res):
        if left == n:
            path += ')' * (n - right)
            res.append(path)
            return
        if left > right:
            self.dfs(n, path + ')', left, right + 1, res)
        self.dfs(n, path + '(', left + 1, right, res)
