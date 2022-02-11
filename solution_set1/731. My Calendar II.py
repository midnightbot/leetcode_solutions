##ss
class MyCalendarTwo:

    def __init__(self):
        self.single = []
        self.double = []
        

    def book(self, start: int, end: int) -> bool:
        
        ans = True
        for x in range(len(self.double)):
            if start < self.double[x][1] and end > self.double[x][0]:
                ans = False
        if ans==True:    
            for x in range(len(self.single)):
                if start < self.single[x][1] and end > self.single[x][0]:
                    self.double.append([max(self.single[x][0],start),min(self.single[x][1],end)])
                
            self.single.append([start,end])
        #print(self.single,"----",self.double,"--",[start,end])
        return ans
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
