class UndergroundSystem:

    def __init__(self):
        # user = {id: (start station, start time)}
        # travel = {(start, end): [period]}
        self.user = defaultdict(list)
        self.travel = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.user[id]
        self.travel[(start_station, stationName)].append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        all_period = self.travel[(startStation, endStation)]
        return sum(all_period) / len(all_period)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
