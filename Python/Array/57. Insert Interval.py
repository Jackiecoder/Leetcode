class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # travel through
        # merge and move on
        # O(n)
        res, new = [], newInterval
        for i, interval in enumerate(intervals):
            if interval[1] < new[0]:
                # 1. [interval] [new]
                res.append(interval)
            elif new[1] < interval[0]:
                # 2. [new] [interval]
                res.append(new)
                return res + intervals[i:]
            else:
                # 3. have overlapping
                new[0] = min(new[0], interval[0])
                new[1] = max(new[1], interval[1])
        res.append(new)
        return res
