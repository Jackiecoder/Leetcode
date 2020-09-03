def wordBreak_topDown(self, s: str, wordDict: List[str]) -> List[str]:
    # --- top down ---
    # use dfs -> find all possible result and save them
    # e.g. ->
    # "catsanddog"
    # ["cat", "cats", "and", "sand", "dog"]
    # dog + <results of "catsand">
    #          -> and + <results of "cats">
    #             sand + <results of "cat">
    res = self.dfs(s, set(wordDict), {})
    if not res:
        return []
    return [' '.join(sub) for sub in res]


def dfs(self, s, words, memo):
    if not s:
        return [[]]
    if s in memo:
        return memo[s]
    res = []
    for i in range(len(s) - 1, -1, -1):
        if s[i:] in words:
            subresult = self.dfs(s[:i], words, memo)
            memo[s] = subresult
            if subresult:
                res.extend([sub + [s[i:]] for sub in subresult])
    if res:
        memo[s] = res
        return res
