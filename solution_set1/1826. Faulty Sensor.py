##ss
class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        
        
        for x in range(len(sensor1)-1):
            if sensor1[x]!=sensor2[x]:
                if sensor1[x+1:] == sensor2[x:len(sensor2)-1] and sensor2[x+1:] != sensor1[x:len(sensor1)-1]:
                    return 2
                elif sensor2[x+1:] == sensor1[x:len(sensor1)-1] and sensor1[x+1:] != sensor2[x:len(sensor2)-1]:
                    return 1
                else:
                    return -1
                
            
        return -1
        
