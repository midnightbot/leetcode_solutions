##Solution 1 (Using Eval Function)
## Now our only task is to create a new eval function for on our own  (Created eval function in Solution 2 below)
class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        x= 0
        
        while x < len(s):
            
            if s[x] == "(":
                stack.append(s[x])
                x+=1
                
            elif s[x] == ")":
                temp = []
                top = stack.pop()
                while top!="(":
                    temp.append(top)
                    top = stack.pop()
                    
                #print(temp) ##evaluate this expression and push on stack top
                new_t = ""
                for k in range(len(temp)-1,-1,-1):
                    #print("hello")
                    new_t+=temp[k]
                #print(new_t)
                #print(new_t)
                #for x in range(len(temp))
                ans = eval(new_t)
                #print(ans)
                stack.append(str(ans))
                    
                x+=1
                
            else:

                stack.append(s[x])
                x+=1
        temp_f = ""
        #print(stack)
        for x in range(len(stack)):
            temp_f+=stack[x]
            
        return eval(temp_f)
      
      
## Solution 2 (Created Own Eval function)
class Solution:
    def calculate(self, s: str) -> int:
        
        stack = []
        x= 0
        
        while x < len(s):
            
            if s[x] == "(":
                stack.append(s[x])
                x+=1
                
            elif s[x] == ")":
                temp = []
                top = stack.pop()
                while top!="(":
                    temp.append(top)
                    top = stack.pop()
                    
                #print(temp) ##evaluate this expression and push on stack top
                new_t = ""
                for k in range(len(temp)-1,-1,-1):
                    #print("hello")
                    new_t+=temp[k]
                #print(new_t)
                #print(new_t)
                #for x in range(len(temp))
                ans = self.evals(new_t)
                #ans = eval(new_t)
                #print(ans)
                stack.append(str(ans))
                    
                x+=1
                
            else:

                stack.append(s[x])
                x+=1
        temp_f = ""
        #print(stack)
        for x in range(len(stack)):
            temp_f+=stack[x]
        ##temp_f = temp_f[::-1]
        #print(temp_f)
        #print(self.evals(temp_f))
        return self.evals(temp_f)
        #return eval(temp_f)
    
    def evals(self,s):
        
        tempo = ""
        x = 0 
        #print(s)
        s = s.replace(" ","")
        while x < len(s):
            if s[x] == "-" and x+1 < len(s) and s[x+1]!="-":
                tempo+="+"
                tempo+='-'
                x+=1
                
            elif s[x] == '-' and x+1 < len(s) and s[x+1]=='-':
                tempo+='+'
                x+=2
            else:
                tempo+=s[x]
                x+=1
        ans = tempo.split("+")
        #print(ans)
        #print(ans)
        #print(ans)
        for x in range(len(ans)):
            if ans[x] == "":
                ans[x] = 0
            else:
                #ans[x] = ans[x].replace(" ","")
                ans[x] = int(ans[x])
        #print(ans)
        return sum(ans)
            
        
