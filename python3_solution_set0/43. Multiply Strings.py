class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        temp1 = 0
        factor = 1
        for x in range(len(num1)-1,-1,-1):
            temp1 += (ord(num1[x])-(ord('0')))*factor
            factor*=10
            
        temp2 = 0
        factors = 1
        for y in range(len(num2)-1,-1,-1):
            temp2+=(ord(num2[y])-ord('0'))*factors
            factors*=10
        
        
        ans = temp1 * temp2
        return str(ans)
            
        
        
            
        
