class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        
        curr = 0
        temp = []
        
        for x,y in logs:
            diff = y - curr
            temp.append([diff, x])
            curr+=diff
            
        #print(temp)
        c = max([x[0] for x in temp])
        #print(c)
        ans = float('inf')
        
        for x,y in temp:
            if x == c:
                ans = min(ans, y)
                
        return ans
        
        
