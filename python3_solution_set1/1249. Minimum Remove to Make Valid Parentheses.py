##ss
##12 mins
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        ##remove min ( or ) to make it valid
        ## empty, only lowercase
        ## AB -> A,B are valid
        ## (A) -> A is valid
        
        ##if at any time bracket count is -ve then remove that bracket
        
        count = 0
        notes = []
        ans = ""
        for x in range(len(s)):
            if s[x] == '(':
                count+=1
                ans+=s[x]
            elif s[x] == ')':
                count-=1
                
                if count < 0:
                    notes.append(x)
                    count = 0
                else:
                    ans+=s[x]
                    #count = 0
            else:
                ans+=s[x]
        
        print(ans)
        count = 0
        for x in range(len(ans)):
            if ans[x] == '(':
                count+=1
                
            elif ans[x] == ')':
                count-=1
                
        if count == 0:
            return ans
        
        elif count > 0:
            ##remove count ( from ans from the end
            result = ""
            for x in range(len(ans)-1,-1,-1):
                if ans[x]!='(':
                    result+=ans[x]
                    
                elif ans[x]=='(' and count!=0:
                    count-=1
                    
                    
                elif ans[x]=='(' and count == 0:
                    result+=ans[x]
                    
            return result[::-1]
            
       
