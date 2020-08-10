class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 1. sort by start time
        # 2. when reach an interval, I will check if current earliest end time is smaller than this start time
        #                                               heap -> find  O(logn)
        # 3. return length of heap
        # Time O(nlogn), Space O(n)
        heap = []
        intervals.sort()
        for start, end in intervals:
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)
        return len(heap)
