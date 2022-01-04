##ss
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        times = []
        
        for x in range(len(trips)):
            times.append([trips[x][1],trips[x][0]])
            times.append([trips[x][2],-trips[x][0]])
            
            
        times = sorted(times)
        cap = 0
        for x in range(len(times)):
            cap+=times[x][1]
            if cap > capacity:
                return False
            
            
        return True
        
