class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # (start, end) time
        # if next start time is smaller than the end, -> need another room
        # else if there is one meeting room that already end -> update its end time
        #
        # e.g.  [[0, 30],[5, 10],[15, 20]]
        # meeting room = [30, 20] # record all end time
        # return len(meeting_room)

        # if use this method -> input intervals must be sorted by the start time increasingly
        # time O(n), space O(n)

        intervals.sort(key=lambda x: x[0])
        meeting_room = []
        for start, end in intervals:
            if not meeting_room:
                meeting_room.append(end)
                continue
            min_endTime = heapq.heappop(meeting_room)
            if min_endTime > start:
                heapq.heappush(meeting_room, min_endTime)
            heapq.heappush(meeting_room, end)
        return len(meeting_room)
