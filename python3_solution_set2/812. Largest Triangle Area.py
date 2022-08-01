##ss
import math
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        def is_valid(x,y,z):
            a = math.dist(points[x],points[y])
            b = math.dist(points[y],points[z])
            c = math.dist(points[x],points[z])
            return (a+b)>c and (a+c)>b and (b+c)>a
        
        def find_area(x,y,z):
            x1 = points[x][0]
            y1 = points[x][1]
            x2 = points[y][0]
            y2 = points[y][1]
            x3 = points[z][0]
            y3 = points[z][1]
            
            if is_valid(x,y,z):
                return abs((x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3)/(2))
            else:
                return -1
            
        
        ans = -1
        for x in range(len(points)-2):
            for y in range(x+1,len(points)-1):
                for z in range(y+1,len(points)):
                    ans = max(ans, find_area(x,y,z))
           
        
        return ans
