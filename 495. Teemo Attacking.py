##ss
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        total = 0
        
        for x in range(len(timeSeries)-1):
            if timeSeries[x+1] - timeSeries[x] < duration:
                total+=timeSeries[x+1]-timeSeries[x]
                
            else:
                total+=duration
                
        return total+duration
        
