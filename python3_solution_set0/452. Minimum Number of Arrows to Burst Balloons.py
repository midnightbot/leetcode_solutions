##ss
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points = sorted(points, key = lambda x:x[0])
        arrows = 1
        
        start = points[0][0]
        end = points[0][1]
        #print(points)
        ##simple greedy burst as many balloons with one arrow, if no overalp found then take new arrow and fit as many balloons again
        for x in range(1,len(points)):
            if points[x][0]>=start and points[x][0]<=end:
                end = min(end,points[x][1])
                
            else:
                arrows+=1
                start = points[x][0]
                end = points[x][1]
                
        return arrows
