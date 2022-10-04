##ss
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        ## to go from current -> correct
        
        time = (int(correct[0:2]) - int(current[0:2])) * 60 + (int(correct[3:]) - int(current[3:]))
        
        op = 0
        #print(time)
        while time!=0:
            if time >= 60:
                time-=60
                
            elif time >=15:
                time-=15
                
            elif time >= 5:
                time-=5
                
            elif time >=1:
                time-=1
                
            op+=1
            
        return op
