import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ans = []
        temp= []
        
        for x in range(len(points)):
            tempo = math.sqrt(points[x][0]*points[x][0]+points[x][1]*points[x][1])
            
            temp.append((tempo,points[x][0],points[x][1]))
            
        temp = sorted(temp)
        for y in range(k):
            ans.append([temp[y][1],temp[y][2]])
            
        return ans
        
