##ss
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        q = []
        
        for x in piles:
            heapq.heappush(q,-x)
        
        
        for x in range(k):
            top = heapq.heappop(q)
            top = top // 2
            heapq.heappush(q,top)
            
        return -sum(q)
        
        
