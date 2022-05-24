##ss
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        ans = 0
        stack.append(-1)
        
        for x in range(len(s)):
            if s[x] == '(':
                stack.append(x)
                
            else:
                stack.pop()
                if not stack:
                    stack.append(x)
                else:
                    ans = max(ans , x - stack[-1])
                    
        return ans
        
