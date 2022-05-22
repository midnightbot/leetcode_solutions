##ss
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extra: int) -> float:
        
        q = []
        ans = 0
        print(eval('-1 * (4/6 - 3/5)'))
        for x,y in classes:
            
            #print(((x++/y++) - (x/y)))
            heapq.heappush(q,[-1 * (((x+1)/(y+1)) - (x/y)),x,y])
            
        #print("___")
        #print(q)
        for c in range(extra):
            top,x,y = heapq.heappop(q)
            
            x+=1
            y+=1
            heapq.heappush(q,[-1 * (((x+1)/(y+1)) - (x/y)),x,y])
            
        #print(q)
        return sum([x[1]/x[2] for x in q]) / len(classes)
