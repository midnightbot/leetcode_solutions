##ss
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        rooms = []
        rooms.append(0)
        intervals = sorted(intervals, key = lambda x:x[0])
        print(intervals)
        for x in range(len(intervals)):
            
            adj = False
            for y in range(len(rooms)-1,-1,-1):
                if intervals[x][0] >= rooms[y]:
                    adj = True
                    rooms[y] = intervals[x][1]
                    break
                    
            if adj == False:
                rooms.append(intervals[x][1])
            #print(rooms)    
        return len(rooms)
            
        
