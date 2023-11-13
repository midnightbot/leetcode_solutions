class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        deg = {x:[0,0] for x in range(len(grid))}

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    deg[x][0] += 1 ## indegree
                    deg[y][1] += 1 ## outdegree

        ## ans will be team with 0 outdegree and >0 indegree

        for x in deg:
            if deg[x][0] > 0 and deg[x][1] == 0:
                return x

        return -1
        
