##ss
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        small = float('inf')
        indx = -1
        
        for z in range(len(points)):
            if points[z][0] == x or points[z][1] == y:
                
                dist = abs(x-points[z][0]) + abs(y-points[z][1])
                
                if dist < small:
                    small = dist
                    indx = z
                    
        return indx
        
