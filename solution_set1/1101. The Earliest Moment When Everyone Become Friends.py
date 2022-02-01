##ss
import math
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        parent = [-1] * n
        grps = n
        def find_parent(x):
            #print(parent)
            if parent[x] == -1:
                return x
            parent[x] = find_parent(parent[x])
            
            return parent[x]
        
        
        def union(x,y):
            
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[ys] = xs
                return True

                
        
            return False
                
                
                
        logs = sorted(logs, key = lambda x:x[0])
        
        for x in range(len(logs)):
            min1 = min(logs[x][1],logs[x][2])
            max1 = max(logs[x][1],logs[x][2])
            a = union(min1,max1)
            
            if a == True:
                grps-=1
                
            if grps == 1:
                return logs[x][0]
            
            
        return -1
        
        
                
                
        
        
