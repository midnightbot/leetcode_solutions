##ss
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        
        ##for every point check every point in visited array and form a line between them diagonal
        ##x1,y1   x2,y2 be the two points then x1y1 x2y2 x1y2 and x2y1 will form a rectangle
        
        ans = float('inf')
        visited = set()
        
        for x1,y1 in points:
            for x2,y2 in visited:
                if (x1,y2) in visited and (x2,y1) in visited:
                    ans = min(ans, abs(x1-x2) * abs(y1-y2))
               
            visited.add((x1,y1))
        return ans if ans!=float('inf') else 0
                    
        
