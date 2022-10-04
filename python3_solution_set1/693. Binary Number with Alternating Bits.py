##ss
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        #print(self.find_bin(5))
        return self.find_alt(self.find_bin(n))
        
        
    def find_bin(self,n):
        ans = ""
        
        for x in range(32):
            if n & 1<<x == 0:
                ans+="0"
                
            else:
                ans+="1"
        ans = ans[::-1]
        for x in range(len(ans)):
            if ans[x] == "1":
                break
        return ans[x:]
    
    
    def find_alt(self,strs):
        
        prev = strs[0]
        for x in range(1,len(strs)):
            
            if strs[x] == prev:
                return False
            
            else:
                prev = strs[x]
                
        return True
