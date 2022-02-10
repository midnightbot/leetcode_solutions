##ss
class Solution:
    def nextClosestTime(self, time: str) -> str:
        
        digits = set()

        hrs = time[0:2]
        mins = time[3:]
        #print(hrs,mins)
        for x in range(len(time)):
            if ord(time[x])>=48 and ord(time[x])<=57:
                digits.add(int(time[x]))
         
        digits = list(digits)
        combinations = self.formation(digits)
        #print(combinations)
        
        for x in range(len(combinations)):
            if int(combinations[x]) > int(mins):
                return hrs+":"+combinations[x]
            
        for x in range(1,25):
            #print(str((int(hrs)+x)%24))
            if str((int(hrs)+x)%24) in combinations:
                break
        #print(int(hrs) + x)    
        newhrs = str((int(hrs)+x)%24)
        newmins = combinations[0]
        
        if len(newhrs) == 1:
            newhrs = "0" + newhrs
            
        if len(newmins) == 1:
            newmins = "0" + newmins
            
            
        return newhrs+":"+newmins
        
    def formation(self,digits):
        comb = set()
        
        for x in range(len(digits)):
            for y in range(len(digits)):
                thisans = str(digits[x]) + str(digits[y])
                
                if int(thisans)>=0 and int(thisans)<=59:
                    comb.add(thisans)
                    
        comb = list(comb)
        #comb = sorted(comb)
        for x in range(len(comb)):
            if comb[x][0] == "0":
                comb.append(comb[x][1])
                
        comb = sorted(comb)
        
        return comb
        
