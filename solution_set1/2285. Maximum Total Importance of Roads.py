##ss
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        
        ## values 1-n
        ##nodes with highest indegeree should have higher weight
        degree = {x:0 for x in range(n)}
        imp = {}
        for x,y in roads:
            degree[x]+=1
            degree[y]+=1
            
        temp = []
        
        for x in degree:
            temp.append([degree[x],x])
            
        temp = sorted(temp, reverse = True, key = lambda x:x[0])
        
        curr = n
        #print(temp)
        for x,y in temp:
            imp[y] = curr
            curr-=1
            
        ans = 0
        
        for x,y in roads:
            ans+=imp[x] + imp[y]
            
        return ans
        
        
        
