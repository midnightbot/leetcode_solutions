class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        
        ans = 0
        balance = 0
        
        for x,y in transactions:
            ans+= max(0,x-y)
            balance = max(balance, min(x,y))
            
        return ans + balance
        
