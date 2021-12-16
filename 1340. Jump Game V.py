##ss
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        
        ##dp[i] be max jumps that can be made from pos i
        arr.insert(0,float('inf'))
        arr.append(float('inf'))
        
        #print(arr)
        dp= [1 for x in range(len(arr))]
        for x in range(1,len(arr)-1):
            dp[x] = self.dojump(x,dp,arr,1,d)
            #print(dp[x])
        
        return max(dp)
        
    def dojump(self,x,dp,arr,jumps,d):
        #print(dp)
        
        if dp[x]!=1:
            return dp[x]
        
        elif arr[x-1] >= arr[x] and arr[x+1] >= arr[x]:
            return 1
        
        else:
            
            for m in range(x+1,min(len(dp),x+1+d),1):
                
                if arr[m] < arr[x]:
                    dp[x] = max(dp[x],1+self.dojump(m,dp,arr,jumps+1,d))
                    
                else:
                    break
            #print(dp[x])
            for m in range(x-1,max(-1,x-1-d),-1):
                if arr[m] < arr[x]:
                    dp[x] = max(dp[x],1+self.dojump(m,dp,arr,jumps+1,d))
                    
                else:
                    break
  
            return dp[x]
                    
            
        
