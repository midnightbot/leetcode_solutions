class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        ## max diff can be m+n (travelling first col and then first row with all 1)
        m,n = len(grid), len(grid[0])
        @cache
        def find_ans(x,y,diff):
            if grid[x][y]==0:
                diff+=1
            else:
                diff-=1

            if x==m-1 and y==n-1 and diff==0:
                return True

            if x+1<m and find_ans(x+1,y,diff):
                return True

            if y+1 < n and find_ans(x,y+1,diff):
                return True

        return find_ans(0,0,0)

