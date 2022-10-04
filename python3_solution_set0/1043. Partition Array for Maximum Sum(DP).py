class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        #opt[i] be optimal ans for 0..i
        
        memo = [-1] * len(arr)
        memo[0] = arr[0]
        #memo[1] = max(arr[0],arr[1])*2
        #memo[2] = max(arr[0],arr[1],arr[2])*3
        
        for y in range(1,k): ##initialization
            
            memo[y] = max(arr[0:y+1]) * (y+1)
        
        for x in range(k,len(arr)):
            #print(memo)
            maxs = max(arr[x-k+1:x+1])
            for z in range(1,k+1):
                maxs = max(arr[x-z+1:x+1])
                memo[x] = max(memo[x],memo[x-1] + arr[x], maxs*z + memo[x-z])
        #print(memo)    
        return memo[len(arr)-1]
