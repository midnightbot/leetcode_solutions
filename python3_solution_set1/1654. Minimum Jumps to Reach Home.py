import heapq
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        ## 'a' fwd, 'b' back
        ## bb not allowed
        ## cannot jump to forbidden pos
        
        ## simple dp
        ## can also do with bfs, create a graph
        
        forb = set(forbidden)
        
        
        memo = {}
        def can_reach(node,back):
            
            if node < 0:
                return float('inf')
            
            elif node in forb:
                return float('inf')
            
            elif node == x:
                return 0
            
            elif 8000 <= node + a - b:
                return float('inf')
            
            elif (node,back) not in memo:
                memo[(node,back)] = 1 + can_reach(node+a,False)
                
                if back == False:
                    memo[(node,back)] = min(memo[(node,back)], 1 + can_reach(node-b,True))
                    
                return memo[(node,back)]
            else:
                return memo[(node,back)]
            
        
        return can_reach(0,False) if can_reach(0,False)!=float('inf') else -1
            
