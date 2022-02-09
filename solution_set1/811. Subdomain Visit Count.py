##ss
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        dicts = {}
        #print(ord('a'),"",ord('z'))
        for x in range(len(cpdomains)):
            
            temp = cpdomains[x].split(".")
            #count = 0
            for z in range(len(temp[0])):
                if ord(temp[0][z]) >=97 and ord(temp[0][z]) <= 122:
                    break
            count = int(temp[0][0:z])        
            temp[0] = temp[0][z:]
            #print(temp,count)
            make = temp[-1]
            if make in dicts:
                dicts[make]+=count
                
            else:
                dicts[make] = count
            for y in range(len(temp)-2,-1,-1):
                make = temp[y]+"." + make
                
                if make in dicts:
                    dicts[make]+= count
                    
                else:
                    dicts[make] = count
                    
        ans = []
        
        for x in dicts:
            s = str(dicts[x]) + " " + x
            ans.append(s)
            
        return ans
                    
        
