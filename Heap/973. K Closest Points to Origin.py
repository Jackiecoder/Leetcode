class Solution:
    def kClosest_QuickSelect(self, points: List[List[int]], K: int) -> List[List[int]]:
        # quick sort
        # make (dist, (x, y)) list, do quick sort
        # Time O(n), space O(1)
        if K >= len(points):
            return points
        dists = [(x**2 + y**2, (x, y)) for x, y in points]
        self.quick_sort(dists, 0, len(dists) - 1, K)
        return [[x, y] for _, (x, y) in dists[:K]]

    def quick_sort(self, dists, start, end, k):
        if start >= end:
            return
        p = self.partition(dists, start, end)
        if p == k:
            return
        elif p < k:
            return self.quick_sort(dists, p + 1, end, k)
        else:
            return self.quick_sort(dists, start, p - 1, k)

    def partition(self, dists, start, end):
        pivot = dists[end][0]
        left = start
        for i in range(left, end):
            if dists[i][0] <= pivot:
                dists[i], dists[left] = dists[left], dists[i]
                left += 1
        dists[end], dists[left] = dists[left], dists[end]
        return left

    def kClosest_heapify(self, points: List[List[int]], K: int) -> List[List[int]]:
        # heap (heapify + pop K)
        # time O(klogn + n), space O(n)
        if K >= len(points):
            return points
        heap = [(x**2 + y**2, (x, y)) for x, y in points]
        heapq.heapify(heap)
        res = []
        while K > 0:
            dist, coordinate = heapq.heappop(heap)
            res.append(coordinate)
            K -= 1
        return res

    def kClosest_heappush(self, points: List[List[int]], K: int) -> List[List[int]]:
        # heap (push and pop keep size K for heap)
        # we want the large distance pop, use -dist
        # Time O(nlogK), space O(n)
        if K >= len(points):
            return points
        heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (-dist, (x, y)))
            if len(heap) > K:
                heapq.heappop(heap)
        return [[x, y] for _, (x, y) in heap]
