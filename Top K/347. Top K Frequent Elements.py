class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # quick sort
        # Time O(nlogn), space O(1)
        counter = [(freq, num) for num, freq in Counter(nums).items()]
        self.quickSort(counter, 0, len(counter) - 1)
        return [num for freq, num in counter][:k]

    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] > pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def topKFrequent_bucketSort(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        # Time O(n), Space O(n)
        bucket = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)
        for num, freq in counter.items():
            bucket[freq].append(num)
        res = []
        for i in range(len(nums), -1, -1):
            res.extend(bucket[i])
            if len(res) == k:
                break
        return res

    def topKFrequent_heappop(self, nums: List[int], k: int) -> List[int]:
        # 1.5 priority queue
        # heap = []
        #  push (freq, num) to heap, and pop top if heap is full
        # Time O(nlogk), space O(k)
        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            _, num = heapq.heappop(heap)
            res.append(num)
        return res[::-1]

    def topKFrequent_heapify(self, nums: List[int], k: int) -> List[int]:
        # 1. priority queue -> implement by heap
        # heap = [(-freq, num)]
        #  push to heap and pop out top k
        # Time O(n + klogn), space O(n)
        counter = Counter(nums)
        heap = [(-freq, val) for val, freq in counter.items()]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            _, val = heapq.heappop(heap)
            res.append(val)
        return res
