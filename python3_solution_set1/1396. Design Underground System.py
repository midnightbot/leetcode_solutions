##ss
class UndergroundSystem:

    def __init__(self):
        
        self.ins = {}
        self.out = {}
        self.avg = {}
        
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ins[id] = [stationName,t]
        #print(self.ins)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.out[id] = [stationName,t]
        
        if id in self.ins:
            a,b = self.ins[id]
            c,d = self.out[id]
            #print(a,b)
            key = a +","+ c
            time = d - b
            
        if key in self.avg:
            e,f = self.avg[key]
            e+=time
            f+=1
            
            self.avg[key] =[e,f]
            
        else:
            self.avg[key] = [time,1]
        self.ins.pop(id)
        self.out.pop(id)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        #return 0
        
        key = startStation +","+ endStation
        
        if key in self.avg:
            a,b = self.avg[key]
            
            return a/b
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
