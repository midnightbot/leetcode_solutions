##ss
class HitCounter:

    def __init__(self):
        self.arr = []
        

    def hit(self, timestamp: int) -> None:
        self.arr.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        ans = 0
        for x in range(len(self.arr)-1,-1,-1):
            if timestamp - self.arr[x] < 300:
                ans+=1
                
            else:
                break
                
        return ans
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
