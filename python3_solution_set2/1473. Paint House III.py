##ss
class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        ## m houses
        ## n colors
        
        
        ## either house will be given prev color
        ## or following color 
        ## or new color
        grps = []
        
        @lru_cache(None)
        def find_ans(indx, prev_color, neigh_left):
            if neigh_left < 0 or neigh_left > m-indx:
                return float('inf')
            
            if indx == m:
                if neigh_left == 0:
                    return 0
                else:
                    return float('inf')
                
            else:
                if houses[indx]:
                    return find_ans(indx+1, houses[indx], neigh_left - (houses[indx]!=prev_color))
                
                else:
                    ans = float('inf')
                    for x in range(1,n+1):
                        #print(x,indx)
                        ans = min(ans, cost[indx][x-1] + find_ans(indx+1,x,neigh_left-(prev_color!=x)))
                    return ans
                
        ans = find_ans(0,0,target)
        return ans if ans < float('inf') else -1
                    
                
                
                
                
                
            
            
        
