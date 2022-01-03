##ss
import queue
class MyCalendar:

    def __init__(self):
        self.cal = []
        #self.cal.put((0,0))
        
    def book(self, start: int, end: int) -> bool:
        #print(self.cal.queue)
        #print(self.cal)
        if len(self.cal) == 0:
            self.cal.append((-float('inf'),-float('inf')))
            self.cal.append((start,end))
            self.cal.append((float('inf'),float('inf')))
            return True
        
        else:
            for x in range(len(self.cal)):
                if self.cal[x][0] >= end and self.cal[x-1][1] <= start: ##sufficient space to insert this time
                    self.cal.insert(x,(start,end))
                    return True
                
                
            return False
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
