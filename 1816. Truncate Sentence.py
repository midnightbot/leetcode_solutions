class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        #ans = len(s.split())
        count = 0
        ans = ""
        final_ans = ""
        temp = len(s.split())
        for x in range(len(s)):
            if count >= k:
                break
            else:
                if s[x]!= " ":
                    ans+=s[x]
                    
                else:
                    ans+=s[x]
                    count+=1
        
        if temp == k:
            return ans
        for y in range(len(ans)-1):
            final_ans+= ans[y]
            
        return final_ans
                    
                    
        
                
        
