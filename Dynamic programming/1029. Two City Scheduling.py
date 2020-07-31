class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # for each person has a choice that choose A or B
        # so the subproblem:
        #   for the condition i people choose A
        #                 and j people choose B

        #   when we try to choose the i+j - th city, we will choose from
        #   1. minimum cost of (i - 1 to A and j to B) + costs[i+j][0]
        #   2. minimum cost of (i to A and j - 1 to B) + costs[i+j][1]
        # define a 2D grid
        #   defination: dp[i][j] -> minimum cost of i people choose A and j people choose B
        #       i -> [0, n], j -> [0, n]
        #   function: dp[i][j] = min(dp[i - 1][j], dp[i][j - 1])
        #   initialize: dp[0][j] = sum(costs[0:j][1])
        #               dp[i][0] = sum(costs[0:i][0])
        #   return : dp[n][n]
        n = len(costs)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i, (cost_A, cost_B) in enumerate(costs):
            dp[i + 1][0] = dp[i][0] + cost_A
            dp[0][i + 1] = dp[0][i] + cost_B
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i + j > n:
                    continue
                dp[i][j] = min(dp[i - 1][j] + costs[i + j - 1][0],
                               dp[i][j - 1] + costs[i + j - 1][1])
        return dp[n//2][n//2]
