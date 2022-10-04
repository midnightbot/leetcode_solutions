##ss
class Solution:
    def countCollisions(self, directions: str) -> int:
        
        
        stack  = []
        c = 0
        stack.append(directions[0])
        
        for x in range(1,len(directions)):
            
            if directions[x] == 'L' and stack[-1] == 'S':
                c+=1
                
            elif directions[x] == 'L' and stack[-1] == 'R':
                c+=2
                stack.pop()
                while stack and stack[-1] == 'R':
                    #print("isndn")
                    c+=1
                    stack.pop()
                stack.append("S")
                
            elif directions[x] == 'S' and stack[-1] == 'R':
                
                while stack and stack[-1] == 'R':
                    #print("isndn")
                    c+=1
                    stack.pop()
                stack.append("S")
                
            else:
                stack.append(directions[x])
                    
            #print(stack)
               
        
        return c
