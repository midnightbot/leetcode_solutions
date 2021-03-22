class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        
        ans = []
        
        for x in range(1,n+1):
            if n%x==0:
                ans.append(x)
                
        if len(ans) >= k:
            return ans[k-1]
        else:
            return -1
        
