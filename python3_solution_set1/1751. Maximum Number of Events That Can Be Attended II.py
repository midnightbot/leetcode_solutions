##ss
import bisect
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events = sorted(events, key = lambda x:x[0])
        
        temps = [x[0] for x in events]
        
        for x in range(len(events)):
            
            indx = bisect.bisect_right(temps, events[x][1])
            
            events[x].append(indx)
            
        @cache
        def find_ans(x, k):
            
            if x>= len(events) or k == 0:
                return 0
            
            else:
                return max(find_ans(x+1,k), events[x][2] + find_ans(events[x][3],k-1))
        
        
        return find_ans(0,k)
