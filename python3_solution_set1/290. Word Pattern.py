##ss
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        comp = s.split(" ")
        #print(comp)
        dicts = {}
        visited = []
        if len(pattern)!=len(comp):
            return False
        
        for x in range(len(pattern)):
            
            if pattern[x] not in dicts and comp[x] not in visited:
                dicts[pattern[x]] = comp[x]
                visited.append(comp[x])
                
            if pattern[x] not in dicts and comp[x] in visited:
                return False
                
                
            elif pattern[x] in dicts:
                temp = dicts[pattern[x]]
                if temp!=comp[x]:
                    return False
                
        return True
