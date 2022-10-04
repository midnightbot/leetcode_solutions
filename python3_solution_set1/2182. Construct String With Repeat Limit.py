import heapq
class Solution:
    def repeatLimitedString(self, s: str, rl: int) -> str:
        
        comp = Counter([x for x in s])
        
        temp = []
        
        for x in comp:
            temp.append([-ord(x),comp[x]]) ##min heaps issues :)
            
        q = []
        
        for x in temp:
            heapq.heappush(q,x)
        
        result = ""
        
        
        
        while q:
            elem,count = heapq.heappop(q)
            elem = chr(-elem)
            
            if count <= rl:
                result+= "".join([elem for x in range(count)])
                
            else:
                result+= "".join([elem for x in range(rl)])
                count-=rl
                
                if not q:
                    return result
                
                else:
                    next_elem,next_count = heapq.heappop(q)
                    next_elem = chr(-next_elem)
                    result+=next_elem
                    next_count-=1
                    
                    if next_count!=0:
                        heapq.heappush(q,[-ord(next_elem),next_count])
                        
                    heapq.heappush(q,[-ord(elem),count])
            
        return result
        
        
