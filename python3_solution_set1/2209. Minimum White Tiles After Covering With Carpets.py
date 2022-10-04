##ss
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        
        ## 0-> black
        ## 1-> white
        
        ##simple dp, either a mattress starting from this white tile, or this white tile does not have mattress over it
        
        wh = [0 for x in range(len(floor)+1)]
        for x in range(len(floor)-1,-1,-1):
            if floor[x] == '1':
                wh[x] = wh[x+1] + 1
            else:
                wh[x] = wh[x+1]
        
        
        @lru_cache(None)
        def find_mins(pos,left):
            
            if pos >= len(floor):
                return 0
            
            elif floor[pos] == '0':
                return find_mins(pos+1,left)
            
            elif floor[pos] == '1':
                if left > 0:
                    return min(find_mins(pos+carpetLen,left-1), 1+ find_mins(pos+1,left))
                
                elif left == 0:
                    
                    return wh[pos]
        
        return find_mins(0,numCarpets)
        
