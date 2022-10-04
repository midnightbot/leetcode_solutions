#ss
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        ##1st though (points on same line indicates some use of slope)
        
        points = sorted(points, key = lambda x:x[0])
        ans = [] 
        ##ans[x] gives max number of points that are on a line passing through points[x]
        ## therefore final ans is max(ans)
        
        for x in range(len(points)):
            dicts = {} 
            ##keeping a dictionary and comparing all other points with points[x] and seeing which points have same slope. If they have same slope they are on the same line
            ## therefore key of dictinary is the slope and value is number of points on that line having specified slope
            for y in range(x+1,len(points)):
                if self.slope(points[x][0],points[y][0],points[x][1],points[y][1]) in dicts.keys():
                    dicts[self.slope(points[x][0],points[y][0],points[x][1],points[y][1])] +=1
                    
                else:
                    dicts[self.slope(points[x][0],points[y][0],points[x][1],points[y][1])] = 2
                    
            maxs = 1
            for z in dicts.keys():
                maxs = max(maxs, dicts[z])
                
            ans.append(maxs)
            
        return max(ans)
    
    def slope(self,x1,x2,y1,y2):
        
        if y1 == y2:## to avoid divide by 0 error
            return float('inf')
            
        return  (x1-x2) / (y1-y2)
        
