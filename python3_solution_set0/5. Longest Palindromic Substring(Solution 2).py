##ss
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if s== None or len(s) < 1:
            return ""
        
        
        start = 0
        end  = 1
        ans = ""
        for i in range(len(s)):
            #print(start,end)
            temp1 = self.expands(s,i,i)
            temp2 = self.expands(s,i,i+1)
            
            thisval = max(len(temp1),len(temp2))
            #print(temp1,temp2)
            if thisval > len(ans):
                #
                if len(temp1) > len(temp2):
                    ans = temp1
                else:
                    ans = temp2

                
        return ans

     
    def expands(self,s,i,j):
  
        while i >= 0 and j < len(s) and s[i] == s[j]:
            
            i-=1
            j+=1
         
     
        return s[i+1:j]
        
