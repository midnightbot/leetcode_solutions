## ss 
## Time Complexity : O(n*logn)
## Space Complexit : O(n)
import heapq
class Solution:
    def mostBooked(self, n_room: int, meetings: List[List[int]]) -> int:
        
        meetings = sorted(meetings, key = lambda x:x[0])
        #print(meetings)
        
        room = []
        end_times = []
        times_used = [0 for x in range(n_room)]
        n = len(meetings)
        
        indx = 0
        
        for x in range(n_room):
            heapq.heappush(room,x)
            
        while indx < n:
            start,end = meetings[indx][0], meetings[indx][1]
            #print(end_times,room)
            b = True
            while b and end_times:
                end_timing, new_room = heapq.heappop(end_times)
                if end_timing <= start:
                    heapq.heappush(room, new_room)

                else:
                    heapq.heappush(end_times, [end_timing, new_room])
                    b = False
            if room:
                new_meeting_room = heapq.heappop(room)
                #print(new_meeting_room)
                times_used[new_meeting_room]+=1
                heapq.heappush(end_times, [end,new_meeting_room])
                indx+=1
                
            else:
                end_timing, new_room = heapq.heappop(end_times)
                #print(end_timing, start, end_times, room)
                if end_timing > start:
                    times_used[new_room]+=1
                    heapq.heappush(end_times, [end_timing + (end-start), new_room])
                    indx+=1
                    
                else:
                    heapq.heappush(room, new_room)
                    #print(room)
                    b = True
                    while b and end_times:
                        end_timing, new_room = heapq.heappop(end_times)
                        if end_timing <= start:
                            heapq.heappush(room, new_room)
                    
                        else:
                            heapq.heappush(end_times, [end_timing, new_room])
                            b = False
               
        return times_used.index(max(times_used))
