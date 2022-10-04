class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #opt[i] be min number of coins required for amount i
        
        opt = [float('inf')] * (amount + 1)
        opt[0] = 0
        for x in coins:
            for y in range(x,amount+1):
                opt[y] = min(opt[y],opt[y-x]+1)
                
        if opt[amount]!=float('inf'):
            return opt[amount]
        
        else:
            return -1
        
