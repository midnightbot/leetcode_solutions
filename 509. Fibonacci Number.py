class Solution:
    def fib(self, n: int) -> int:
        
        ans = []
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        else:
            
            ans.append(1)
            ans.append(1)
            
            for x in range(2,n+1):
                ans.append(ans[x-1]+ans[x-2])
            
            return ans[n-1]
        
