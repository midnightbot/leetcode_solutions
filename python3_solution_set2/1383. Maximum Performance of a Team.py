import heapq
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        ans = -float('inf')
        curr = 0
        mods = 10**9+7
        n = len(speed)
        comp = [[efficiency[i], speed[i]] for i in range(n)]
        
        comp = sorted(comp, reverse = True)
        q = []
        for x,y in comp:
            while len(q) > k-1:
                curr-= heapq.heappop(q)
            heapq.heappush(q,y)
            curr+=y
            ans = max(ans, curr*x)
            
        return ans%mods
        
