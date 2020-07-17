class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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
