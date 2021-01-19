class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # hash set
        # store the sum of A and B in a hash set, and store the sum of C and D in another hash set.
        # time O(n ** 2), space O(n ** 2)
        val_to_cnt = defaultdict(int)
        for i in A:
            for j in B:
                val_to_cnt[i + j] += 1
        res = 0
        for i in C:
            for j in D:
                res += val_to_cnt.get(-(i + j), 0)
        return res
