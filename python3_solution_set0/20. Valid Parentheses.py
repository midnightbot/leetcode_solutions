##ss
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        
        #visited = []
        if s.count(")")!=s.count("(") or s.count("[")!=s.count("]") or s.count("{")!=s.count("}"):
            return False
        for x in range(len(s)):
            #print(stack)
            if s[x] == "]" and "[" not in stack:
                return False
            
            elif s[x] == ")" and "(" not in stack:
                #print("(" in stack)
                return False
            
            elif s[x] == "}" and "{" not in stack:
                return False
            
            
            elif s[x] == "]" and "[" in stack:
                head  = -1
                while head!="[" and len(stack)!=0:
                    head = stack.pop()
                    #print(head)
                    
                if head!="[":
                    return False
                
            elif s[x] == ")" and "(" in stack:
                head  = -1
                while head!="(" and len(stack)!=0:
            
                    head = stack.pop()
                   
                if head!="(":
                    return False
                
            elif s[x] == "}" and "{" in stack:
                head  = -1
                while head!="{" and len(stack)!=0:
                    head = stack.pop()
                    
                if head!="{":
                    return False
                
            else:
                stack.append(s[x])
                
                
        if len(stack) == 0:
            return True
        else:
            return False
                    
        
