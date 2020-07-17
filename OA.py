def mario(mission):
    # dp[i] = max(dp[j] + mission[j] * mission[i] * (i - j))
    # time O(n^2), space O(n)
    if not mission:
        return 0

    dp = [0] * len(mission)

    for i in range(len(mission)):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] + mission[i] *
                        mission[j] * ((i - j) ** 2))
    return max(dp) if max(dp) > 0 else 0


testcase = [1, 10, -1, 0, 0, 0, -20]
res = mario(testcase)
print(res)
