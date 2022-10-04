class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        
        if str1 == str2:
            return True
        t1 = self.form_dicts(str1,str2)
        t2 = self.form_dicts(str2,str1)
        
        temps = set(str2)
        #print(len(temps))

        #print(self.check2(t1,str1,str2))
        if self.check1(t1) and len(temps) < 26:
                return True

            
        return False
        
        
    def form_dicts(self,str1,str2):
        dicts = {}
        for x in range(len(str1)):
          
            if str1[x] not in dicts.keys():
                dicts[str1[x]] = set()
                dicts[str1[x]].add(str2[x])

            else:
                dicts[str1[x]].add(str2[x])
                    
        return dicts
    
    
    def check1(self,dicts1):
        for x in dicts1.keys():
            if len(dicts1[x])!=1:
                return False
            
        return True
    
    def check2(self,dicts1,str1,str2):
        var = -1
        c = 0
        for x in dicts1.keys():
            #print(var,str1[(c+1)%len(str1)],dicts1[x])
            if list(dicts1[x])[0] != str1[(c+1)%len(str1)]:
                var = -1
                
            else:
                var+=1
                
            c+=1
        if var == -1:
            return True
        else:
            return False
                
        

     
