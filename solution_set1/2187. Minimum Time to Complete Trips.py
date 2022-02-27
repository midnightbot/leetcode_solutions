##ss
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        ##solution1 keep on checking for each time what is the total number of trips
        ##whenever trips >= totalTrips return that time
        ##Solution2 whenever we are lineary searching for something in an array, an array is in increasing order, there is always a possibility to use binary search
        #here array is the trips array, as time increases, trips will also increase, hence we can use binary search
        
        ##simple binary search
        
        start = 0
        end = totalTrips * max(time) * 2
        
        while start <  end:
            #print(start,end)
            mid = start + (end - start)//2
            
            trips = 0
            for x in range(len(time)):
                trips+=mid//time[x]
             
            #print(trips)
            if trips == totalTrips:
                end = mid 
            
            
            elif trips > totalTrips:
                end = mid
                
            else:
                start = mid + 1
            
            
        return start
        
