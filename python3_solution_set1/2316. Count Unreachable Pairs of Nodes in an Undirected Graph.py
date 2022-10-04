class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        ## n nodes
        ## 0 to n-1 nodes
        ## union find, find number of components, 
        ## nodes of one compoent not connected to other
        
        parent = [-1 for x in range(n)]
        grps = {}
        def find_parent(x):
            if parent[x] == -1 or parent[x] == x:
                return x
            parent[x] = find_parent(parent[x])
            return parent[x]
        
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[min(xs,ys)] = max(xs,ys)
                return True
            
            return False
        
        
        for x,y in edges:
            union(x,y)
         
        #print(parent)
        for x in range(len(parent)):
            if parent[x] == -1:
                parent[x] = x
                
        for x in range(len(parent)):
            parent[x] = find_parent(parent[x])
            
        temp = list(Counter(parent).values())

        if len(temp) <= 1:
            return 0
        else:
            c = 0
            
            for x in range(len(temp)):
                c+= temp[x] * (n-temp[x])
            return c//2
