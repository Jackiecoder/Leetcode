class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # dfs
        # each time I can choose (1, 2, 3) characters as a number
        #       if first char is '0', this number must be 0.
        # Time O(27)
        res = []
        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, index, path, res):
        if len(path) == 4 or index == len(s):
            if index == len(s) and len(path) == 4:
                res.append('.'.join(path))
            return
        if s[index] == '0':
            # this integer must be '0'
            path.append('0')
            self.dfs(s, index + 1, path, res)
            path.pop()
            return
        # This integer can be 'xyz'
        for length in range(1, 4):
            if index + length - 1 > len(s) - 1 or not 0 <= int(s[index: index + length]) <= 255:
                continue
            val = s[index: index + length]
            path.append(val)
            self.dfs(s, index + length, path, res)
            path.pop()
