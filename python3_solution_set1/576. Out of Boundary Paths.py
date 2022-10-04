##ss
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, r: int, c: int) -> int:
        
        ## inital position -> [startrow, startcolumn]
        ##movement -> up,down,left,right
        ##atmost 'maxmove'
        
        modulo = 10**9 + 7
        
        dp = [[0 for x in range(n)]for y in range(m)]
        
       
        
        @lru_cache(None)
        def paths(i,j,move):
            if move < 0:
                return 0
            
            if i < 0 or i==m or j < 0 or j==n:
                return 1
            
            return (paths(i+1,j,move-1)%modulo + paths(i-1,j,move-1)%modulo + paths(i,j-1,move-1)%modulo + paths(i,j+1,move-1)%modulo)%modulo
        
        
        return paths(r,c,maxMove)
            
   
