##ss
##very good ques
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        stack = []
        
        last = {}
        
        for x in range(len(s)):
            last[s[x]] = x
            
        for x in range(len(s)):
            #print(stack)
            if s[x] in stack:
                continue
                
              
            while stack and stack[-1] > s[x] and last[stack[-1]] > x:
                stack.pop()
                
            stack.append(s[x])
            
        return ''.join(stack)
