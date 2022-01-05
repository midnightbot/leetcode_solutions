class Solution:
    def minCut(self, s: str) -> int:
        
        ##dp[x] be min partitions required for string s[0:x]
        
        dp = [float('inf') for x in range(len(s))]
        dp[0] = 0
        #dp[1] = 0
        
        for x in range(1,len(s)):
            #print(s[0:x])
            if s[0:x+1] == s[0:x+1][::-1]:
                dp[x] = 0
                
            else:
                
                #min_ans = float('inf')
                for y in range(x+1,-1,-1):
                    #print(s[y:x+1],x,y,dp)
                    if s[y:x+1]!="" and s[y:x+1] == s[y:x+1][::-1]:
                        #print("inside")
                        dp[x] = min(dp[x],1+dp[y-1])
                    
                    
         
        #print(dp)
        return dp[len(dp)-1]
      
        
        
        
        
        
