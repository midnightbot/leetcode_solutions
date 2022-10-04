class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        parent = [-1 for x in range(n)]
        ans = []
        grp = {}
        for x in range(n):
            grp[x] = set()
            grp[x].add(x)
            
        res = {}
        for x in range(n):
            res[x] = set()
        for x in range(len(restrictions)):
            
            res[restrictions[x][0]].add(restrictions[x][1])

            
            res[restrictions[x][1]].add(restrictions[x][0])
        #print(grp)
        def find_parent(x):
            if parent[x] ==-1:
                return x
            
            parent[x] = find_parent(parent[x])
            return parent[x]
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[xs] = ys
                grp[ys] = grp[ys] | grp[xs]
                res[ys] = res[ys] | res[xs]
                
        #print(res)
        for x,y in requests:
            xs = find_parent(x)
            ys = find_parent(y)
            
            result = True
            if res[xs]&grp[ys] or res[ys]&grp[xs]:
                result = False
                
            if result == True:
                union(y,x)
                ans.append(True)
                
            else:
                ans.append(False)
                    
        return ans
                    
