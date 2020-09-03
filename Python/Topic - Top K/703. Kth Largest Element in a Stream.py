class KthLargest:
    '''
    maintain a heap with length = k
    If we call add() n times
    Time O(nlogk), Space O(n)
    The average time of add() is O(logk)
    '''

    def __init__(self, k: int, nums: List[int]):
        heap = nums
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        self.heap = heap
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
