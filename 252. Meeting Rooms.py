class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals = sorted(intervals)
        
        for x in range(len(intervals)-1):
            if intervals[x][1] > intervals[x+1][0]:
                return False
            
            
        return True
        
