##ss
##Solution1 (Time Limit Exceeded)
##Recursive Approach
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        mod = pow(10,9) + 7
        
        @lru_cache(None)
        def get_ans(n):
            if n == 1:
                return "1"
            elif n > 1:
                return str(format(int(get_ans(n-1) + str(format(n,"b")),2)%mod,"b"))
        
        
        return int(get_ans(n),2)
        
 ##Solution2 (Iterative approach)
 class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        mod = pow(10,9) + 7
        #print(bin(10))
        ans = ''.join(format(x,"b") for x in range(n+1))
        return int(ans,2)%mod
        
