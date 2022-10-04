##ss
class StockSpanner:

    def __init__(self):
        self.queue = []
        

    def next(self, price: int) -> int:
        #print(self.queue)
        if len(self.queue) == 0:
            self.queue.append([price,1])
            return 1
        
        else:
            count  = 0
            while self.queue and self.queue[-1][0] <= price:
                thisitem = self.queue.pop()
                count+= thisitem[1]
                
            self.queue.append([price,count+1])
            return self.queue[-1][1]
                

            
            
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
