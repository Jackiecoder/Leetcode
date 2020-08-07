class Leaderboard:
    '''
    use hash table to store {id: score}
    '''

    def __init__(self):
        self.board = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    def top(self, K: int) -> int:
        # Nlogk -> priority queue
        heap = []
        for key, val in self.board.items():
            heapq.heappush(heap, val)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
