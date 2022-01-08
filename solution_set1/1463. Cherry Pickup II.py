##ss
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        
        
    
        @lru_cache(None)
        def expand(row,col1,col2):

            if col1 <0 or col1 >= self.n or col2 <0 or col2>=self.n:
                return -float('inf')


            ans = 0
            ans+=grid[row][col1]
            if col1!=col2:
                ans+=grid[row][col2]

            if row!=self.m-1:

                ans+=max(expand(row+1,newcol1,newcol2) for newcol1 in [col1-1,col1,col1+1] for newcol2 in [col2-1,col2,col2+1])


            return ans
        
        return expand(0,0,self.n-1)
        
        
