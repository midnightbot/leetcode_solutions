##ss
##Solution 1 (Time Limit Exceeded)
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        #print(pow(3,9))
        #return []
        self.n = len(num)
        self.result = []
        self.expand(1,num,target,[num[0]],num[0])
        return self.result

    
    def expand(self,pointer,num,target,exp,curr):
        #print(exp,pointer)
        if pointer == len(num):
            
            expression = self.makestring(exp)
            
            if eval(expression) == target:
                self.result.append(expression)
                
        elif pointer < len(num):
            exp1 = copy.copy(exp)
            if len(exp1) >= 1:
                
                    
                exp1.append("+")
                exp1.append(num[pointer])

                self.expand(pointer+1,num,target,exp1,num[pointer])

            exp2 = copy.copy(exp)
            if len(exp2) >= 1:
                
                exp2.append("-")
                exp2.append(num[pointer])
                #print(exp2,"exp2")
                self.expand(pointer+1,num,target,exp2,num[pointer])
            
            exp3 = copy.copy(exp)
            if len(exp3) >= 1:
                exp3.append("*")
                exp3.append(num[pointer])                   
                self.expand(pointer+1,num,target,exp3,num[pointer])
           
            
                #temp = exp.pop()
            if curr !="0":
                temp = exp.pop()
                temp+= num[pointer]
                
                exp.append(temp)
                self.expand(pointer+1,num,target,exp,exp[-1])
 
        
    def makestring(self,exps):
        ans = ""
        for x in range(len(exps)):
            ans+=exps[x]
            
        return ans
        

##Solution 2 (Same as Solution1 rather than using array to store current expression, stored it directly into a string)
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        
        #print(pow(3,9))
        #return []
        self.n = len(num)
        self.result = []
        self.expand(1,num,target,num[0],num[0])
        return self.result

    
    def expand(self,pointer,num,target,exp,curr):
        #print(exp,pointer)
        if pointer == len(num):
            
            #expression = self.makestring(exp)
            
            if eval(exp) == target:
                self.result.append(exp)
                
        elif pointer < len(num):
            #exp1 = copy.copy(exp)
            if len(exp) >= 1:
  
                self.expand(pointer+1,num,target,exp+"+"+num[pointer],num[pointer])

                self.expand(pointer+1,num,target,exp+"-"+num[pointer],num[pointer])
         
                self.expand(pointer+1,num,target,exp+"*"+num[pointer],num[pointer])
           
            
                #temp = exp.pop()
            if curr !="0":
                new_curr = str(int(curr+num[pointer]))
                self.expand(pointer+1,num,target,exp+num[pointer],new_curr)
 
        
    def makestring(self,exps):
        ans = ""
        for x in range(len(exps)):
            ans+=exps[x]
            
        return ans
        
        
