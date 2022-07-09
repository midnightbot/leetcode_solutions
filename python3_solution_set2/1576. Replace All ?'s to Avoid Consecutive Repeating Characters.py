##ss
class Solution:
    def modifyString(self, s: str) -> str:
        
        opt = ['a','b','c']
        temp = [x for x in s]
        
        temp.insert(0,'z')
        temp.append('z')
        for x in range(1,len(temp)-1):
            if temp[x] == '?':
                seen = set()
                seen.add(temp[x-1])
                seen.add(temp[x+1])
                
                for it in opt:
                    if it not in seen:
                        temp[x] = it
                        break
            
        return "".join(temp[1:-1])
            
            
        
