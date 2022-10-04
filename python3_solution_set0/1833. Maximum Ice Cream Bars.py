class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs = sorted(costs)
        
        count = 0
        while count < len(costs) and  costs[count] <= coins :
            
            coins = coins - costs[count]
            count+=1
            
        return count
            
        
