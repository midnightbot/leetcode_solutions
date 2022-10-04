##ss
##Solution1 (Using DP, Time Limit Exceeded)
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        @lru_cache(None)
        def go_fwd(pt,bricks,ladders):
            
            if pt + 1 < len(heights) and heights[pt+1] <= heights[pt]:
                return 1 + go_fwd(pt+1,bricks,ladders)
                
            elif pt + 1 < len(heights) and heights[pt+1] > heights[pt]:
                ans = 0
                
                
                if bricks >= (heights[pt+1]-heights[pt]):
                    
                    ans = max(ans,1 + go_fwd(pt+1,bricks - (heights[pt+1]-heights[pt]),ladders))
                    
                if ladders > 0:
                    
                    ans = max(ans, 1 + go_fwd(pt+1,bricks,ladders-1))
                    
                return ans
            
            else:
                return 0
            
            
        return go_fwd(0,bricks,ladders)
                
        
        
  ##Solution2 (Greedy Approach)
  import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        ##greedy solution
        ##longer jumps use ladder, shorter jumps use bricks
        ##python heaps are always min-heaps
        
        jumps = []
        maxjumps = []
        #heights.insert(0,heights[0])
        for x in range(len(heights)-1):
            jumps.append(max(0,heights[x+1]-heights[x]))
        #print(jumps)  
        #print("jumps")
        if ladders == 0:
            pt = 0
            while bricks >= 0 and pt < len(jumps):
                bricks-=jumps[pt]
                pt+=1
            
            if bricks >=0:
                return pt
            
            return pt-1
                
        for x in range(len(jumps)):
            
            if jumps[x] > 0:
                if ladders > 0:
                    heapq.heappush(maxjumps,jumps[x])
                    ladders-=1

                elif ladders == 0:
                    top = heapq.heappop(maxjumps)
                    if  top < jumps[x]:
                        heapq.heappush(maxjumps,jumps[x])

                        if bricks >= top:
                            bricks-=top
                            
                        else:
                            return x
                        
                        
                    else:
                        heapq.heappush(maxjumps,top)
                        
                        if bricks > jumps[x]:
                            bricks-=jumps[x]
                        elif bricks == jumps[x]:
                            bricks = 0
                            
                        else:
                            return x
            #print(x,maxjumps,ladders,bricks)
        return len(heights)-1          
                    
            
            
