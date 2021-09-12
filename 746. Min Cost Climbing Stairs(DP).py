class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def min_cost(i):
            
            if i<=1:
                return 0
            
            if i in memo:
                return memo[i]
            
            one_step = cost[i-1] + min_cost(i-1)
            two_step = cost[i-2] + min_cost(i-2)
            
            memo[i] = min(one_step,two_step)
            
            return memo[i]
        
        memo = {}
        return min_cost(len(cost))
        
