##ss
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        if len(pairs) == 0:
            return s
        
        n = len(s)
        parent = [-1 for x in range(len(s))]
               
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
            
            return False
        
        for x in range(len(pairs)):
            union(pairs[x][0],pairs[x][1])
         
        #print(parent)
        newp = [-1 for x in range(len(parent))]
        for x in range(len(parent)):
            newp[x] = find_parent(x)
            
        ans = [-1 for x in range(len(s))]
        
        grps = {}
        for x in range(len(newp)):
            if newp[x] not in grps:
                grps[newp[x]] = {x}
            else:
                grps[newp[x]].add(x)
                
        for x in grps:
            temp = ""
            elem = list(grps[x])
            for z in elem:
                temp+=s[z]
                
            temp = sorted(temp)
            #print(temp)
            elem = sorted(elem)
            for z in range(len(elem)):
                ans[elem[z]] = temp[z]
            
        for x in range(len(ans)):
            if ans[x] == -1:
                ans[x] = s[x]
                
        return "".join(ans)
            
