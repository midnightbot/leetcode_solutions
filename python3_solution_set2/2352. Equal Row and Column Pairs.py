##ss
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        def make_key(arr):
            arr = [str(x) for x in arr]
            return ",".join(arr)
    
        ro = {}
        col = {}
        
        for x in grid:
            key = make_key(x)
            ro[key] = ro.get(key,0) + 1
            
        for x in range(len(grid[0])):
            key = ""
            for y in range(len(grid)):
                key+=str(grid[y][x])+","
                
            key = key[:-1]
            #print(key)
            col[key] = col.get(key,0) + 1
            
        ans = 0
        for x in ro:
            if x in col:
                ans+=ro[x]*col[x]
                
        return ans
        #print(ro,col)    
        
