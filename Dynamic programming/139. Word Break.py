class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp - top down
        # 1. dfs
        # subproblem -> s[:i] is valid and s[i:] in wordDict
        # leet -> is valid ? + code in dict?
        # 2. repeated calculation
        # e.g. [code, co, de]
        #   code -> leet?
        #   co + de -> leet?
        # memo[i] -> s[:i] is valid
        if not wordDict:
            return False
        m = len(max(wordDict, key=len))
        return self.dfs(s, set(wordDict), {}, m)

    def dfs(self, s, words, memo, m):
        if not s:
            return True

        if len(s) in memo:
            return memo[len(s)]

        for i in range(len(s) - 1, -1, -1):
            if len(s) - i > m:
                break
            if s[i:] in words and self.dfs(s[:i], words, memo, m):
                memo[i] = True
                return True
        memo[len(s)] = False
        return False

    def wordBreak_bottomUp(self, s: str, wordDict: List[str]) -> bool:
        #dp [T, F, F, F, F, F, F, F, F]
        #s     [l, e, e, t, c, o, d, e]
        #       i. = 1
        #       i_s = 0
        n = len(s)
        # dp[i] -> s[:i] can can be segmented into sequence
        dp = [False] * (n + 1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(1, n + 1):
            if not dp[i - 1]:
                continue
            for j in range(i, n + 1):
                # print(dp,s[i-1:j])
                if s[i - 1: j] in wordDict:
                    dp[j] = True
        return dp[-1]
