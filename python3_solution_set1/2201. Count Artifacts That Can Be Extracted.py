##ss
class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        
        
        space = {}
        pos = {}
        count = 0
        for x in range(len(artifacts)):
            #s = abs(artifacts[x][0] - artifacts[x][2] + 1) * abs(artifacts[x][1] - artifacts[x][3] + 1)
            
            s = 0
            
            for r in range(artifacts[x][0], artifacts[x][2] + 1):
                for c in range(artifacts[x][1], artifacts[x][3] + 1):
                    pos[str(r)+","+str(c)] = x
                    s+=1
                    
            space[x] = s
                    
        for x in range(len(dig)):
            if str(dig[x][0]) + "," + str(dig[x][1]) in pos:
                space[pos[str(dig[x][0]) + "," + str(dig[x][1])]] -=1
                
        count = 0
        
        for x in space:
            if space[x] == 0:
                count+=1
                
        return count
            
            
            
        
