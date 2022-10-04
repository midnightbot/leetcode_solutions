##Solution 1 (Time Limit Exceeded) Naive Solution 
class Solution:
    def numSplits(self, s: str) -> int:
        
        ans = 0
        
        for x in range(len(s)):
            if len(set(s[0:x])) == len(set(s[x:len(s)])):
                ans+=1
                
                
        return ans
        
##Solution 2
class Solution:
    def numSplits(self, s: str) -> int:
        
        ##2, 26 arrays
        ans = 0
        a = [0 for x in range(26)]
        b = [0 for x in range(26)]
        
        for x in range(len(s)):
            b[ord(s[x])-ord('a')]+=1
            
        for x in range(len(s)):
            a[ord(s[x])-ord('a')]+=1
            b[ord(s[x])-ord('a')]-=1
            
            #print(self.notzero(a) == self.notzero(b))
            if self.notzero(a) == self.notzero(b):
                ans+=1
                
        return ans
            
     
    def notzero(self,arr):
        
        ans = 0
        for x in range(26):
            if arr[x]!=0:
                ans+=1
                
        return ans
                
        
