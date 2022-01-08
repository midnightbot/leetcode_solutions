##ss
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
        
        
