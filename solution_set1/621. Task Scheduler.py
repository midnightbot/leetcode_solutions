##ss
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        
        ##1 task or idle
        
        ## 'n' units of time between same tasks
        
        ##finish all tasks
        ##if more than 'n' elements left choose most freq 'n' elements and reduce their count by 1
        ##time+=n
        
        ##if less than 'n' elems are left choose all of them and reduce their count by 1
        ##time+=n , idle time = n + 1 - len(q)
        time = 0
        if n == 0:
            return len(tasks)
        
        dicts = {}
        for x in range(len(tasks)):
            dicts[tasks[x]] = dicts.get(tasks[x],0) + 1
            
        #print(dicts)
        comp = []
        for x in dicts:
            heapq.heappush(comp,[-1*dicts[x],x])
            
        done = len(tasks)
        time = 0
        while done!=0:
            
            if len(comp) > n:
                removed = []
                for z in range(n+1):
                    t = heapq.heappop(comp)
                    done-=1
                    time+=1
                    t[0]+=1
                    if t[0]!=0:
                        removed.append(t)
                 
                for z in removed:
                    heapq.heappush(comp,z)
                    
                    
            else:
                removed = []
                k = len(comp)
                for z in range(k):
                    t = heapq.heappop(comp)
                    done-=1
                    time+=1
                    t[0]+=1
                    if t[0]!=0:
                        removed.append(t)
                
                if done!=0:
                    time+=(n+1-k)
                
                for z in removed:
                    heapq.heappush(comp,z)
                    
        return time
