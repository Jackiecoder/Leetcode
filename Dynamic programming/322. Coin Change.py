class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # top down dp
        # coinChange -> return the minimum number of coins are needed for the amount
        res = self.coinChange_wz_memo(coins, amount, {})
        return res if res != float('inf') else -1

    def coinChange_wz_memo(self, coins, amount, memo):
        if amount in memo:
            return memo[amount]
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0

        res = float('inf')
        for coin in coins:
            res = min(res, self.coinChange_wz_memo(
                coins, amount - coin, memo) + 1)
        memo[amount] = res
        return res

    def coinChange_bottomUp(self, coins: List[int], amount: int) -> int:
        # bottom up dp
        # dp[i] -> the number of coins are needed with amount = i
        # dp[i] = dp[i - coin] + 1, dp[i - coin] >= 0
        # initialization dp[i] = -1
        # e.g. coins = [1,2,5]
        # dp = [0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
        # Time O(amount * len(coins)), space O(amount)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

    def coinChange_bfs(self, coins: List[int], amount: int) -> int:
        # BFS
        coins.sort(reverse=True)
        queue = deque([amount])
        num_of_coin = 0
        visited = set([amount])
        while queue:
            for _ in range(len(queue)):
                # all amount in queue must be un-visited
                amount = queue.popleft()
                if amount == 0:
                    return num_of_coin
                if amount > 0:
                    for coin in coins:
                        if amount - coin in visited:
                            continue
                        queue.append(amount - coin)
                        visited.add(amount - coin)
            num_of_coin += 1
        return -1
