from sortedcontainers import SortedDict
class MyCalendarThree:

    ## Simple Line Sweep Algorithm
    def __init__(self):
        self.dicts = SortedDict()
        

    def book(self, start: int, end: int) -> int:
        self.dicts[start] = self.dicts.get(start,0) + 1
        self.dicts[end] = self.dicts.get(end,0) - 1
        
        c = 0
        ans = 0
        for x in self.dicts.values():
            c+=x
            ans = max(ans, c)
            
        return ans
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
