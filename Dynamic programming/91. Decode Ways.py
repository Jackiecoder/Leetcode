class Solution:
    def numDecodings(self, s: str) -> int:
        # space optimize
        # time O(n), space O(1)
        n = len(s)
        dp = [0] * 3
        dp[0] = 1
        for i in range(n):
            index = (i + 1) % 3
            dp[index] = 0
            if s[i] != '0':
                dp[index] = dp[index - 1]
            if i >= 1 and '10' <= s[i - 1: i + 1] <= '26':
                dp[index] += dp[index - 2]
        return dp[n % 3]

        '''
        # iteration (bottom up)
        # length == 1 -> "2"   -> 1
        # length == 2 -> "22"  -> 1 + 1 -> length 1 is good + find 2-digits number 
        # length == 3 -> "226" -> 1 + 1 + 1 -> length 1 is good + [22] is good + find '26'
        # dp[i] -> the number of decoding solutions in s[0] to s[i]
        # if s[i] is not '0' -> dp[i] = dp[i - 1], else: dp[i] = 0
        # if "10" <= s[i - 1] to s[i] <= "26": dp[i] += dp[i - 2]
        # return dp[-1]
        # time O(n), space O(n)
        n = len(s)
        dp = [0] * (n + 1) # dp[i] --> reach s[i - 1]
        dp[0] = 1
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if i >= 2 and '10' <= s[i - 2: i] <= '26':
                dp[i] += dp[i - 2]
        return dp[-1]
        '''

        '''
        # recursive + memo (Top down)
        # time O(n), space O(n)
        memo = {}
        return self.numDecodings_from_position(0, s, memo)
        
    def numDecodings_from_position(self, pos, s, memo):
        if pos in memo:
            return memo[pos]
        if pos == len(s):
            memo[pos] = 1
            return 1
        if s[pos] == '0':
            memo[pos] = 0
            return 0
        res = None
        if pos < len(s) - 1 and '10' <= s[pos: pos + 2] <= '26':
            res = self.numDecodings_from_position(pos + 1, s, memo) + self.numDecodings_from_position(pos + 2, s, memo)
        else:
            res = self.numDecodings_from_position(pos + 1, s, memo)
        memo[pos] = res
        return res
        '''

        '''
        # recursive
        # time O(2 ^ n), space O(n)
        return self.numDecodings_from_position(0, s)
    
    def numDecodings_from_position(self, pos, s):
        if pos == len(s):
            return 1
        if s[pos] == '0':
            return 0
        if pos < len(s) - 1 and '10' <= s[pos: pos + 2] <= '26':
            return self.numDecodings_from_position(pos + 1, s) + self.numDecodings_from_position(pos + 2, s)
        else:
            return self.numDecodings_from_position(pos + 1, s)
        '''
