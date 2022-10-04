##ss
class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for x in range(len(s)):
            if len(stack)!=0 and stack[-1] == s[x]:
                stack.pop()
                
            else:
                stack.append(s[x])
                
        ans = "".join(stack)
        return ans
