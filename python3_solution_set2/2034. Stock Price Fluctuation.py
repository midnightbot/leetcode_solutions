import heapq
class StockPrice:

    def __init__(self):
        self.prices = {}
        self.max_tp = -1
        
        self.mins = []
        self.maxs = []
        

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        self.max_tp = max(self.max_tp, timestamp)
        heapq.heappush(self.mins, (price, timestamp))
        heapq.heappush(self.maxs, (-price, timestamp))

    def current(self) -> int:
        return self.prices[self.max_tp]
        

    def maximum(self) -> int:
        while self.prices[self.maxs[0][1]] != -self.maxs[0][0]:
            heapq.heappop(self.maxs)
        return -self.maxs[0][0]
        

    def minimum(self) -> int:
        while self.prices[self.mins[0][1]] != self.mins[0][0]:
            heapq.heappop(self.mins)
        return self.mins[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
