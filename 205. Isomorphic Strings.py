##ss
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        dicts = {}
        visited = []
        if len(s)!=len(t):
            return False
        
        for x in range(len(s)):
            if s[x] in dicts.keys() and (dicts[s[x]]!=t[x]):
                return False
            
            if s[x] not in dicts.keys():
                dicts[s[x]] = t[x]
                
        #print(dicts)
        visited = []
        
        for x in dicts.keys():
            if dicts[x] not in visited:
                visited.append(dicts[x])
                
            else:
                return False
            
        return True
            
        
