class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ## simple find groups, return max grp size

        def check_valid(x,y):
            return 0<=x<len(grid) and 0<=y<len(grid[0])

        def gen_nei(x,y):
            arr = [(x,y+1), (x,y-1), (x+1,y), (x-1,y)]
            ans = []
            for it in arr:
                if check_valid(it[0], it[1]):
                    ans.append((it[0],it[1]))
            return ans 

        def do_bfs(x,y):
            q = [(x,y)]
            score = 0

            while q:
                new_q = []
                for x in range(len(q)):
                    xs = q[x][0]
                    ys = q[x][1]
                    score+=grid[xs][ys]
                    neis = gen_nei(xs,ys)
                    for it in neis:
                        if grid[it[0]][it[1]] > 0:
                            new_q.append((it[0],it[1]))

                    grid[xs][ys] = 0

                q = new_q
                    
                
            
            return score

        grps = []

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] > 0:
                    grps.append(do_bfs(x,y))

        return max(grps) if grps else 0

