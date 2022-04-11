##ss
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        q = []
        tasks = [[x[0],x[1],c] for c,x in enumerate(tasks)]
        n = len(tasks)
        tasks = sorted(tasks)
        i = 0
        start_time = tasks[0][0]
        
        while len(ans)!=n:
            
            while i < len(tasks) and tasks[i][0] <= start_time:
                heapq.heappush(q,[tasks[i][1],tasks[i][2]])
                i+=1
                
            if q:
                new_elem = heapq.heappop(q)
                start_time+=new_elem[0]
                ans.append(new_elem[1])
                
            else:
                start_time = tasks[i][0]
                
        return ans
            
        
