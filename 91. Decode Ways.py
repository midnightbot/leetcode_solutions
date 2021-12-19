##ss
class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s[0] == 0:
            return 0
        return self.ways_to_make(0,s)
     
    @lru_cache(None)
    def ways_to_make(self,index,s):
        ans = 0
        if index == len(s):
            return 1
        
        elif s[index] == "0":
            return 0
        
        elif index == len(s) - 1:
            return 1
        
        else:
            if int(s[index:index+2]) <= 26:
                ans+=self.ways_to_make(index+2,s)
                
            ans+=self.ways_to_make(index+1,s)
            
            return ans
        
