## simple simulation
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ## 1 \
        ## -1 /
        
        ans = [0 for x in  range(len(grid[0]))]
        
        for cols in range(len(grid[0])):
            curr = cols
            for x in range(len(grid)):
                if cols == len(grid[0]) or cols == -1:
                    ans[cols] = -1
                    break
                elif grid[x][curr] == 1:
                    if curr+1 < len(grid[0]) and grid[x][curr+1] == 1:
                        curr+=1
                    else:
                        ans[cols] = -1
                        break
                        
                elif grid[x][curr] == -1:
                    if curr-1>=0 and grid[x][curr-1] == -1:
                        curr-=1
                    else:
                        ans[cols] = -1
                        break
                    
            if ans[cols]!=-1:
                ans[cols] = curr
        return ans
