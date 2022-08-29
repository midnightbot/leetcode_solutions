class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for x in s:
            if x!="*":
                stack.append(x)
            else:
                while stack and stack[-1]=="*":
                    print("inside")
                    
                stack.pop()
        
        return "".join(stack)
        
