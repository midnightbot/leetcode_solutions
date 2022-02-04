##ss
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        
        if p1==p2==p3==p4:
            return False
        dist = []
        def distance(p1,p2):
            
            d = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
            
            dist.append(d)
            
        points = [p1,p2,p3,p4]
        
        for x in range(len(points)-1):
            for y in range(x+1,len(points)):
                distance(points[x],points[y])
                
        dist = sorted(dist)
        #print(dist)
            
        return dist[0] == dist[1] == dist[2] == dist[3] and dist[4] == dist[5]
