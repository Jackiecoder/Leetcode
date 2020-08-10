class Word:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # target: O(nlogk)
        # maintain a size k heap
        # heap = [(freq, string)] so the heap will pop out smallest freq, and largest string first.
        # so peak of heap is the tuple with (small freq, and large string)
        # then in the heap, just maintain a size k heap
        counter = Counter(words)
        heap = []
        for word, freq in counter.items():
            heapq.heappush(heap, Word(word, freq))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            word = heapq.heappop(heap)
            res.append(word.word)
        return res[::-1]

    def topKFrequent_klogn(self, words: List[str], k: int) -> List[str]:
        # hash table = {word: freq}
        # then use priority queue to find top k freq
        # -> implement: heapify (-freq, string), pop k times
        # time O(n + klogn), space O(n)
        counter = Counter(words)
        heap = [(-freq, word) for word, freq in counter.items()]
        heapq.heapify(heap)  # O(n)
        res = []
        for _ in range(k):                # O(k)
            _, word = heapq.heappop(heap)  # O(logn)
            res.append(word)
        return res
