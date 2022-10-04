import math
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        ans = []
        
        for y in range(len(queries)):
            count = 0
            for x in range(len(points)):
                temp = math.sqrt((points[x][0]-queries[y][0])**2 + (points[x][1]-queries[y][1])**2)
                if temp <= queries[y][2]:
                    count+=1
                    
            ans.append(count)
            
            
        return ans
                    
                
                
            
        
