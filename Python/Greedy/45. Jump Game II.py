class Solution:
    def jump(self, nums: List[int]) -> int:
        # BFS
        # queue -> (reachable index in each step)
        # once n - 1 reached, return steps
        # Time O(n^2), space O(n)
        if len(nums) == 1:
            return 0
        queue = deque([0])
        visited = set([0])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                start = queue.popleft()
                for i in range(start + nums[start], start, -1):
                    if i == len(nums) - 1:
                        return steps + 1
                    if i in visited:
                        continue
                    queue.append(i)
                    visited.add(i)
            steps += 1
        return -1

    def jump_dp2(self, nums: List[int]) -> int:
        # dp2 -> TLE
        # dp2 -> change the update function
        # for each j in [i + 1: i + nums[i] + 1] -> dp[j] = min(dp[j], dp[i] + 1)
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            length = nums[i]
            for j in range(i + 1, min(i + length + 1, len(nums))):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[-1]

    def jump_dp1(self, nums: List[int]) -> int:
        # dp1 -> TLE
        # dp[i] = k -> reach index i will need at least k steps
        # dp[i] = min(dp[j] + 1) if j + nums[j] >= i,  0 <= j < i
        # dp[i] initialize to inf -> can't reach
        #   dp[0] = 0

        # Time O(n ^ 2), Space O(n)
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(i):
                if j + nums[j] >= i and dp[j] != float('inf'):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
