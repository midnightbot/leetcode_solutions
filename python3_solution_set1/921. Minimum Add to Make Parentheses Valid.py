##ss
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        ##empty, AB, (A)
        
        ins = 0
        
        balance = 0
        
        for x in range(len(s)):
            if s[x] == '(':
                balance+=1
                
            elif s[x] == ')':
                balance-=1
                
            if balance < 0:
                ins+= balance * -1
                balance = 0
                
        if balance > 0:
            return ins + balance
        elif balance == 0:
            return ins
        
        else:
            return ins + 1
        
        
