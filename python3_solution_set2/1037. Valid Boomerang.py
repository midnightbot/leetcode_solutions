class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        def pt_counter(points):
            ans = set()
            
            for x,y in points:
                ans.add((x,y))
                
            return len(ans)
        
        
        def find_slope(a,b):
            x1 = a[0]
            y1 = a[1]
            x2 = b[0]
            y2 = b[1]
            if (x2-x1) == 0:
                return float('inf')
            return (y2-y1)/(x2-x1)
        
        q,w,e = points[0], points[1], points[2]
        return find_slope(q,w) != find_slope(w,e) and pt_counter(points) == 3
        
