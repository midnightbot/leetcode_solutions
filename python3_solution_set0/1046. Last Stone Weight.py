##ss
import queue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        ##priority queue always pops out smaller value first,
        ## but we want two largest stones
        ##hence trick is to store -ve values of stones, hence we will get 2 largest values everytime
        ans  = queue.PriorityQueue()
        for x in range(len(stones)):
            ans.put(-1*stones[x])
            
        #print(ans.queue)
        while len(ans.queue) > 1:
            t1 = -1 * ans.get()
            t2 = -1 * ans.get()
            
            if t1 > t2:
                ans.put(t2-t1)
                
        if len(ans.queue) == 0:
            return 0
        
        else:
            return ans.queue[0]*-1
        
