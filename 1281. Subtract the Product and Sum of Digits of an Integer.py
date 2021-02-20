class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(x) for x in str(n)]
        a1 = 1
        a2 =0
        
        for x in range(len(digits)):
            a2 = a2 + digits[x]
            a1 = a1 * digits[x]
            
        return a1-a2
            
        
