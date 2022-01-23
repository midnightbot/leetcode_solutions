##ss
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        cost = sorted(cost,reverse=True)
        result = 0
        for x in range(len(cost)):
            if (x+1)%3!=0:
                result+=cost[x]
                
                
        return result
        
