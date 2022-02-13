class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        ans = 0
        costs = sorted(costs, key = lambda x: x[0]-x[1])
        
        for x in range(len(costs)//2):
            ans+=costs[x][0] + costs[len(costs)//2 + x][1]
            
        return ans
        
