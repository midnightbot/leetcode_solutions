##ss
class Solution:
    def countPoints(self, rings: str) -> int:
        
        ##color, position
        ##[r,g,b]
        
        dicts = [[0,0,0] for x in range(10)]
        print(dicts)
        
        for x in range(0,len(rings),2):
            if rings[x] == "R":
                dicts[int(rings[x+1])][0]+=1
                
            elif rings[x] == "G":
                dicts[int(rings[x+1])][1]+=1
                
            else:
                dicts[int(rings[x+1])][2]+=1
                
        count = 0
        
        for x in range(len(dicts)):
            if dicts[x][0]>0 and dicts[x][1] >0 and dicts[x][2]>0:
                count+=1
        return count
        
