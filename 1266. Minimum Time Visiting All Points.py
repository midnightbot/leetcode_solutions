class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        for x in range(len(points)-1):
            mins1 = abs(points[x][0]-points[x+1][0])
            mins2 = abs(points[x][1]-points[x+1][1])
            mins3 = abs(mins1-mins2)
            mins4 = min(mins1,mins2)
            time+= mins3+mins4
            
            
                
                
                
        return time
        
