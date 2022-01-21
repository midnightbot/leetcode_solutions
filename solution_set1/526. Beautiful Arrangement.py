##simple recursion
class Solution:
    def countArrangement(self, n: int) -> int:
        self.result = 0
        #print([(x+1) for x in range(n)])
        self.expand(n,[(x+1) for x in range(n)],1,"")
        return self.result
   
    def expand(self, n,left,pointer,ans):
        #print(left,"->",pointer,"-->",ans)
        if pointer > n:
            #print(ans)
            self.result+=1
        
        elif len(left)!=0:
            #print(left)
            for x in range(len(left)):
                if (left[x]%pointer==0) or (pointer%left[x] == 0):
                    
                    temp = left[x]
                    left.remove(temp)
                    self.expand(n,left,pointer+1,ans+str(temp))
                    left.insert(x,temp)
                    
        
                
            
        
