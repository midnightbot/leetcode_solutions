##nss
import math
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        
        parent = [-1] * 100001
        
        def find_parent(x):
            if parent[x] == -1:
                return x
            parent[x] = find_parent(parent[x])
            return parent [x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[ys] = xs
                
        for x in nums:
            for i in range(2,int(math.sqrt(x))+1):
                if x%i == 0:
                    union(i,x)
                    union(x,x//i)
                    
        count = 0
        dicts = {}
        for x in nums:
            xs = find_parent(x)
            count = max(count, 1+dicts.get(xs,0))
            dicts[xs] = 1 + dicts.get(xs,0)
            
        return count
        
