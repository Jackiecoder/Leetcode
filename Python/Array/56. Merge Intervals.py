class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # travel through the intervals
        # range = [s, e]
        #   if start < cur.end -> merge
        #   else: 1. store range-> res,
        #         2. range = cur
        # Time O(nlogn), Space O(n)
        if not intervals:
            return []
        res = []
        intervals.sort()
        interval_range = intervals[0]
        for start, end in intervals:
            if interval_range[1] >= start:
                # merge
                interval_range[1] = max(interval_range[1], end)
            else:
                # new interval_range
                res.append(interval_range)
                interval_range = [start, end]
        res.append(interval_range)
        return res
