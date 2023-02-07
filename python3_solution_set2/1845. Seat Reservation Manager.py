class SeatManager:
    def __init__(self, n: int):
        self.arr = 1
        self.aval = []
        

    def reserve(self) -> int:
        #print(self.aval)
        if self.aval:
            a = heapq.heappop(self.aval)
            return a
        else:
            self.arr+=1
            return self.arr-1


    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.aval, seatNumber)
        #self.aval.add(seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
