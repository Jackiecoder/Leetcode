class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # we want high frequency and low word order
        word_count = collections.Counter(words)
        heap = [(-count, word) for word, count in word_count.items()]
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            if not heap:
                break
            res.append(heapq.heappop(heap)[1])
        return res
