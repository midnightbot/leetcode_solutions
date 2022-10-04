##ss
##Solution1 (Time Limit Exceeded 50/64 Testcases passed)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ##number of distinct subseq which equal t
        
        q = [s]
        
        i = 0
        
        while i < len(t):
            #print(q)
            for x in range(len(q)):
                strings = q.pop(0)

                comp = self.find_pos(strings, t[i])
                
                if len(comp)!=0:
                    for z in comp:
                        q.append(strings[z+1:])
                        
            i+=1
            
        return len(q)
                
                
                
    def find_pos(self,s,chrs):
        
        ans = []
        for x in range(len(s)):
            if s[x] == chrs:
                ans.append(x)
        return ans
 ##Solution2 (Simple DP , Accepted)
 class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        
        @lru_cache(None)
        def calc(i,j):
            
            if i == len(s) or j == len(t) or len(s) - i < len(t) - j:
                
                if j == len(t):
                    return 1 
                
                else:
                    return 0
                
            ans = calc(i+1,j)
            
            if s[i] == t[j]:
                ans+= calc(i+1,j+1)
                
            return ans
        
        return calc(0,0)
        
