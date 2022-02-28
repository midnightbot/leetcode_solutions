##ss
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ##exactly 4 numbers seperated by '.'
        ##each number must be in 0-255 range
        ## number is 0 then ok
        ## else number cannot start with 0
        ##numbers are eitherr 1digit, 2digit or 3digit
        
        self.result = []
        
        self.expand(s,0,"",[])
        return (self.result)
        
    def expand(self,s,pointer,prev,ans):
        #print(pointer,ans,prev,self.result)
        
        if pointer == len(s) and len(ans) == 4:
            self.result.append(".".join(ans))
            
            
        elif len(ans) == 3 and pointer!=len(s):
            if int(prev + s[pointer:]) <= 255 and (prev + s[pointer:])[0]!='0':
                ans.append(prev + s[pointer:])
                self.result.append('.'.join(ans))
            
            elif pointer == len(s) - 1 and prev + s[pointer] == '0':
                ans.append('0')
                self.result.append('.'.join(ans))
            #print('here',prev+s[pointer] == '0')     
        elif pointer == len(s) and len(ans) == 3:
            #print("inside",ans)
            if prev!="" and int(prev) == 0 and len(prev) == 1:
                ans.append(prev)
                self.result.append('.'.join(ans))
                
            elif prev!="" and 0 < int(prev) <= 255:
                ans.append(prev)
                
                self.result.append('.'.join(ans))
        
        elif len(ans) < 3 and pointer < len(s):
            
            if len(prev) < 3:
                temp = prev + s[pointer]
                if temp[0]!='0' and int(temp) <= 255:
                    #ans.append(temp)
                    self.expand(s,pointer+1,temp,ans)
                    
                if len(temp)==1 and temp[0] == '0':
                    newans = copy.deepcopy(ans)
                    newans.append('0')
                    self.expand(s,pointer+1,"",newans)
                if prev == '0':
                    newans = copy.deepcopy(ans)
                    newans.append(prev)
                    self.expand(s,pointer+1,s[pointer],newans)
                    
                
                elif prev!="" and int(prev)<=255:
                    newans = copy.deepcopy(ans)
                    newans.append(prev)
                    self.expand(s,pointer+1,s[pointer],newans)
        
            
            elif len(prev) == 3:
                if int(prev) <=255 and prev[0]!='0':
                    newans = copy.deepcopy(ans)
                    newans.append(prev)
                    self.expand(s,pointer+1,s[pointer],newans)
        
