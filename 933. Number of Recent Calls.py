##ss
class RecentCounter:

    def __init__(self):
        self.queue = []
        
        

    def ping(self, t: int) -> int:
        
        self.queue.append(t)
        if t <= 3000:
            return len(self.queue)
        
        else:
            for x in range(len(self.queue)-1,-1,-1):
                if self.queue[len(self.queue)-1]-self.queue[x] > 3000:
                    break
            
            if x==0 and self.queue[len(self.queue)-1]-self.queue[0] <=3000:
                return len(self.queue)-(x)
            
            else:
                return len(self.queue)-(x+1)
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
