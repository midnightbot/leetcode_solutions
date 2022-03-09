##ss
from sortedcontainers import SortedList
class SummaryRanges:

    def __init__(self):
        
        self.ans = SortedList()
        self.seen = set()
        

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            self.ans.add(val)
        

    def getIntervals(self) -> List[List[int]]:
        
        result = []
        start = self.ans[0]
        end = self.ans[0]
        for x in range(1,len(self.ans)):
            if self.ans[x] == end + 1:
                end = self.ans[x]
                
            else:
                result.append([start,end])
                start = self.ans[x]
                end = self.ans[x]
                
        result.append([start,end])
        return result
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
