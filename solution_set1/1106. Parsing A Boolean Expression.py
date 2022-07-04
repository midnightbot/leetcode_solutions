##ss
class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        
        stack  = []
        for x in exp:
            if x == 't':
                stack.append(True)
            elif x=='f':
                stack.append(False)
                
            elif x==',':
                continue
                
            elif x == '(':
                stack.append('(')
                
            elif x == ')':
                arr = []
                while stack[-1]!='(':
                    arr.append(stack.pop())
                    
                stack.pop() ## '('
                exps = stack.pop() ## operation
                
                if len(arr)==1 and exps == "!":
                    stack.append(not arr[0])
                    
                elif exps == '&':
                    ans = True
                    for it in arr:
                        ans = ans and it
                        
                    stack.append(ans)
                    
                elif exps=='|':
                    ans = False
                    for it in arr:
                        ans = ans or it
                        
                    stack.append(ans)
                
            
                
            else:
                stack.append(x)
                
        return stack[0]
