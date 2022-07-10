##ss
class SmallestInfiniteSet:

    def __init__(self):
        self.q = []
        self.seen = set()

        for x in range(1,1001):
            heapq.heappush(self.q,x)
            self.seen.add(x)
    def popSmallest(self) -> int:
        
        top =  heapq.heappop(self.q)
        self.seen.remove(top)
        return top
    
    def addBack(self, num: int) -> None:
        
        if num not in self.seen:
            heapq.heappush(self.q,num)
            self.seen.add(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
