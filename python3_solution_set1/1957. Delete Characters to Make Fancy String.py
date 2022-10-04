##ss
class Solution:
    def makeFancyString(self, s: str) -> str:
        
        stack = []
        
        for x in range(len(s)):
            if len(stack) < 2:
                stack.append(s[x])
                
            else:
                if stack[-1] == stack[-2] == s[x]:
                    continue
                    
                else:
                    stack.append(s[x])
                    
        return ''.join(stack)
        
