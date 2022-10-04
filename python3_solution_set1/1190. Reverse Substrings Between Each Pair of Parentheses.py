##ss
class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        
        for x in range(len(s)):
            if s[x]!=')':
                stack.append(s[x])
                
            elif s[x] == ')':
                indx = -1
                for a in range(len(stack)-1,-1,-1):
                    if stack[a] == '(':
                        indx = a
                        break
                        
                stack = stack[0:a] + stack[a+1:][::-1]
                
        return ''.join(stack)
        
