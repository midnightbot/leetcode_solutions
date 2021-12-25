##ss
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        ##all points on same line means slope of every point with point0 will be same
        
        temp = self.find_slope(coordinates[0][0],coordinates[1][0],coordinates[0][1],coordinates[1][1])
        for x in range(1,len(coordinates)):
            if temp!= self.find_slope(coordinates[0][0],coordinates[x][0],coordinates[0][1],coordinates[x][1]):
                return False
            
        return True
        
        
        
    def find_slope(self,x1,x2,y1,y2):
        
        if y1 == y2:
            return float('inf')
        
        else:
            return (x1-x2) / (y1-y2)
