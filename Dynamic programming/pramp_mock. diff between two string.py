def diffBetweenTwoStrings(source, target):
    """
    @param source: str
    @param target: str
    @return: str[]
    """
    # two choices: A move forward or B move forward
    # if it is same: move forward together
    # else: 1. remove A, 2. add B
    #   REQUEIREMENTS:  1. choose the minimum steps, 2. choose remove first
    # [aaaa]
    # [bbbb]
    # i, j =     0, 0
    # i, j = 0, 1 or        1, 0
    #    0, 2 or 1, 1    1, 1.  2, 0
    # res = []
    # dp[i][j] = steps will need, dp[n][...] -> A reach end
    # if A[i] == B[j]: dp[i][j] = dp[i + 1][j + 1] , res = [A[i]] + res
    #            else:
    #               if dp[i + 1][j] <= dp[i][j + 1]:  dp[i][j] = dp[i + 1][j], res +=
    #               else:   dp[i][j] = dp[i][j + 1]
    # print(source)
    # print(target)
    m, n = len(source), len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        dp[i][n] = m - i
    for j in range(n):
        dp[m][j] = n - j
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if source[i] == target[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1])

    # for i in range(m):
    #     print(dp[i])
    i, j = 0, 0
    res = []
    while i < m and j < n:
        # print(i, j)
        # print(res)
        if source[i] == target[j]:
            res.append(source[i])
            i += 1
            j += 1
        else:
            if dp[i + 1][j] <= dp[i][j + 1]:
                # do remove
                res.append('-' + source[i])
                i += 1
            else:
                # do add
                res.append('+' + target[j])
                j += 1
    # print(i, j)
    # print(res)
    while j < n:
        res.append('+' + target[j])
        j += 1
    # while i < m:
    #     res.append('-' + source[i])
    #     i += 1
    return res
