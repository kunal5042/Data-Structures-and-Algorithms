# Question: https://leetcode.com/problems/design-underground-system/description/
# Medium


class UndergroundSystem:
    # O(1) time and O(query) space
    
    def __init__(self):
        self.check_ins = {}
        self.travels = {}

    def checkIn(self, id: int, station_name: str, t: int) -> None:
        self.check_ins[id] = (station_name, t)

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        route = (start_station, end_station)
        self.travels[route] = (
            self.travels.get(route, (0, 0))[0] + (t - start_time),
            self.travels.get(route, (0, 0))[1] + 1
        )

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        route = (start_station, end_station)
        return self.travels[route][0] / self.travels[route][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


# May 31, 2023

'''

# Kunal Wadhwa

'''