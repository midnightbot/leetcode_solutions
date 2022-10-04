##ss
class Solution:
    def reverseWords(self, s: str) -> str:
        
        comp = s.split(" ")
        comp = comp[::-1]
        ans = ''
        
        for x in range(len(comp)):
            if comp[x]!='' and comp[x]!=" ":
                ans+=comp[x]+" "
                
        return ans[:-1]
             
        
        
