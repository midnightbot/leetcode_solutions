##ss
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        stack.append("root")
        temp = path.split("/")
        for x in range(len(temp)):
            #print(stack)
            if temp[x] == "..":
                if len(stack) > 0:
                    stack.pop()
                
            elif temp[x] == "/":
                continue

            elif temp[x]!="" and temp[x]!=".":
                stack.append(temp[x])
                
        ans = "/"
        for x in range(0,len(stack)):
            if stack[x]!="root":
                ans+=stack[x]
                ans+="/"
        
        if len(ans) == 1:
            return "/"
        return ans[0:len(ans)-1]
        
