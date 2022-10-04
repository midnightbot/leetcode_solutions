class Solution:
    def reverseWords(self, s: str) -> str:
        
        temp  = s.split( )
        for x in range(len(temp)):
            temp[x] = temp[x][::-1]
            
        ans = ""
        for x in range(len(temp)):
            ans+= temp[x]
            ans+=" "
            
        return ans[0:len(ans)-1]
