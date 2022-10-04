##ss
import math
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ##dist(i,j) == dist(i,k)
        
        dist = {}
        ans = 0
        for x in range(len(points)):
            for y in range(len(points)):
                if y!=x:
                    d = self.dist(points[x],points[y])
                    if str(points[x][0])+","+str(points[x][1])+","+str(d) in dist:
                        dist[str(points[x][0])+","+str(points[x][1])+","+str(d)]+=1
                        
                    else:
                        dist[str(points[x][0])+","+str(points[x][1])+","+str(d)] = 1
                        
        for x in dist:
            if dist[x] > 1:
                ans+= dist[x] * (dist[x]-1)
                
        return ans
                
                
                
                
    def dist(self,p1,p2):
        
        px = p1[0]
        py = p1[1]
        
        qx = p2[0]
        qy = p2[1]
        
        return math.sqrt((px-qx)**2 + (py-qy)**2)
        
