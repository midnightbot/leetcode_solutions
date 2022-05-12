##ss
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        ## ( >> )
        ## down or right
        
       
        m = len(grid)
        n = len(grid[0])
        
        visited = set()
        def dfs(x,y,brackets):
            
            if grid[x][y] == '(':
                brackets+=1
                
            else:
                brackets-=1
                
            if brackets < 0 or brackets > (m+n)//2 or (x,y,brackets) in visited:
                return False
            
            visited.add((x,y,brackets))
            
            if x==m-1 and y==n-1 and brackets == 0:
                return True
            
            if x<m-1 and dfs(x+1,y,brackets):
                return True
            
            if y<n-1 and dfs(x,y+1,brackets):
                return True
            
            
            return False
        
        
        return dfs(0,0,0)
                
            
        
        
        
        
