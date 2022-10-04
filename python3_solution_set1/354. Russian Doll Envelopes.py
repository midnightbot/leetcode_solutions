##ss
##Solution 1 (Normal dp Time Limit Exceeded)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        
        envelopes = sorted(envelopes)
        dp = [1 for x in range(len(envelopes))]
        #print(envelopes)
        
        print(envelopes)
        
        for x in range(1,len(envelopes)):
            for y in range(x):
                if envelopes[x][0] > envelopes[y][0] and envelopes[x][1] > envelopes[y][1]: ## we will do this operation using binary search
                    dp[x] = max(dp[x], 1 + dp[y])
                    
        return max(dp)
        
  ##Solution 2
  
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        
        ans = []
        
        envelopes = sorted(envelopes, key = lambda x:(x[0],-x[1]))
        #print(envelopes)
        ## we know that length of all prev envelopes is smaller than this envelopes
        ## we just have to find lis on heights now
        
        ##lonest increasing subsequence problem now
        
        for x in range(len(envelopes)):
            indx = bisect_left(ans, envelopes[x][1])
            
            if indx == len(ans):
                ans.append(envelopes[x][1])
                
            else:
                ans[indx] = envelopes[x][1]
           
        print(ans)
        return len(ans)
                
                
