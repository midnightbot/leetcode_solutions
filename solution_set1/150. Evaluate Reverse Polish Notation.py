##ss
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        
        for x in range(len(tokens)):
            #print(stack)
            if tokens[x]!="+" and tokens[x]!="-" and tokens[x]!="*" and tokens[x]!="/":
                stack.append(int(tokens[x]))
                
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                
                if tokens[x] == "+":
                    stack.append(num2+num1)
                    
                elif tokens[x] == "-":
                    stack.append(num2-num1)
                    
                elif tokens[x] == "*":
                    stack.append(int(num2*num1))
                    
                elif tokens[x] == "/":
                    temps = num2/num1
                    #print(temps)
                    if temps < 0:
                        temps = math.ceil(temps)
                    else:
                        temps = math.floor(temps)
                    stack.append(temps)
                    
        return stack[0]
            
        
