##ss
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        ##simple union find
        parent = [-1 for x in range(len(strs))]
        grps = {"grps": len(strs)}
        def find_parent(x):
            if parent[x] == -1:
                return x
            
            parent[x] = find_parent(parent[x])
            
            return parent[x]
        
        
        def union(x,y):
            xs = find_parent(x)
            ys = find_parent(y)
            
            if xs!=ys:
                parent[xs] = ys
                grps["grps"]-=1
                
                
        for x in range(1,len(strs)):
            for y in range(0,x):
                if self.check_diff(strs[x],strs[y]):
                    union(x,y)
                    
        return grps["grps"]
                
                
    def check_diff(self,str1,str2):
        diff = 0
        
        for x in range(len(str1)):
            if str1[x] != str2[x]:
                diff+=1
        return (diff == 2 or diff == 0)
                
        
        
        
