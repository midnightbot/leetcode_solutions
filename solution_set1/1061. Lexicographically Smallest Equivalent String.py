class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        ##a-c-e
        ##b-d
        
        ## eed -> aab
        
        parent = {}
        
        def find_parent(x):
            if x not in parent:
                return x
            
            parent[x] = find_parent(parent[x])
            return parent[x]
        
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                comp = [xs,ys]
                comp = sorted(comp)
                
                parent[comp[1]] = comp[0] ## make larger chr child of smaller chr, as we want lowest lexical order in ans
                
                
        for x in range(len(s1)):
            union(s1[x],s2[x])
            
        ans = ""
        
        for x in range(len(baseStr)):
            ans+= find_parent(baseStr[x])
            
        return ans
