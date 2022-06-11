import bisect
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        
        ## simple dp
        ## if I take this ride, find optimal ans for remaning valid rides
        ## else dont take this ride
        
        rides = sorted(rides, key = lambda x:x[0])
        #print(rides)
        
        temps = [x[0] for x in rides]
        
        for x in range(len(rides)):
            indcs = bisect.bisect_left(temps, rides[x][1])
            rides[x].append(indcs)
            
        #print(rides)
        @lru_cache(None)
        def find_ans(indx):
            if indx>=len(rides):
                return 0
            
            else:
                return max(find_ans(indx+1), rides[indx][1] - rides[indx][0] + rides[indx][2] + find_ans(rides[indx][3]))
            
        return find_ans(0)
            
