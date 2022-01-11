##ss
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        
        self.result = set()
        self.n = len(s)
        dicts = {}
        for x in range(len(s)):
            if s[x] in dicts:
                dicts[s[x]] +=1
                
            else:
                dicts[s[x]] = 1
                
        if self.validate(dicts):
            self.combine(dicts)
            
        return self.result
            
                
                
    def validate(self,dicts):
        
        count = 0
        for x in dicts.keys():
            if dicts[x]%2!=0:
                count+=1
                
        return count <=1
    
    
    def combine(self,dicts):
        
        double = []
        single = []
        
        for x in dicts.keys():
            div = dicts[x] // 2
            rem = dicts[x] % 2
            
            for y in range(div):
                double.append(x)
                
            for z in range(rem):
                single.append(x)
              
        ans = [-1 for x in range(self.n)]
        #print("combining")
        self.rec_comb(single,double,0,self.n-1,ans)
        
        
    def rec_comb(self,single,double,startp,endp,ans):
        #print(ans)
        if startp == endp:
            ans[startp] = single[0]
            self.result.add(''.join(ans))
                
        elif startp > endp:
            
            self.result.add(''.join(ans))
   
        elif startp < endp:
            for y in range(len(double)):
                new_ans = copy.copy(ans)
                
                new_ans[startp] = double[y]
                new_ans[endp] = double[y]
                new_double = copy.copy(double)
                new_double.remove(double[y])
                self.rec_comb(single,new_double,startp+1,endp-1,new_ans)
        
        
        
                
        
