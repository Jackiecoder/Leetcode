class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # swap two loops
        # Time O(k * n), Space O(1)
        if not prices:
            return 0
        dp = [0] * 3
        minimum_cost = [prices[0]] * 3
        for i in range(1, len(prices)):
            for k in range(1, 3):
                minimum_cost[k] = min(minimum_cost[k], prices[i] - dp[k - 1])
                dp[k] = max(dp[k], prices[i] - minimum_cost[k])
        return dp[-1]

    def maxProfit_swapLoops(self, prices: List[int]) -> int:
        # swap two loops
        if not prices:
            return 0
        dp = [[0] * 3 for _ in range(len(prices))]
        minimum_cost = [prices[0] for _ in range(3)]
        for i in range(1, len(prices)):
            for k in range(1, 3):
                minimum_cost[k] = min(
                    minimum_cost[k], prices[i] - dp[i - 1][k - 1])
                dp[i][k] = max(dp[i - 1][k], prices[i] - minimum_cost[k])
        return dp[-1][-1]

    def maxProfit_bestSolution(self, prices: List[int]) -> int:
        # because minimum_cost[i] was not been used until dp[k][i] be called
        # thus those two loops can be combined together
        # Time O(k * n), Space O(k * n)
        if not prices:
            return 0
        dp = [[0] * len(prices) for _ in range(3)]
        for k in range(1, 3):
            minimum_cost = prices[0]
            for i in range(1, len(prices)):
                minimum_cost = min(minimum_cost, prices[i] - dp[k - 1][i - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - minimum_cost)
        return dp[-1][-1]

    def maxProfit_twoLoop(self, prices: List[int]) -> int:
        # avoid repeated calculation for minimum cost
        # I can use a array to store minimum cost of day j
        # Time O(k * n), space O(k * n)
        if not prices:
            return 0
        dp = [[0] * len(prices) for _ in range(3)]
        for k in range(1, 3):
            minimum_cost = [prices[0]]
            for i in range(1, len(prices)):
                minimum_cost.append(
                    min(minimum_cost[-1], prices[i] - dp[k - 1][i - 1]))
            for i in range(1, len(prices)):
                dp[k][i] = max(dp[k][i - 1], prices[i] - minimum_cost[i])
        return dp[-1][-1]

    def maxProfit_anotherStraightForward(self, prices: List[int]) -> int:
        # This is another way to understand the straight forward DP
        # Time O(k * n ^ 2), Space O(k * n)
        # ---- TLE -----
        if not prices:
            return 0
        dp = [[0] * len(prices) for _ in range(3)]
        for k in range(1, 3):
            for i in range(1, len(prices)):
                # assuming we need to do one transaction in day i, thus we must buy a stock, so minimum cost is the money that we have earned after buy a new stock.
                minimum_cost = prices[0]
                for j in range(1, i + 1):
                    minimum_cost = min(
                        minimum_cost, prices[j] - dp[k - 1][j - 1])
                dp[k][i] = max(dp[k][i - 1], prices[i] - minimum_cost)
        return dp[-1][-1]

    def maxProfit_straightForwardDP(self, prices: List[int]) -> int:
        # split into subquestions that -> what is the maximum profit from 0 -> i th day if do only one transaction
        #                                 and the maximum profit from i + 1 th day -> n - 1 th day if do only one transaction
        # definition: dp[k][i] -> do k transaction until day i
        # formula: dp[k][i] = dp[k][i - 1] -> do nothing since day i - 1
        #                     dp[k - 1][j] + prices[i] - prices[j]  -> do one transaction since day j to day i, 0 <= j <= i
        #                     because we must do one transaction, so prices[j] must be the smallest
        # Time O(k * n ^ 2), Space O(k * n)
        # ----TLE ----
        if not prices:
            return 0
        dp = [[0] * (len(prices)) for _ in range(3)]
        for k in range(1, 3):
            for i in range(1, len(prices)):
                for j in range(i + 1):
                    dp[k][i] = max(dp[k][i], dp[k][i - 1],
                                   dp[k - 1][j] + prices[i] - prices[j])
        return dp[-1][-1]
