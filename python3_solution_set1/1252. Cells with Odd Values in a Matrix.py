##ss
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        rdict = {}
        cdict = {}
        for x in range(m):
            rdict[x] = 0
            
        for x in range(n):
            cdict[x] = 0
        for x in range(len(indices)):
            
            rdict[indices[x][0]]+=1
            cdict[indices[x][1]]+=1

                
                
        #print(rdict,cdict)
        ##iterate over each row to see which elem are even and which are odd
        
        count = 0
        
        for x in rdict:
            op = rdict[x]
            
            for y in cdict:
                if op%2==0:
                    if cdict[y]%2!=0:
                        count+=1
                        
                else:
                    if cdict[y]%2==0:
                        count+=1
                        
                        
        return count
        
        
        
