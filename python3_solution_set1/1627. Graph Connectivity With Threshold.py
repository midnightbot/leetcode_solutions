##ss
import math
class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        
        if threshold == 0:
            return [True for x in range(len(queries))]
        ans = [False for x in range(len(queries))]
        
        parent = [-1 for x in range(n+1)]
        #print(queries[9])
        def find_parent(x):
            if parent[x] == -1:
                return x
            
            parent[x] = find_parent(parent[x])
            return parent[x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[min(xs,ys)] = max(xs,ys)
                return True
            
            else:
                return False
            
            
        ##1,2,3,4,5,6
        for x in range(threshold+1,(n+1)//2 + 1):
            vals = x
            
            while vals <= n:
                union(vals,x)
                vals+=x
        newp = []
        
        for x in range(len(parent)):
            newp.append(find_parent(x))
            
        #print(newp)
        for x in range(len(queries)):
            if newp[queries[x][0]] == newp[queries[x][1]]:
                ans[x] = True
                
        return ans
