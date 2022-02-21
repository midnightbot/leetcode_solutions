##ss
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        ans = [0 for x in range(n+1)]
        
        for x in range(len(bookings)):
            ans[bookings[x][0]-1]+=bookings[x][2]
            ans[bookings[x][1]]-=bookings[x][2]
            
        for x in range(1,len(ans)):
            ans[x]+=ans[x-1]
            
        return ans[:-1]
        
