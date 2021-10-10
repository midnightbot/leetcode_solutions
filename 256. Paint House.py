## 0th index red
## 1st index blue
## 2nd index green

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if costs == []:
            return 0
        return min(self.paint(0,0,costs,{}),self.paint(0,1,costs,{}),self.paint(0,2,costs,{}))
        
        
    
    def paint(self, n, color,costs, memo={}):
        if (n,color) in memo:
            return memo[(n,color)]
        total_cost = costs[n][color]
        if n == len(costs) - 1:
            pass
        
        elif color == 0:
            total_cost+= min(self.paint(n+1,1,costs,memo),self.paint(n+1,2,costs,memo))
            
        elif color == 1:
            total_cost+= min(self.paint(n+1,0,costs,memo), self.paint(n+1,2,costs,memo))
            
        else:
            total_cost+= min(self.paint(n+1,0,costs,memo), self.paint(n+1,1,costs,memo))
            
        memo[(n,color)] = total_cost
        return memo[(n,color)]
        
