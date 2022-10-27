class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        
        ## simple line sweep algorithm
        lights = [[x[0]-x[1], x[0]+x[1]] for x in lights] ## make the ranges for each light
        maps = {}
        
        #+1 on position of start of range
        #-1 on position of end of range
        for x,y in lights:
            maps[x] = maps.get(x,0)+1
            maps[y+0.01] = maps.get(y+0.01,0)-1
            
        ans = 0
        result = -1
        curr = 0
        for indx in sorted(maps.keys()):
            curr+=maps[indx]
            #print(indx)
            if curr > ans:
                ans = curr
                result = indx
                
        return result
        
