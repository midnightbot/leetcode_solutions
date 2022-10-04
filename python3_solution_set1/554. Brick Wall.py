##ss
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        width = sum(wall[0])
        
        #print(width)
        walls = []
        totalends = set()
        for x in range(len(wall)):
            thiswall = set()
            sums= 0
            for y in range(len(wall[x])):
                sums+=wall[x][y]
                thiswall.add(sums)
                totalends.add(sums)
                
            walls.append(thiswall)
            
        #print(walls)
        #print(totalends)
        totalends.remove(width)
        ans = len(walls)
        for x in totalends:
            c = 0
            #print(ans)
            for y in range(len(walls)):
                if x in walls[y]:
                    c+=1
                    
            ans = min(ans, len(walls)-c)
            
            
        return ans
                
        #return -1
        
