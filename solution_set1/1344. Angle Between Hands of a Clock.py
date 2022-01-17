##ss
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        ##per gap 360/12  30 degree
        ##hour hand += mins / 60
        ##calculate angle from 12 to both hands and then subt
        ##1/2 degree per minute
        
        mins_angles = ((minutes) / 60) * 360
        
        #print(mins_angles)
        
        hours = (hour - 12) % 12
        hours_angles = hours * 30 + minutes * 1/2
        #print(mins_angles,hours_angles)
        
        
        ang =  max(mins_angles-hours_angles,hours_angles-mins_angles)
        
        return min(ang,360-ang)
