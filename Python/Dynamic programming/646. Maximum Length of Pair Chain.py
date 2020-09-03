class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # sort based on x[0]
        # dp[i] = k --> when chain length = i, k is the min x[1]
        # for (x[0],x[1]), we need to find dp[i] that dp[i] < x[0], and we want i as large as possible --> find largest smaller
        # if we find this i, we can update dp[i + 1] = x[1]
        # time O(n logn), SPACE O(n)
        pairs.sort()
        n = len(pairs)
        dp = [-float('INFINITY')]
        for i, (head, end) in enumerate(pairs):
            if head > dp[-1]:
                dp.append(end)
            else:
                left, right = 0, len(dp) - 1
                while left + 1 < right:
                    mid = (left + right) // 2
                    if dp[mid] < head:
                        left = mid
                    else:
                        right = mid
                # update_index = left + 1
                if dp[right] < head and dp[right + 1] > end:
                    dp[right + 1] = end
                elif dp[left] < head and dp[left + 1] > end:
                    dp[left + 1] = end
        return len(dp) - 1
