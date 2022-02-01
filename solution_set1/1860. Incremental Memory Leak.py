##ss
import heapq
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        
        arr = []
        heapq.heappush(arr,(-1*memory1,1))
        heapq.heappush(arr,(-1*memory2,2))
        time = 0
        
        top,a = heapq.heappop(arr)
        top*=-1
        
        heapq.heappush(arr,(-1 * top,a))
        time = 1
        while top >= time:
            #print(arr)
            newtime = heapq.heappop(arr)
            t = newtime[0]
            t*=-1
            elem = newtime[1]
            
            t-=time
            heapq.heappush(arr,(-1*t,elem))
            c,d = heapq.heappop(arr)
            c*=-1
            top = c
            heapq.heappush(arr,(c*-1,d))
            time+=1
            
            
        ans = [0,0,0]
        ans[0] = time
        
        a,b = heapq.heappop(arr)
        c,d = heapq.heappop(arr)
        
        ans[b] = -1 *a
        ans[d] = -1*c
        
        return ans
        
