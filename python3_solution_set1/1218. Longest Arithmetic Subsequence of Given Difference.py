##ss
##simple dp
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        ##diff is arr[x+1] - arr[x]
        ##simple dp 
        
        dp = [1 for x in range(len(arr))]
        
        dicts = {}
        dicts[arr[0]] = 0
        result = 1
        for x in range(1,len(dp)):
            find = arr[x] - difference
            #print(find)
            if find in dicts:
                #ans = -float('inf')
                #for y in range(len(dicts[find])):
                #ans = max(ans,dp[dicts[find][y]])
                    
                dp[x] = 1 + dp[dicts[find]]
                
            else:
                dp[x] = 1
            
            
            dicts[arr[x]] = x
                
            
            result = max(result,dp[x])
            
        return result
                
        #print(dp,dicts)
                
        
        
