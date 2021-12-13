##ss
class Solution:
    def totalMoney(self, n: int) -> int:
        
        amount = 0
        
        base = 0
        prev = 0
        for x in range(n):
            if x%7==0:
                base+=1
                amount+=base
                prev = base
                
            else:
                prev+=1
                amount+=prev
                
        return amount
            
        
