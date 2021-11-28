##ss
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        ans  = ""
        
        for x in range(len(order)):
            if order[x] in s:
                counts = s.count(order[x])
                for z in range(counts):
                    ans+=order[x]
        
        
        for x in range(len(s)):
            if s[x] not in ans:
                counts = s.count(s[x])
                for z in range(counts):
                    ans+=s[x]
                
        return (ans)
                
        
        
