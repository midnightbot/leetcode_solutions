##ss
##same as 1081
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        stack = []
        last = {}
        
        seen = set()
        
        for x in range(len(s)):
            last[s[x]] = x
            
            
        for x in range(len(s)):
            if s[x] in seen:
                continue
                
            while stack and stack[-1] > s[x] and last[stack[-1]] > x:
                t = stack.pop()
                seen.remove(t)
                
            stack.append(s[x])
            seen.add(s[x])
            
        return ''.join(stack)
        
