##ss
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        ans = ""
        prev = 0
        spaces.append(len(s))
        for x in range(len(spaces)):
            ans+= s[prev:spaces[x]]
            ans+=" "
            prev = spaces[x]
            
            
        return ans[0:len(ans)-1]
             
        
