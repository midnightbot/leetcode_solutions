class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ## horizontal and vertical movements
        ## approach 1
        ## whenever we see a 1 do bfs and make all connecting 1 to 0
        ## count the number of islands == number of bfs runs
        ## approach 2
        ## union find
        
        n = len(grid)
        m = len(grid[0])
        parent = {}

        def valid(x,y):
            return 0<=x<n and 0<=y<m

        for x in range(n):
            for y in range(m):
                parent[(x,y)] = -1

        def find_parent(x,y):
            if parent[(x,y)] == -1:
                return (x,y)

            parent[(x,y)] = find_parent(parent[(x,y)][0], parent[(x,y)][1])
            return parent[(x,y)][0], parent[(x,y)][1]

        ## union of two islands
        def union(x1,y1,x2,y2):
            p1 = find_parent(x1,y1)
            p2 = find_parent(x2,y2)

            if p1!=p2:
                parent[p1] = p2

        for x in range(n):
            for y in range(m):
                if grid[x][y] == '1':
                    if valid(x-1,y) and grid[x-1][y] == '1':
                        union(x,y,x-1,y)

                    if valid(x,y-1) and grid[x][y-1] == '1':
                        union(x,y,x,y-1)
        
        ## to update the parents of all to point the highest parent in hierarchy
        for x in parent:
            find_parent(x[0], x[1])

        ## to make all the single ones also an island
        for x in range(n):
            for y in range(m):
                if grid[x][y] == '1' and  parent[(x,y)] == -1:
                    parent[(x,y)] = (x,y)

        ## find count of unique parents
        islands = set()
        for x in parent:
            if parent[x]!=-1:
                islands.add(parent[x])

        return len(islands)
