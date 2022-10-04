class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climb_stairs(0,n,memo)
        
    def climb_stairs(self,i: int, n: int, memo = {}) -> int:
        if i in memo:
            return memo[i]
        if i>n:
            return 0
        
        elif i==n:
            return 1
        
        memo[i] = self.climb_stairs(i+1,n,memo)+self.climb_stairs(i+2,n,memo)
        return memo[i]
        
