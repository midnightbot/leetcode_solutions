##ss
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        def convs(strs):
            
            hrs = int(strs[0:2])
            mins = int(strs[3:])
            
            return hrs*60 + mins
        
        
        seen = {}
        
        alerts = set()
        
        syss = []
        
        for x in range(len(keyName)):
            syss.append([convs(keyTime[x]),keyName[x]])
            
        syss = sorted(syss, key = lambda x:x[0])
        
        for x,y in syss:
            
            if y not in seen:
                seen[y] = [x]
                
            else:
                seen[y].append(x)
                
                if len(seen[y]) >= 3 and seen[y][-1] - seen[y][-3]<=60:
                    alerts.add(y)
                    
        return sorted(list(alerts))
            
            
            
        
