class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        ans  = [0 for x in range(n+1)]
        
        ans[0] = 0
        ans[1] = 1
        
        for x in range(2,n+1):
            if x%2==0:
                
                ans[x] = ans[int(x/2)]
                
            else:
                ans[x] = ans[int((x-1)/2)] + ans[int(((x-1)/2) + 1)]
        
        return max(ans)
