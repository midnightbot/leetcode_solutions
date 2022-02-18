##ss
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        
        for x in num:
            while k and stack and stack[-1] > x:
                stack.pop()
                k-=1
                
            stack.append(x)
            
        if k > 0:
            stack = stack[:-k]
        
        if stack:
            return str(int(''.join(stack))) 
        
        return "0"
