class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans  = []
        self.permute(s,0,"",ans)
        return ans
        
        
    def permute(self,s,index,strs,ans):
        if index>=len(s):
            ans.append(strs)
            return ans
            
        temp = s[index]
        if temp.isalpha():
            lower = strs + str(temp.lower())
            upper = strs+ str(temp.upper())
            
            self.permute(s,index+1,lower,ans)
            self.permute(s,index+1,upper,ans)
            
            
        else:
            self.permute(s,index+1,strs+temp,ans)
        
