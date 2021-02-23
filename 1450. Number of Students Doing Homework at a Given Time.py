class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for x in range(len(startTime)):
            if(queryTime>=startTime[x] and queryTime<=endTime[x]):
                count+=1
                
        return count
        
