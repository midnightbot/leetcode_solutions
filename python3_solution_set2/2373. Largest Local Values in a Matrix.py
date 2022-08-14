class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        def find_max(arr):
            ans = -float('inf')
            for x in arr:
                ans = max(ans, max(x))
                
            return ans
        
        
        result = []
        m = len(grid)
        n = len(grid[0])
        
        for x in range(m-2):
            layer = []
            for y in range(n-2):
                temp = grid[x:x+3]
                tp = []
                for g in temp:
                    tp.append(g[y:y+3])
                #print(tp)
                layer.append(find_max(tp))
            result.append(layer)
        return result
