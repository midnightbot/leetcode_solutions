##ss
import heapq
class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if num == 0:
            return num
        if num < 0:
            num = -1 * num
            comp = [x for x in str(num)]
            comp = sorted(comp, reverse = True)
            
            ans = ''.join(comp)
            return -1 * int(ans)
            
            
        comp = [x for x in str(num)]
        comp = sorted(comp)
        dicts = {}
        
        for x in range(len(comp)):
            if comp[x] in dicts:
                dicts[comp[x]]+=1
                
            else:
                dicts[comp[x]] = 1
                
        
        #dicts = sorted(dicts)
        #print(dicts)
        ans = ""
        #print(comp,dicts)
        for x in range(len(comp)):
            #print(ans)
            for m in dicts:
                if len(ans)!=0:
                    ans+=str(m)
                    dicts[m]-=1
                    if dicts[m] == 0:
                        dicts.pop(m)
                    break
                elif len(ans) == 0 and int(m)!=0:
                    ans+=str(m)
                    dicts[m]-=1
                    if dicts[m] == 0:
                        dicts.pop(m)
                    break
        return int(ans)
        
        
