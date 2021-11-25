##ss
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        
        memo = {}
        ans = self.make_string(n,memo)
        return ans[k-1]
        
        
    def make_string(self,n,memo):
        
        if n == 1:
            memo[1] = "0"
            return memo[1]
        
        if n in memo.keys():
            return memo[n]
        
        ans = self.make_string(n-1,memo) + "1" + self.invert(self.make_string(n-1,memo))[::-1]
        memo[n] = ans
        return memo[n]
        
        
        
    def invert(self,strs):
        ans  = ""
        for x in range(len(strs)):
            if strs[x] == "1":
                ans+= "0"
                
            else:
                ans+="1"
                
        return ans
            
        
