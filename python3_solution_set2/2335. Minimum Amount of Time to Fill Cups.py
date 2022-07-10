import heapq
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        q = []
        for x in amount:
            if x!=0:
                heapq.heappush(q,-x)
            
       
        time = 0
        while q:
            
            if len(q) >= 2:
                top1 = heapq.heappop(q)
                top2 = heapq.heappop(q)

                top1+=1
                top2+=1
                time+=1
                
                if top1!=0:
                    heapq.heappush(q,top1)
                if top2!=0:
                    heapq.heappush(q,top2)
            
            if len(q) == 1:
                top1 = heapq.heappop(q)
                time-=top1
        
        return time
